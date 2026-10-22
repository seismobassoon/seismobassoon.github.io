+++
title = "Ricerca"
draft = false
+++

Dalla tomografia globale e regionale alla riconciliazione delle scale grazie ai vincoli mineralogici, petrologici e geodinamici, con la piattaforma unica `flexOPT.jl`

{{< collapse title="Introduzione generale" >}}

Il mio progetto di ricerca mira a vincolare meglio l’evoluzione dell’interno dei corpi tellurici a partire dall’analisi di dati (geo)fisici, in particolare delle forme d’onda sismiche.

Nel tempo ho sviluppato metodi numerici e teorici per l’inversione delle forme d’onda, che tengono conto delle proprietà elastiche e viscoelastiche dei mezzi a diverse scale, e li ho applicati a dati reali.

Uno dei miei contributi principali è lo sviluppo della cosiddetta *tomografia a scatola* (*box tomography*) a più scale, che permette di ottenere l’immagine di una regione localizzata (la «scatola») a partire da forme d’onda sismiche che campionano non solo l’interno di questa regione ma anche il suo ambiente esterno.

Presento innanzitutto i finanziamenti che hanno reso possibili le mie ricerche. Illustro poi una serie di lavori di imaging elastico e anelastico sulla micro-dinamica sotto la placca delle Caroline, svolti con geodinamici e petrologi. Formulo quindi alcune domande su metodi, risultati e interpretazioni. Descrivo poi la cassetta degli attrezzi teorici e numerici che ho sviluppato nel tempo per affrontare problemi scientifici diversi. Infine descrivo il progetto di ricerca che desidero portare avanti con i miei partner attuali e futuri.

![Schema della tomografia a scatola](/images/schema_box.png)

*
Alcuni esempi di applicazione della tomografia a scatola a diverse scale:
(a) in sismologia globale, uso di eventi telesismici per ottenere immagini di regioni localizzate;  
(b) sotto la placca delle Caroline, inversione delle forme d’onda 1D e 3D per `Vs` e `Qs`;  
(c) inversione 1D e 3D per `Vs` nella LLVP sotto le Hawaii;  
(d) apertura verso l’imaging con i neutrini;  
(e) vincoli sulla risalita di fusione parziale sotto La Réunion;  
(f) imaging 3D di `Vp`, `Vs` e densità sotto l’altopiano tibetano, recentemente esteso al Monte Fuji.
*
{{< /collapse >}}

{{< collapse title="Finanziamenti ottenuti" >}}

Due terzi del mio dottorato sono stati finanziati dalla JSPS (Società giapponese per la promozione della scienza). In Giappone, fino all’inizio degli anni 2010, i dottorandi non ricevevano sistematicamente un finanziamento. Ho quindi dovuto scrivere il mio progetto di ricerca, incentrato sullo sviluppo dell’inversione delle forme d’onda per l’elasticità e l’anelasticità, il che mi ha dato presto uno sguardo critico sulla scrittura di progetti scientifici.

Tra il 2012 e il 2017 sono stato collaboratore e principale responsabile della didattica nel consorzio GPX, dedicato alla geofisica di esplorazione. Il consorzio ha favorito ricerca e formazione, collegando università e industria. I miei lavori teorici sull’inversione localizzata delle forme d’onda e sullo sviluppo fondamentale del calcolo dei sismogrammi sintetici hanno posto le basi del mio nuovo metodo attuale: gli *operatori ottimali per equazioni alle derivate parziali arbitrarie*.

Ho poi contribuito agli studi preparatori del sismometro della missione InSight su Marte, che mi hanno portato alla prima determinazione dei meccanismi focali su Marte con i miei metodi di inversione.

Parallelamente ho ottenuto diversi finanziamenti per organizzare workshop internazionali, da cui sono nate collaborazioni durature. Grazie alla stretta collaborazione con Frédéric Deschamps (Academia Sinica), ho partecipato a vari progetti franco-taiwanesi, nei quali ho sviluppato la serie di studi di imaging sismo-petrologico descritta di seguito. Questa partnership mi ha permesso di seguire la mia prima dottoranda ufficiale, S.-T. Lai, nell’ambito del bando MOPGA (*Make Our Planet Great Again*).

Dal 2022 sono junior member dell’Institut universitaire de France (IUF) per la mediazione scientifica, il che mi permette di dedicare tempo sia alla ricerca sia alle attività di divulgazione per il grande pubblico.

