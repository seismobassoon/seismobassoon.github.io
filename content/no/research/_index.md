+++
title = "Forskning"
draft = false
+++

Fra global og regional tomografi til forening av skalaer gjennom mineralogiske, petrologiske og geodynamiske føringer – med den unike plattformen `flexOPT.jl`

{{< collapse title="Generell innledning" >}}

Målet med forskningen min er å avgrense utviklingen av det indre av terrestriske legemer bedre ved å analysere (geo)fysiske data, særlig seismiske bølgeformer.

Gjennom årene har jeg utviklet numeriske og teoretiske metoder for bølgeforminversjon som tar hensyn til mediets elastiske og viskoelastiske egenskaper på ulike skalaer, og anvendt dem på reelle data.

Et av mine viktigste bidrag er utviklingen av såkalt *boks-tomografi* på flere skalaer, som avbilder en lokal region (en «boks») fra seismiske bølgeformer som har passert ikke bare innsiden av regionen, men også omgivelsene.

Først presenterer jeg finansieringen som har gjort forskningen mulig. Deretter viser jeg en serie elastiske og anelastiske avbildningsstudier av mikrodynamikken under Karolineplaten, utført sammen med geodynamikere og petrologer. Så reiser jeg spørsmål om metoder, resultater og tolkninger. Deretter beskriver jeg den teoretiske og numeriske verktøykassen jeg har bygget opp for ulike vitenskapelige problemstillinger. Til slutt beskriver jeg forskningsprosjektet jeg ønsker å lede med nåværende og fremtidige partnere.

![Skisse av boks-tomografi](/images/schema_box.png)

*
Eksempler på anvendelser av boks-tomografi på ulike skalaer:
(a) i global seismologi brukes teleseismiske skjelv for å avbilde lokale regioner;  
(b) under Karolineplaten: 1D- og 3D-bølgeforminversjon for `Vs` og `Qs`;  
(c) 1D- og 3D-inversjon for `Vs` i LLVP-en under Hawaii;  
(d) mot nøytrinoavbildning;  
(e) føringer på oppstigningen av partiell smelte under Réunion;  
(f) 3D-avbildning av `Vp`, `Vs` og tetthet under Tibetplatået, nylig utvidet til Fuji-fjellet.
*
{{< /collapse >}}

{{< collapse title="Finansiering" >}}

To tredjedeler av doktorgraden min ble finansiert av JSPS (Japan Society for the Promotion of Science). I Japan fikk doktorgradsstudenter fram til begynnelsen av 2010-tallet ikke systematisk finansiering. Jeg måtte derfor skrive min egen forskningssøknad, sentrert rundt utvikling av bølgeforminversjon for elastisitet og anelastisitet, noe som tidlig ga meg et kritisk blikk på det å skrive forskningssøknader.

Fra 2012 til 2017 var jeg samarbeidspartner og hovedansvarlig for undervisningen i GPX-konsortiet for letegeofysikk. Konsortiet fremmet forskning og utdanning i skjæringspunktet mellom universiteter og industri. Mitt teoretiske arbeid med lokalisert bølgeforminversjon og grunnleggende beregning av syntetiske seismogrammer la grunnlaget for min nåværende nye metode: *optimale operatorer for vilkårlige partielle differensialligninger*.

Deretter bidro jeg til forstudiene for seismometeret på Mars-oppdraget InSight, noe som førte meg til den første bestemmelsen av fokalmekanismer på Mars med mine inversjonsmetoder.

Parallelt fikk jeg flere bevilgninger til å arrangere internasjonale workshops, som ga varige samarbeid. Takket være mitt nære samarbeid med Frédéric Deschamps (Academia Sinica) deltok jeg i flere fransk-taiwanske prosjekter, der jeg utviklet serien av seismo-petrologiske avbildningsstudier beskrevet nedenfor. Partnerskapet ga meg muligheten til å veilede min første offisielle doktorgradsstudent, S.-T. Lai, gjennom utlysningen MOPGA (*Make Our Planet Great Again*).

Siden 2022 har jeg vært juniormedlem av Institut universitaire de France (IUF) innen vitenskapsformidling, noe som lar meg bruke tid både på forskningen og på formidling til allmennheten.

