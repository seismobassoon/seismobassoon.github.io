#!/usr/bin/env python3
"""Add Dropbox share links for score PDFs to data/dropbox.json.

Usage (from the repo folder):
    export DROPBOX_TOKEN='...'      # generate it on https://www.dropbox.com/developers/apps (your app > Settings)
    python3 makeJsonScores.py            # only folders not yet in dropbox.json
    python3 makeJsonScores.py --all      # recompute every folder

Safe by design: existing entries are kept, and nothing is written if any Dropbox call fails.
"""
import json, os, sys, urllib.request, urllib.error

ROOTS = [os.path.expanduser("~/IPGP Dropbox/nobuaki fuji/shared_for_website"),
         os.path.expanduser("~/Dropbox (IPGP)/shared_for_website")]
API_PREFIX = "/shared_for_website/musicSheets"   # path as seen by the Dropbox API
JSON_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "dropbox.json")

ORDER = """score vn v1 v2 v3 v4 va va1 va2 vc vc1 vc2 db db1 db2 bg fl fl1 fl2 pic xiao ob ob1 ob2 ca
cl cl1 cl2 bcl altosx altosx1 altosx2 tensx barsx bn bn1 bn2 dbn hu hr hr1 hr2 tp tp1 tp2 tb tb1 tb2 btb tu
dig timp perc pf hp uk sc poem""".split()
NAMES = {"vn":"Violin","v1":"Violin I","v2":"Violin II","v3":"Violin III","v4":"Violin IV","va":"Viola","va1":"Viola I","va2":"Viola II",
 "vc":"Cello","vc1":"Cello I","vc2":"Cello II","db":"Double Bass","db1":"Double Bass I","db2":"Double Bass II","bg":"Bass Guitar",
 "fl":"Flute","fl1":"Flute I","fl2":"Flute II","pic":"Piccolo","xiao":"Xiao","ob":"Oboe","ob1":"Oboe I","ob2":"Oboe II","ca":"English Horn",
 "cl":"Clarinet","cl1":"Clarinet I","cl2":"Clarinet II","bcl":"Bass Clarinet","altosx":"Alto Sax","altosx1":"Alto Sax I","altosx2":"Alto Sax II",
 "tensx":"Tenor Sax","barsx":"Baritone Sax","bn":"Bassoon","bn1":"Bassoon I","bn2":"Bassoon II","dbn":"Double Bassoon","hu":"Hulu",
 "hr":"Horn","hr1":"Horn I","hr2":"Horn II","tp":"Trumpet","tp1":"Trumpet I","tp2":"Trumpet II","tb":"Trombone","tb1":"Trombone I",
 "tb2":"Trombone II","btb":"Bass Trombone","tu":"Tuba","dig":"Didgeridoo","timp":"Timpani","uk":"Ukulele","sc":"SoundCube","poem":"Poem",
 "perc":"Percussion","pf":"Piano","hp":"Harp"}

def api(endpoint, payload, token):
    req = urllib.request.Request("https://api.dropboxapi.com/2/sharing/" + endpoint,
        data=json.dumps(payload).encode(),
        headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as r:
            return json.load(r), None
    except urllib.error.HTTPError as e:
        return None, e.read().decode(errors="replace")

def share_link(path, token):
    res, err = api("list_shared_links", {"path": path, "direct_only": True}, token)
    if err: raise RuntimeError(f"{path}: {err}")
    if res["links"]:
        url = res["links"][0]["url"]
    else:
        res, err = api("create_shared_link_with_settings", {"path": path}, token)
        if err: raise RuntimeError(f"{path}: {err}")
        url = res["url"]
    return url.replace("dl=0", "raw=1")

def main():
    token = os.environ.get("DROPBOX_TOKEN", "").strip()
    if not token or token == "your_token":
        sys.exit("DROPBOX_TOKEN is not set (export DROPBOX_TOKEN='...').")
    root = next((r for r in ROOTS if os.path.isdir(r)), None)
    if not root: sys.exit("shared_for_website folder not found: " + " / ".join(ROOTS))
    sheets = os.path.join(root, "musicSheets")
    data = json.load(open(JSON_OUT)) if os.path.exists(JSON_OUT) else {}
    redo_all = "--all" in sys.argv

    folders = {}
    for d, _, files in os.walk(sheets):
        pdfs = sorted(f for f in files if f.lower().endswith(".pdf"))
        if pdfs: folders[os.path.relpath(d, sheets)] = pdfs

    todo = [f for f in sorted(folders) if redo_all or f not in data]
    if not todo:
        print("Nothing to do: every folder is already in dropbox.json."); return
    new = {}
    for folder in todo:
        print("→", folder)
        entries = []
        for f in folders[folder]:
            abbr = f[:-4]
            url = share_link(f"{API_PREFIX}/{folder}/{f}", token)
            entries.append((ORDER.index(abbr) if abbr in ORDER else len(ORDER), {"url": url, "name": NAMES.get(abbr, abbr)}))
        new[folder] = [e for _, e in sorted(entries, key=lambda x: x[0])]
    data.update(new)
    tmp = JSON_OUT + ".tmp"
    json.dump(data, open(tmp, "w"), indent=2, ensure_ascii=False)
    os.replace(tmp, JSON_OUT)
    print(f"✅ dropbox.json updated ({len(new)} folder(s) added, {len(data)} in total).")

if __name__ == "__main__":
    try: main()
    except RuntimeError as e: sys.exit("❌ Dropbox error, nothing written:\n" + str(e))