Di recente ho ottenuto diversi finanziamenti di dottorato, in particolare sulla caratterizzazione del Monte Fuji. È inoltre nata una stretta collaborazione con Véronique Van Elewyck, con cui abbiamo ottenuto due borse postdoc sulla tomografia con i neutrini per l’imaging della Terra profonda a partire da osservabili geofisiche.

{{< /collapse >}}


{{< collapse title="Bilancio: micro-dinamica del mantello sotto la placca delle Caroline" >}}

![Schema della placca delle Caroline](/images/caro_schema.jpg)

Schema semplificato di una serie di studi tomografici sul mantello sotto la placca delle Caroline. Le nostre immagini tomografiche, unite a previsioni petrologiche, suggeriscono che un pennacchio mantellico profondo, a ridosso del bordo della LLVP del Pacifico/Hawaii, potrebbe trascinare ferro dal limite nucleo-mantello. Nella zona di transizione sovrastante si individua un pennacchio più superficiale, che alimenta la dorsale di Eauripik e potrebbe contribuire alla dinamica rapida della microplacca delle Caroline.

In questa sezione presento brevemente i miei studi basati sull’inversione delle forme d’onda sviluppata nel corso della mia carriera, limitandomi alla serie di studi tomografici del mantello superiore e inferiore sotto la placca delle Caroline. In alto, questa microplacca è circondata da grandi placche antiche, mentre alla base del mantello la regione corrisponde a una zona a bassa velocità delle onde di taglio (LLVP) sotto le Hawaii. Abbiamo ottenuto l’immagine di un piccolo pennacchio che sale dal fondo del mantello, probabilmente ricco di ferro, forse fino ad alimentare la dorsale della placca delle Caroline, spingendo la microplacca verso sud ad alta velocità, il che porta a un regime di subduzione di tipo *roll-over*.

### La placca delle Caroline

La placca delle Caroline presenta un contesto geodinamico particolarmente complesso: delimitata dalle placche australiana, filippina e pacifica, si trova in una zona di rapida convergenza, segnata da subduzioni attive e antiche, margini trasformi, rift abbandonati e un’attività vulcanica sostenuta. Una struttura maggiore, la dorsale di Eauripik, attraversa il centro della placca e costituisce una notevole anomalia topografica e magmatica, interpretata come antica dorsale morta oppure come traccia di un pennacchio profondo o di un punto caldo.

La geometria delle anomalie magnetiche, la batimetria e strutture come la fossa di Sorol o le fosse della Nuova Guinea testimoniano una dinamica ancora poco compresa, forse legata a una risalita mantellica profonda dal limite nucleo-mantello.

### Struttura profonda e pennacchio delle Caroline

Abbiamo condotto in questa regione una serie di studi di imaging sismico con il metodo di inversione delle forme d’onda che ho sviluppato durante il dottorato e il postdoc. Questo approccio permette di ottenere immagini ad alta risoluzione della velocità di taglio `Vs` e del fattore di qualità `Qs`, particolarmente sensibili ai contrasti termici. Usando i dati della rete giapponese F-net per terremoti profondi nelle regioni di Tonga e Figi, abbiamo evidenziato un’anomalia marcata e localizzata di `Vs` e `Qs`, centrata sotto il pennacchio delle Caroline.

L’interpretazione suggerisce un eccesso di temperatura localizzato di circa 100 K nella LLVP pacifica, oltre a un possibile contributo di materiale arricchito in ferro nel pennacchio, incompatibile con un modello puramente termico. L’analisi è stata estesa ad altre regioni del Pacifico per confermare il carattere localizzato di queste anomalie. La modellazione geodinamica e mineralogica indica una possibile interazione con il limite nucleo-mantello su diverse centinaia di chilometri di altezza.

### Struttura della zona di transizione e del mantello superiore

Infine, abbiamo condotto un’inversione Monte Carlo dei tempi di arrivo di più fasi per vincolare la struttura della zona di transizione del mantello sotto la placca delle Caroline. Il modello finale, basato su dataset SS e sulla modellazione delle forme d’onda, rivela una velocità di taglio anormalmente elevata in tutto il mantello superiore. Dopo diverse simulazioni geodinamiche, abbiamo concluso che il nostro modello sismico indica la possibilità di subduzioni di placca di tipo *roll-over* dal limite sud ed eventualmente anche da quello nord, oltre a anomalie di bassa velocità a forma di pennacchio che si estendono almeno fino a 800 km di profondità sotto la placca delle Caroline. Le simulazioni mostrano inoltre che la subduzione *roll-over* richiede una spinta della placca relativamente rapida.