Nylig har jeg fått flere doktorgradsfinansieringer, særlig knyttet til karakterisering av Fuji-fjellet. Et nært samarbeid er også innledet med Véronique Van Elewyck, og sammen har vi fått to postdoktorstillinger om nøytrinotomografi for avbildning av den dype jorden fra geofysiske observabler.

{{< /collapse >}}


{{< collapse title="Resultater: mantelens mikrodynamikk under Karolineplaten" >}}

![Skisse av Karolineplaten](/images/caro_schema.jpg)

Forenklet skisse av en serie tomografiske studier av mantelen under Karolineplaten. Våre tomografiske bilder, kombinert med petrologiske prediksjoner, tyder på at en dyp mantelplume rett ved kanten av Stillehavs-/Hawaii-LLVP-en kan føre med seg jern fra kjerne–mantel-grensen. I overgangssonen ovenfor finnes en grunnere plume som forsyner Eauripik-ryggen og kan bidra til den raske dynamikken i Karoline-mikroplaten.

I denne delen presenterer jeg kort studiene mine basert på bølgeforminversjonen jeg har utviklet gjennom karrieren, og begrenser meg til serien av tomografiske studier av øvre og nedre mantel under Karoline-platen. Øverst er mikroplaten omgitt av store, gamle plater, mens regionen nederst i mantelen tilsvarer en sone med lav skjærbølgehastighet (LLVP) under Hawaii. Vi har avbildet en liten, sannsynligvis jernrik plume som stiger fra bunnen av mantelen, kanskje helt opp til å forsyne ryggen på Karoline-platen, og som skyver mikroplaten sørover i høy fart – noe som gir et *roll-over*-subduksjonsregime.

### Karoline-platen

Karoline-platen har en særlig kompleks geodynamisk ramme: avgrenset av Den australske, Den filippinske og Stillehavsplaten ligger den i en sone med rask konvergens, preget av aktive og gamle subduksjoner, transformmarginer, forlatte rift og vedvarende vulkansk aktivitet. En hovedstruktur, Eauripik-ryggen, bryter opp midten av platen og utgjør en betydelig topografisk og magmatisk anomali, tolket enten som en gammel død rygg eller som sporet etter en dyp plume eller hotspot.

Geometrien til de magnetiske anomaliene, batymetrien og strukturer som Sorol-trauet eller Ny-Guinea-gropene vitner om en dynamikk som fortsatt er dårlig forstått, og som muligens henger sammen med dyp oppstrømning fra kjerne–mantel-grensen.

### Dyp struktur og Karoline-plumen

Vi har gjennomført en serie seismiske avbildningsstudier i regionen med bølgeforminversjonsmetoden jeg utviklet under doktorgraden og postdoktortiden. Metoden avbilder med høy oppløsning skjærbølgehastigheten `Vs` og kvalitetsfaktoren `Qs`, som er særlig følsomme for termiske kontraster. Med data fra det japanske F-net-nettverket for dype skjelv i Tonga- og Fiji-regionene påviste vi en markert, lokal anomali i `Vs` og `Qs` sentrert under Karoline-plumen.

Tolkningen tyder på et lokalt temperaturoverskudd på rundt 100 K i Stillehavs-LLVP-en, samt et mulig bidrag fra jernrikt materiale i plumen, som er uforenlig med en rent termisk modell. Analysen ble utvidet til andre deler av Stillehavet for å bekrefte at anomaliene er lokale. Geodynamisk og mineralogisk modellering tyder på mulig vekselvirkning med kjerne–mantel-grensen over flere hundre kilometer i høyden.

### Struktur i overgangssonen og øvre mantel

Til slutt gjennomførte vi en Monte Carlo-inversjon av gangtider for flere faser for å avgrense strukturen i mantelens overgangssone under Karoline-platen. Den endelige modellen, basert på SS-datasett og bølgeformmodellering, viser unormalt høy skjærbølgehastighet i hele øvre mantel. Etter flere geodynamiske simuleringer konkluderte vi med at den seismiske modellen tyder på mulig *roll-over*-subduksjon fra den sørlige og muligens også den nordlige grensen, samt plumeformede lavhastighetsanomalier som strekker seg minst til 800 km dyp under Karoline-platen. Simuleringene viser dessuten at *roll-over*-subduksjon krever et relativt raskt platedytt.

{{< /collapse >}}

