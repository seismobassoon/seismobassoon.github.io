#!/bin/bash

shopt -s nullglob

#token 
TOKEN="$DROPBOX_TOKEN"
create_link () {

  local path="$1"

  RESPONSE=$(curl -s https://api.dropboxapi.com/2/sharing/list_shared_links \
    --header "Authorization: Bearer $TOKEN" \
    --header "Content-Type: application/json" \
    --data "{\"path\":\"$path\",\"direct_only\":true}")

  LINK=$(echo "$RESPONSE" | jq -r '.links[0].url // empty')

  if [[ -z "$LINK" ]]; then
      RESPONSE=$(curl -s https://api.dropboxapi.com/2/sharing/create_shared_link_with_settings \
        --header "Authorization: Bearer $TOKEN" \
        --header "Content-Type: application/json" \
        --data "{\"path\":\"$path\"}")

      LINK=$(echo "$RESPONSE" | jq -r '.url // empty')
  fi

  echo "$LINK" | sed 's/dl=0/raw=1/'
}
  
# --------------------------
# 1️⃣ Paramètres
# --------------------------
localDropbox="/Users/nobuaki/Dropbox (IPGP)/shared_for_website"
#files_txt="files.txt"
json_out="data/dropbox.json"
mkdir -p data

# --------------------------
# 2️⃣ Dictionnaire abbr -> name
# --------------------------

instrumentOrder=(
    score
vn v1 v2 v3 v4
va va1 va2
vc vc1 vc2
db db1 db2
bg
fl fl1 fl2 pic xiao
ob ob1 ob2 ca
cl cl1 cl2 bcl
altosx altosx1 altosx2 tensx barsx
bn bn1 bn2 dbn
hu
hr hr1 hr2
tp tp1 tp2
tb tb1 tb2 btb tu
dig
timp
perc
pf
hp
uk
poem
)

declare -A nameMap=(
  [vn]="Violin" [v1]="Violin I" [v2]="Violin II" [v3]="Violin III" [v4]="Violin IV"
  [va]="Viola" [va1]="Viola I" [va2]="Viola II"
  [vc]="Cello" [vc1]="Cello I" [vc2]="Cello II"
  [db]="Double Bass" [db1]="Double Bass I" [db2]="Double Bass II"
  [bg]="Bass Guitar"
  [fl]="Flute" [fl1]="Flute I" [fl2]="Flute II" [pic]="Piccolo" [xiao]="Xiao"
  [ob]="Oboe" [ob1]="Oboe I" [ob2]="Oboe II" [ca]="English Horn"
  [cl]="Clarinet" [cl1]="Clarinet I" [cl2]="Clarinet II" [bcl]="Bass Clarinet"
  [altosx]="Alto Sax" [altosx1]="Alto Sax I" [altosx2]="Alto Sax II"
  [tensx]="Tenor Sax" [barsx]="Baritone Sax"
  [bn]="Bassoon" [bn1]="Bassoon I" [bn2]="Bassoon II" [dbn]="Double Bassoon"
  [hu]="Hulu"
  [hr]="Horn" [hr1]="Horn I" [hr2]="Horn II"
  [tp]="Trumpet" [tp1]="Trumpet I" [tp2]="Trumpet II"
  [tb]="Trombone" [tb1]="Trombone I" [tb2]="Trombone II" [btb]="Bass Trombone" [tu]="Tuba"
  [dig]="Didgeridoo" [timp]="Timpani" [uk]="Ukulele" [poem]="Poem"
  [perc]="Percussion" [pf]="Piano" [hp]="Harp"
)


declare -A fileURL
declare -A fileName
declare -A foldersSeen
# --------------------------
# 3️⃣ Générer files.txt
# --------------------------
#[ -f "$files_txt" ] && rm "$files_txt"
#> "$files_txt"

for f in "$localDropbox"/musicSheets/*/*.pdf "$localDropbox"/musicSheets/*/*/*.pdf; do
    relpath="${f#"$localDropbox/musicSheets/"}"
    folder=$(dirname "$relpath")
    filename=$(basename "$f")
    #url="https://www.dropbox.com/home/nobuaki%20fuji/shared_for_website/musicSheets/$folder/$filename?raw=1"
    dropboxPath="/shared_for_website/musicSheets/$folder/$filename"
    url=$(create_link "$dropboxPath")
    # abbr et mapping
    abbr="${filename%.pdf}"
    name="${nameMap[$abbr]}"
    [[ -z "$name" ]] && name="$abbr"
     key="$folder|$abbr"

    fileURL[$key]="$url"
    fileName[$key]="$name"
    foldersSeen[$folder]=1
    #echo "$folder|$url|$name" >> "$files_txt"
done
#echo "✅ files.txt généré !"
folders=("${!foldersSeen[@]}")
# --------------------------
# 4️⃣ Générer dropbox.json
# --------------------------
[ -f "$json_out" ] && rm "$json_out"
echo '{}' > "$json_out"
for folder in "${folders[@]}"; do

  for inst in "${instrumentOrder[@]}"; do

    key="$folder|$inst"

    if [[ -n "${fileURL[$key]}" ]]; then

      url="${fileURL[$key]}"
      name="${fileName[$key]}"

      obj=$(jq -n --arg url "$url" --arg name "$name" '{url:$url,name:$name}')

      jq --arg folder "$folder" --argjson obj "$obj" \
         'if .[$folder] then .[$folder]+=[$obj] else .[$folder]=[$obj] end' \
         "$json_out" > tmp.json && mv tmp.json "$json_out"

    fi

  done

done

echo "✅ dropbox.json généré !"