{{< /collapse >}}

{{< collapse title="Domande aperte" >}}

Anche se questo approccio di imaging localizzato, la *tomografia a scatola*, ha permesso di chiarire alcune regioni cruciali per la comprensione della dinamica del mantello, molti punti restano da migliorare o chiarire, sia dal punto di vista scientifico sia tecnico.

Uno dei principali limiti di questa metodologia è che trascura le eterogeneità esterne alla scatola. Finora abbiamo usato solo modelli sferici 1D per simulare il campo d’onda, sia nel calcolo delle derivate parziali delle forme d’onda sia nella ricostruzione del campo d’onda ai bordi della scatola. Abbiamo valutato la propagazione degli errori dovuta a questa approssimazione in un quadro cartesiano, ma l’assenza di un trattamento rigoroso degli effetti esterni resta un limite importante da affrontare più seriamente in futuro. L’accoppiamento tra il metodo degli elementi spettrali e il mio metodo DSM, pur promettente, resta molto costoso. È anche per rispondere a questa sfida che ho intrapreso di recente una riorganizzazione completa della mia cassetta degli attrezzi numerici.

Inoltre, riguardo alla risalita del pennacchio delle Caroline, resta da ottenere l’immagine della porzione di mantello tra 800 e 2500 km di profondità, per verificare l’eventuale continuità della colonna del pennacchio dal limite nucleo-mantello alla superficie. A parte gli studi sulla base del pennacchio, non abbiamo ancora avuto occasione di interpretare quantitativamente i modelli tomografici ottenuti, espressi per ora solo in termini di parametri sismologici come `Vs` e `Qs`. È ormai essenziale collaborare con petrologi, geochimici e geodinamici per interpretare e valorizzare meglio le strutture rivelate dalla sismologia. In questa prospettiva propongo un approccio innovativo di filtraggio sismico, chiamato *SeLFiE*.

{{< /collapse >}}

{{< collapse title="Strumenti numerici e teorici" >}}

![Codici e flexOPT](/images/codes.jpg)

Stato dei miei codici fino al 2023 (a sinistra) e sviluppo recente di `flexOPT.jl` (a destra). La figura riassume l’evoluzione dei miei strumenti, dagli storici sviluppi in Fortran al meta-programma generico in Julia capace di derivare automaticamente operatori ottimali per EDP arbitrarie.

Ciò che distingue il mio approccio da quello di altri sismologi è che mi interesso alla dinamica del mantello e al ruolo dei processi chimici in essa, pur essendo anche sviluppatore di schemi numerici, sia per l’inversione sia per la modellazione diretta. Analizzo i dati e al tempo stesso progetto gli strumenti teorici e numerici per interpretarli.

Dal dottorato ho sviluppato numerosi codici basati sul Direct Solution Method (DSM) nel dominio della frequenza per pianeti sferici, e sulle differenze finite nel dominio del tempo con operatori modificati. Entrambi poggiano su una base teorica comune: gli operatori ottimali. Ho dedicato una parte importante del mio lavoro all’implementazione numerica di questa teoria, sviluppando codici specifici.

Gli operatori ottimali sono operatori compatti che raggiungono una precisione superiore a quella degli operatori convenzionali con lo stesso numero di punti nello spazio e nel tempo. Tuttavia il metodo generale per derivarli non era mai stato formulato in modo sistematico. Io stesso ho contribuito all’ottimizzazione degli operatori per gli elementi spettrali, senza immaginare che una ricetta generale fosse alla nostra portata.

La maggior parte di questi codici era scritta in Fortran e si è rivelata difficile da mantenere: un codice per ogni scopo specifico, con un debug lungo e faticoso. Ho quindi deciso di ripartire da zero per progettare un unico meta-programma capace di coprire molti casi d’uso. *Julia* si è imposto come scelta naturale, grazie alle sue capacità di meta-programmazione e di manipolazione simbolica e alla sua integrazione fluida con strumenti moderni come MPI o le GPU.

Lavorando a questo progetto con Thibault Duretz, che mi ha suggerito diverse equazioni di test e piste di ottimizzazione del codice, ho potuto formalizzare un metodo generale per derivare automaticamente operatori ottimali per equazioni alle derivate parziali arbitrarie. Un preprint che presenta questo approccio è stato sottomesso a *Computer Methods in Applied Mechanics and Engineering*.