{{< collapse title="Åpne spørsmål" >}}

Selv om denne lokaliserte avbildningsmetoden, *boks-tomografi*, har kastet lys over noen regioner som er avgjørende for å forstå manteldynamikken, gjenstår mange punkter å forbedre eller avklare, både vitenskapelig og teknisk.

En av de største flaskehalsene er at heterogenitetene utenfor boksen neglisjeres. Hittil har vi bare brukt sfæriske 1D-modeller til å simulere bølgefeltet, både ved beregning av bølgeformenes partielle deriverte og ved rekonstruksjon av bølgefeltet på boksens grenser. Vi har vurdert feilforplantningen fra denne tilnærmingen i en kartesisk ramme, men mangelen på en streng behandling av ytre effekter er fortsatt en viktig begrensning som må tas mer på alvor framover. Kobling av spektralelementmetoden med min DSM-metode er lovende, men svært ressurskrevende. Dette er blant grunnene til at jeg nylig har satt i gang en fullstendig omorganisering av min numeriske verktøykasse.

Når det gjelder oppstigningen av Karoline-plumen, gjenstår det å avbilde mantelen mellom 800 og 2500 km dyp, for å sjekke om plumesøylen er sammenhengende fra kjerne–mantel-grensen til overflaten. Bortsett fra studiene våre av plumens basis har vi ennå ikke hatt anledning til å tolke de tomografiske modellene kvantitativt; de er så langt bare uttrykt i seismologiske parametere som `Vs` og `Qs`. Det er nå avgjørende å samarbeide med petrologer, geokjemikere og geodynamikere for å tolke og utnytte strukturene seismologien avdekker bedre. Til dette foreslår jeg en innovativ seismisk filtreringstilnærming kalt *SeLFiE*.

{{< /collapse >}}

{{< collapse title="Numeriske og teoretiske verktøy" >}}

![Koder og flexOPT](/images/codes.jpg)

Status for kodene mine fram til 2023 (venstre) og den nylige utviklingen av `flexOPT.jl` (høyre). Figuren oppsummerer utviklingen av verktøyene mine, fra de historiske Fortran-kodene til det generiske metaprogrammet i Julia som automatisk utleder optimale operatorer for vilkårlige PDL-er.

Det som skiller min tilnærming fra andre seismologers, er at jeg er interessert i manteldynamikk og kjemiske prosessers rolle i den, samtidig som jeg utvikler numeriske skjemaer, både for inversjon og forovermodellering. Jeg analyserer data samtidig som jeg utformer de teoretiske og numeriske verktøyene for å tolke dem.

Siden doktorgraden har jeg utviklet mange koder basert på Direct Solution Method (DSM) i frekvensdomenet for sfæriske planeter, og på endelig-differansemetoden i tidsdomenet med modifiserte operatorer. Begge tilnærmingene hviler på et felles teoretisk grunnlag: optimale operatorer. En stor del av arbeidet mitt har gått til den numeriske implementeringen av denne teorien gjennom egne koder.

Optimale operatorer er kompakte operatorer som oppnår høyere nøyaktighet enn konvensjonelle operatorer med samme antall punkter i rom og tid. Den generelle metoden for å utlede dem var imidlertid aldri formulert systematisk. Jeg bidro selv til å optimalisere operatorer for spektralelementer, uten å tenke meg at en generell oppskrift var innen rekkevidde.

De fleste av kodene var skrevet i Fortran og vanskelige å vedlikeholde: én kode per formål, med lang og tungvint feilsøking. Jeg bestemte meg derfor nylig for å starte på nytt og utforme ett enkelt metaprogram som dekker mange bruksområder. *Julia* var et naturlig valg takket være metaprogrammering, symbolsk manipulasjon og god integrasjon med moderne verktøy som MPI og GPU-er.

I samarbeid med Thibault Duretz, som foreslo flere testligninger og måter å optimalisere koden på, kunne jeg formalisere en generell metode for automatisk å utlede optimale operatorer for vilkårlige partielle differensialligninger. Et preprint om tilnærmingen er sendt til *Computer Methods in Applied Mechanics and Engineering*.

Ved siden av testing og benchmarking brukes `flexOPT.jl` allerede til å løse ulike partielle differensialligninger, blant annet av doktorgradsstudenten min Hesaneh Mohammadi i et tomografiprosjekt om Fuji-fjellet, der den sammenlignes med andre referansekoder.