Parallelamente a test e benchmark, il codice `flexOPT.jl` è già usato per risolvere diverse equazioni alle derivate parziali, in particolare dalla mia dottoranda Hesaneh Mohammadi in un progetto di tomografia del Monte Fuji, dove è confrontato con altri codici di riferimento.

{{< /collapse >}}

{{< collapse title="Progetto di ricerca: visione d’insieme" >}}

![Strategia tomografia–geodinamica–SeLFiE](/images/tomo_projet.jpg)

Schema dei progetti di ricerca che desidero condurre.  
A sinistra: miglioramento della tomografia delle forme d’onda, dalla scala globale a quella locale, tenendo conto degli effetti esterni alla scatola.  
Al centro: interpretazione litologica e filtraggio sismologico con l’approccio *SeLFiE*.  
A destra: modellazione della convezione del mantello e generazione di Terre virtuali di cui calcolare le osservabili sismiche e neutriniche.

Come accennato, diversi progetti si inseriscono naturalmente nella continuità delle mie ricerche. Ora che il mio progetto di modernizzazione e democratizzazione degli operatori ottimali giunge a maturità, è il momento di mobilitare pienamente questi risultati per rivisitare dati sismologici, ma anche altri tipi di dati, per rispondere ad alcune delle grandi domande delle geoscienze: come si sono evoluti i pianeti dalla formazione del Sistema solare e come evolveranno in futuro? Che cosa rende il nostro pianeta così unico tra i suoi vicini?

{{< /collapse >}}

{{< collapse title="Tomografia delle forme d’onda, tra scala locale e scala globale" >}}

La *tomografia a scatola* si basa sull’ipotesi che il campo d’onda incidente possa essere stimato con precisione sufficiente, a partire da un modello 1D di riferimento della Terra oppure supponendo che le onde incidenti si comportino come onde piane. Questa approssimazione è ragionevolmente valida per alcune prime onde di volume isolate, come le onde P dirette, PKP o S. Diventa però insufficiente ad alta frequenza, dove la coerenza del campo d’onda globale non può più essere garantita.

Per superare questo limite propongo di usare diversi modelli tomografici più realistici, come SEISGLOB2, che rappresentano più fedelmente la propagazione delle onde complesse, soprattutto nelle regioni in cui l’eterogeneità del mantello influenza fortemente le fasi osservate. Per vincolare meglio le incertezze userò più modelli ricavati da osservabili diverse, come le onde di superficie o i tempi di arrivo delle onde di volume.

Aggiornerò così il mio metodo di tomografia a scatola tenendo conto delle eterogeneità oltre la regione di interesse. Test sintetici sono già stati condotti in un quadro cartesiano, ma l’applicazione in sismologia globale sarà una prima assoluta. Questa nuova versione richiede solutori capaci di modellare mezzi 3D in due domini annidati (globale e locale), il che ha motivato lo sviluppo di `flexOPT.jl`.

In particolare esplorerò fasi che permettano di ottenere l’immagine della regione dalla base del mantello fino alla superficie della placca delle Caroline, per `Vs`, `Qs`, `Vp`, `Qp` e, in un secondo tempo, l’anisotropia. Ciò contribuirà a comprendere la dinamica del pennacchio di cui ho ottenuto l’immagine, dalla base del mantello al mantello superiore. La regione sotto la microplacca delle Caroline potrebbe offrire uno scenario mai osservato, esotico dal punto di vista geodinamico, al bordo della LLVP hawaiana.

Prevedo inoltre di applicare il metodo ad altre regioni geodinamicamente attive, in particolare il mantello superiore e la zona di transizione sotto il Giappone, La Réunion e l’altopiano tibetano.

Usando i modelli globali per affinare l’immagine locale nelle scatole, potremo far progredire passo dopo passo la risoluzione della Terra profonda. È però noto che l’inversione delle forme d’onda soffre più della non unicità e della non linearità rispetto all’inversione di attributi secondari come la dispersione delle onde di superficie o i tempi di arrivo. È quindi cruciale partire da modelli iniziali realistici. Proseguirò inoltre l’interpretazione dei modelli tomografici con i petrologi, per tradurli in parametri fisico-chimici più pertinenti per vincolare la dinamica del mantello.

{{< /collapse >}}

{{< collapse title="Tomografia delle oscillazioni dei neutrini" >}}

Di recente i fisici delle alte energie hanno iniziato a interessarsi all’uso delle oscillazioni dei neutrini che attraversano l’interno della Terra per ottenerne l’immagine. Dal 2022, con Véronique Van Elewyck, co-supervisioniamo due postdoc e lavoriamo alla formalizzazione del problema inverso per questo tipo di dati, valutando la sensibilità di queste osservazioni alla struttura interna della Terra.

I neutrini sono prodotti nell’atmosfera dall’interazione dei raggi cosmici con le particelle atmosferiche e poi attraversano la Terra. La loro interazione con la materia è estremamente debole, ma durante la propagazione, a velocità prossima a quella della luce, possono cambiare sapore tramite un meccanismo di oscillazione sensibile alla densità elettronica lungo il percorso. Poiché l’idrogeno-1 è praticamente l’unico atomo privo di neutroni, queste osservazioni potrebbero vincolare indirettamente il contenuto d’acqua dell’interno della Terra, anche se la risoluzione spaziale resta limitata a scale superiori a 1000 km.

Usiamo il codice EarthProb, versione specializzata del software OscProb, per simulare queste oscillazioni di sapore. Sto integrando il codice nell’ambiente di modellazione e inversione `flexOPT.jl`, per poter esplorare configurazioni inverse più flessibili.

Inoltre, l’arrivo di Hyper-Kamiokande, osservatorio di neutrini di nuova generazione la cui entrata in funzione è prevista in Giappone nel 2027, dovrebbe migliorare notevolmente la risoluzione e l’intervallo di energie rilevabili. Questo nuovo strumento potrebbe trasformare profondamente la nostra capacità di sondare l’interno della Terra con questo metodo.

{{< /collapse >}}

{{< collapse title="SeLFiE: Seismic and Lithological Filtering of Earth’s and planets’ models con flexOPT.jl" >}}

Che cosa accadrebbe se riuscissimo a ottenere immagini dell’interno della Terra con una risoluzione di pochi centimetri? Sarebbe una vittoria definitiva? Anche se riuscissimo a vincolare meglio la dinamica interna con l’inversione dei dati geofisici, comprendere l’evoluzione della Terra profonda è tutto un altro problema inverso, questa volta con parametri quasi illimitati.

Uno dei grandi dibattiti persistenti in geodinamica riguarda l’origine delle LLVP: sono di origine puramente termica o termochimica? In altre parole, la convezione del mantello è solo termica, o la chimica vi gioca un ruolo essenziale? Per dirimere questo tipo di questioni, il problema inverso si riformula come un problema di classificazione.

In questo contesto diventa pertinente esaminare direttamente i dati sismici osservati, confrontandoli con quelli previsti dai modelli geodinamici. Concretamente, ciò implica una modellazione a catena dalla geodinamica alla simulazione delle forme d’onda. Ho chiamato questo processo *SeLFiE*: **Se**ismic and **L**ithological **Fi**ltering of **E**arth’s (and planets’) models. Si tratta di confrontare i segnali sismici generati da istantanee di modelli numerici della Terra con quelli della Terra reale, come se facessimo un *selfie* dell’interno del nostro pianeta.

Dispongo già di diverse collezioni di modelli globali di convezione termica 2D e 3D, e di recente ho integrato in `flexOPT.jl` funzioni per leggerli. Ciò permette di visualizzare i campi termici e chimici, inclusa la circolazione dell’acqua nel mantello o la risalita del ferro dalla sua base.

Traduciamo poi questi modelli in parametri fisici pertinenti per la propagazione delle onde sismiche — densità, velocità `Vp` e `Vs`, anisotropia, attenuazione — a partire dalle fasi *in situ*, in collaborazione con i petrologi. Questa conversione tiene conto delle incertezze tramite tabelle di corrispondenza (*look-up tables*).

Da questi modelli generiamo sismogrammi sintetici, da cui estraiamo attributi (*features*) delle forme d’onda per una classificazione o un apprendimento supervisionato con l’intelligenza artificiale. I codici, disponibili in Python, potranno essere integrati nell’ecosistema Julia.

{{< /collapse >}}

{{< collapse title="Monte Fuji – un nuovo laboratorio naturale" >}}

Rappresentazione delle coerenze temporali tra dati continui registrati in sei stazioni intorno al Monte Fuji durante il 2008, proiettate con *UMAP*. Questa rappresentazione permette di visualizzare l’evoluzione temporale dei regimi sismici e di individuare segnali associati ai *Low Frequency Earthquakes* (LFE) e ad altri eventi tettonici.