{{< /collapse >}}

{{< collapse title="Forskningsprosjekt: helhetlig visjon" >}}

![Strategi tomografi–geodynamikk–SeLFiE](/images/tomo_projet.jpg)

Skisse av forskningsprosjektene jeg ønsker å gjennomføre.  
Venstre: forbedring av bølgeformtomografi fra global til lokal skala, med hensyn til effekter utenfor boksen.  
Midten: litologisk tolkning og seismologisk filtrering med *SeLFiE*.  
Høyre: modellering av mantelkonveksjon og generering av virtuelle jordkloder der seismiske og nøytrino-observabler kan beregnes.

Som nevnt ovenfor følger flere prosjekter naturlig av forskningen min. Nå som prosjektet mitt med å modernisere og demokratisere optimale operatorer er modent, er det tid for å ta disse resultatene fullt i bruk for å se på seismologiske og andre data på nytt, og ta fatt på noen av de store spørsmålene i geovitenskapen: Hvordan har planetene utviklet seg siden solsystemet ble dannet, og hvordan vil de utvikle seg i framtiden? Hva gjør vår planet så unik blant naboene?

{{< /collapse >}}

{{< collapse title="Bølgeformtomografi mellom lokal og global skala" >}}

*Boks-tomografi* bygger på antakelsen om at det innkommende bølgefeltet kan anslås tilstrekkelig nøyaktig, enten fra en 1D-referansemodell for jorden eller ved å anta plane bølger. Tilnærmingen holder rimelig godt for enkelte isolerte førsteankomster av romlige bølger, som direkte P-, PKP- eller S-bølger, men blir utilstrekkelig ved høye frekvenser, der koherensen i det globale bølgefeltet ikke lenger kan garanteres.

For å omgå denne begrensningen foreslår jeg å bruke flere mer realistiske tomografiske modeller, som SEISGLOB2, som gir en mer tro framstilling av komplekse bølger, særlig der mantelheterogenitet påvirker de observerte fasene sterkt. For å avgrense usikkerhetene bedre vil jeg bruke flere modeller fra ulike observabler, som overflatebølger eller gangtider for romlige bølger.

Jeg vil dermed oppdatere boks-tomografien til å ta hensyn til heterogeniteter utenfor interesseområdet. Syntetiske tester er allerede gjort i en kartesisk ramme, men anvendelse i global seismologi blir en premiere. Den nye versjonen krever løsere som kan modellere 3D-medier i to nøstede domener (globalt og lokalt), noe som motiverte utviklingen av `flexOPT.jl`.

Jeg vil særlig utforske faser som kan avbilde regionen fra bunnen av mantelen til overflaten av Karoline-platen, for `Vs`, `Qs`, `Vp`, `Qp` og i et neste steg anisotropi. Det vil bidra til å forstå dynamikken i plumen jeg har avbildet, fra mantelens bunn til øvre mantel. Regionen under Karoline-mikroplaten kan by på et aldri tidligere observert, geodynamisk eksotisk scenario ved kanten av Hawaii-LLVP-en.

Jeg planlegger også å anvende metoden i andre geodynamisk aktive regioner, særlig øvre mantel og overgangssonen under Japan, Réunion og Tibetplatået.

Ved å bruke globale modeller til å forfine det lokale bildet i boksene kan vi forbedre oppløsningen av den dype jorden steg for steg. Det er imidlertid velkjent at bølgeforminversjon lider sterkere av ikke-entydighet og ikke-linearitet enn inversjon av sekundære attributter som overflatebølgedispersjon eller gangtider. Det er derfor avgjørende å starte fra realistiske startmodeller. Jeg vil også fortsette å tolke tomografiske modeller sammen med petrologer, for å oversette dem til fysisk-kjemiske parametere som er mer relevante for manteldynamikken.

{{< /collapse >}}

{{< collapse title="Tomografi med nøytrinooscillasjoner" >}}

Nylig har høyenergifysikere fått interesse for å bruke oscillasjonene til nøytrinoer som passerer gjennom jorden, til å avbilde dens struktur. Siden 2022 har Véronique Van Elewyck og jeg veiledet to postdoktorer sammen og arbeidet med å formalisere det inverse problemet for denne typen data. Vi vurderer hvor følsomme disse observasjonene er for jordens indre struktur.

Nøytrinoer dannes i atmosfæren når kosmisk stråling vekselvirker med atmosfæriske partikler, og trenger deretter inn i jorden. Vekselvirkningen deres med materie er ekstremt svak, men under forplantningen – nesten med lysets hastighet – kan de skifte smak gjennom en oscillasjonsmekanisme som er følsom for elektrontettheten langs banen. Siden hydrogen-1 praktisk talt er det eneste atomet uten nøytroner, kan slike observasjoner indirekte avgrense vanninnholdet i jordens indre, selv om den romlige oppløsningen er begrenset til skalaer over 1000 km.

Vi bruker koden EarthProb, en spesialisert versjon av programvaren OscProb, til å simulere smaksoscillasjonene. Jeg er i ferd med å integrere koden i modellerings- og inversjonsmiljøet `flexOPT.jl` for å kunne utforske mer fleksible inverse oppsett.

Dessuten bør det kommende Hyper-Kamiokande, et nøytrinoobservatorium av neste generasjon som etter planen settes i drift i Japan i 2027, forbedre oppløsningen og det detekterbare energiområdet betydelig. Det nye instrumentet kan grunnleggende endre vår evne til å utforske jordens indre med denne metoden.

{{< /collapse >}}

{{< collapse title="SeLFiE: Seismic and Lithological Filtering of Earth’s and planets’ models med flexOPT.jl" >}}

Hva om vi kunne avbilde jordens indre med en oppløsning på noen få centimeter? Ville det vært en endelig seier? Selv om vi klarer å avgrense den indre dynamikken bedre ved å invertere geofysiske data, er det å forstå utviklingen av den dype jorden et helt annet inverst problem – denne gangen med nesten ubegrenset mange parametere.

En av de store, langvarige debattene i geodynamikken gjelder opprinnelsen til LLVP-ene: er de rent termiske eller termokjemiske? Med andre ord: er mantelkonveksjonen rent termisk, eller spiller kjemien en vesentlig rolle? For å avgjøre slike spørsmål omformuleres det inverse problemet til et klassifiseringsproblem.

I denne sammenhengen blir det relevant å se direkte på observerte seismiske data sammenlignet med data predikert av geodynamiske modeller. Konkret innebærer det en modelleringskjede fra geodynamikk til bølgeformsimulering. Jeg har kalt prosessen *SeLFiE*: **Se**ismic and **L**ithological **Fi**ltering of **E**arth’s (and planets’) models. Ideen er å sammenligne seismiske signaler generert fra øyeblikksbilder av numeriske jordmodeller med signalene fra den virkelige jorden – som om vi tok en *selfie* av planetens indre.

Jeg har allerede flere samlinger av globale 2D- og 3D-modeller for termisk konveksjon, og har nylig lagt inn funksjoner for å lese dem i `flexOPT.jl`. Det gjør det mulig å visualisere termiske og kjemiske felt, inkludert vannsirkulasjon i mantelen og oppstigning av jern fra bunnen.

Deretter oversetter vi modellene til fysiske parametere som er relevante for seismisk bølgeutbredelse – tetthet, hastighetene `Vp` og `Vs`, anisotropi, demping – ut fra *in situ*-fasene, i samarbeid med petrologer. Omregningen tar hensyn til usikkerheter gjennom oppslagstabeller.

Fra modellene genererer vi syntetiske seismogrammer, og trekker ut bølgeformattributter (*features*) for klassifisering eller veiledet læring med kunstig intelligens. Kodene, tilgjengelige i Python, kan integreres i Julia-økosystemet.

{{< /collapse >}}

{{< collapse title="Fuji-fjellet – et nytt naturlig laboratorium" >}}

Framstilling av den tidsmessige koherensen mellom kontinuerlige data registrert på seks stasjoner rundt Fuji-fjellet i 2008, projisert med *UMAP*. Framstillingen viser den tidsmessige utviklingen av seismiske regimer og hjelper til å identifisere signaler knyttet til *Low Frequency Earthquakes* (LFE) og andre tektoniske hendelser.