Da un tirocinio di M2 che ho co-supervisionato con Yosuke Aoki nel 2022, mi interesso alla struttura e all’attività sismica del Monte Fuji. Contrariamente a quanto si potrebbe pensare, il Monte Fuji non riceve l’attenzione che merita. In Giappone oltre 100 vulcani attivi sono sorvegliati per le loro frequenti eruzioni, mentre il Fuji non erutta da più di 300 anni. Questa inattività ne rende lo studio più difficile per i vulcanologi — ma non per i sismologi.

Con Léonard Seydoux e Jean-Philippe Métaxian abbiamo lavorato allo sviluppo di un metodo di monitoraggio dei dati sismici continui con l’apprendimento automatico, in particolare con *UMAP*. Definendo attributi di coerenza tra sei stazioni sismiche intorno al Fuji, siamo riusciti a classificare automaticamente i *Low Frequency Earthquakes* (LFE) e altri eventi sismici di origine tettonica.

Dopo questo primo studio ho ottenuto una borsa di dottorato CNRS-MITI per Hesaneh Mohammadi, co-supervisionata da Stéphanie Durand e da me. Il progetto riguarda l’imaging sismologico 3D e 4D del Monte Fuji. Prevediamo una *tomografia a scatola* ad altissima frequenza (> 2 Hz) per ottenere l’immagine dei primi 50 km sotto il vulcano. In questo caso i modelli 1D o tomografici standard non sono più utilizzabili per calcolare i campi d’onda esterni alla scatola. Propongo quindi di valutare la validità dell’approssimazione di onda piana per arrivi isolati come le onde P e S. Superata questa tappa, cercheremo di retro-propagare le forme d’onda associate agli LFE così identificati.

Parallelamente è stato avviato un progetto con Béatrice Puyssegur e Manon Dalaison nell’ambito del dottorato di Lorette Drique, che mira a sviluppare strumenti per attenuare gli errori delle immagini InSAR dovuti alla vegetazione. Anche se il tema non è direttamente legato al Fuji, prevediamo di applicare questi metodi durante il terzo anno di dottorato per analizzare eventuali deformazioni della regione intorno al vulcano.

{{< /collapse >}}

{{< collapse title="Planetologia con la sismologia: InSight / FSS" >}}

![SeLFiE planetologia](/images/optiSeLFiE_schema.jpg)

Estensione della metodologia *SeLFiE* alla planetologia, per distinguere scenari di evoluzione termochimica della Terra, di Marte e della Luna a partire da modelli numerici e da attributi estratti con l’intelligenza artificiale o la scienza partecipativa.

Continuo a lavorare occasionalmente sui dati marziani di InSight per alcuni progetti. Per il progetto FSS (*FarSide Suite*) sulla Luna nel 2026 sarò collaboratore scientifico e artistico.

Proporremo il metodo di filtraggio *SeLFiE* per tre corpi tellurici. Raccoglieremo scenari 1D, 2D e 3D di raffreddamento dell’oceano di magma e di convezione del mantello per la Terra, Marte e la Luna, basati su osservazioni geofisiche, geochimiche e petrologiche. Costruiremo poi, numericamente tramite simulazioni di convezione o concettualmente, modelli planetari attuali, con particolare attenzione alla geometria degli strati parzialmente fusi o dei pennacchi alla base del mantello.

Convertiremo questi modelli in parametri viscoelastici per simulare le onde sismiche nei diversi scenari e calcolare con `flexOPT.jl` kernel di sensibilità che prevedano le fasi sensibili alla struttura della base del mantello.

Confronteremo i dati sismologici sintetici, che contengono informazioni sulla base del mantello dei tre corpi tellurici, con i dati osservati. Ciò ci permetterà di valutare la pertinenza dei modelli proposti e di affinare la nostra comprensione di queste strutture profonde.

Classificheremo poi i dati secondo gli scenari con l’intelligenza artificiale, massimizzando la capacità di distinguere i diversi scenari di formazione del mantello.

Parallelamente organizzeremo una mostra di divulgazione scientifica incentrata sull’ascolto dei suoni — concerti divulgativi e sessioni di ascolto di dati sintetici e osservati — sfruttando la psicologia del controllo cognitivo, anche per arricchire la nostra ricerca con i dati raccolti dal grande pubblico.

{{< /collapse >}}