Siden et M2-praksisopphold jeg veiledet sammen med Yosuke Aoki i 2022, har jeg vært interessert i strukturen og den seismiske aktiviteten til Fuji-fjellet. I motsetning til hva man kanskje skulle tro, får ikke Fuji den oppmerksomheten den fortjener. I Japan overvåkes over 100 aktive vulkaner på grunn av hyppige utbrudd, mens Fuji ikke har hatt utbrudd på mer enn 300 år. Denne inaktiviteten gjør den vanskeligere å studere for vulkanologer – men ikke for seismologer.

Med Léonard Seydoux og Jean-Philippe Métaxian har vi arbeidet med å utvikle en metode for overvåking av kontinuerlige seismiske data med maskinlæring, særlig med *UMAP*. Ved å definere koherensattributter mellom seks seismiske stasjoner rundt Fuji kunne vi automatisk klassifisere *Low Frequency Earthquakes* (LFE) og andre seismiske hendelser av tektonisk opprinnelse.

Etter denne første studien fikk jeg et CNRS-MITI-doktorgradsstipend for Hesaneh Mohammadi, veiledet av Stéphanie Durand og meg. Prosjektet gjelder seismisk 3D- og 4D-avbildning av Fuji-fjellet. Vi planlegger *boks-tomografi* ved svært høye frekvenser (> 2 Hz) for å avbilde de første 50 km under vulkanen. Her kan 1D-modeller eller standard tomografiske modeller ikke lenger brukes til å beregne bølgefeltene utenfor boksen. Jeg foreslår derfor å vurdere gyldigheten av planbølgetilnærmingen for isolerte ankomster som P- og S-bølger. Når det er gjort, vil vi forsøke å tilbakeforplante bølgeformene til LFE-ene som er identifisert på denne måten.

Parallelt er det startet et prosjekt med Béatrice Puyssegur og Manon Dalaison i Lorette Driques doktorgrad, som skal utvikle en verktøykasse for å redusere vegetasjonsrelaterte feil i InSAR-bilder. Selv om temaet ikke er direkte knyttet til Fuji, planlegger vi å bruke metodene i doktorgradens tredje år til å analysere mulige deformasjoner rundt vulkanen.

{{< /collapse >}}

{{< collapse title="Planetologi med seismologi: InSight / FSS" >}}

![SeLFiE planetologi](/images/optiSeLFiE_schema.jpg)

Utvidelse av *SeLFiE*-metodikken til planetologi, for å skille mellom scenarier for den termokjemiske utviklingen av Jorden, Mars og Månen ut fra numeriske modeller og attributter hentet ut med kunstig intelligens eller folkeforskning.

Jeg arbeider fortsatt av og til med Mars-data fra InSight i enkelte prosjekter. I prosjektet FSS (*FarSide Suite*) på Månen i 2026 blir jeg vitenskapelig og kunstnerisk samarbeidspartner.

Vi vil foreslå *SeLFiE*-filtreringen for tre terrestriske legemer. Vi samler 1D-, 2D- og 3D-scenarier for avkjøling av magmahavet og mantelkonveksjon for Jorden, Mars og Månen, basert på geofysiske, geokjemiske og petrologiske observasjoner. Deretter bygger vi – numerisk gjennom simuleringer av mantelkonveksjon, eller konseptuelt – modeller av dagens planeter, med særlig vekt på geometrien til delvis smeltede lag eller plumer ved mantelens bunn.

Vi omregner modellene til viskoelastiske parametere for å simulere seismiske bølger i ulike scenarier og beregner sensitivitetskjerner med `flexOPT.jl` som predikerer hvilke faser som er følsomme for strukturen ved mantelens bunn.

Vi sammenligner de syntetiske seismologiske dataene, som inneholder informasjon om mantelbunnen i de tre legemene, med observerte data. Det lar oss vurdere hvor relevante modellene er, og forfine forståelsen av disse dype strukturene.

Deretter klassifiserer vi dataene etter scenario med kunstig intelligens, for å maksimere evnen til å skille mellom ulike scenarier for mantelens dannelse.

Parallelt vil vi arrangere en formidlingsutstilling sentrert rundt lytting – formidlingskonserter og lytteøkter med syntetiske og observerte data – med utgangspunkt i psykologien bak kognitiv kontroll, og også for å berike forskningen med data samlet inn fra publikum.

{{< /collapse >}}
