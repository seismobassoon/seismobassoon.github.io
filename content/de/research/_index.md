+++
title = "Forschung"
draft = false
+++

Von der globalen und regionalen Tomographie zur Versöhnung der Skalen mithilfe mineralogischer, petrologischer und geodynamischer Randbedingungen – mit der einheitlichen Plattform `flexOPT.jl`

{{< collapse title="Allgemeine Einführung" >}}

Ziel meiner Forschung ist es, die Entwicklung des Inneren tellurischer Körper anhand (geo)physikalischer Daten, insbesondere seismischer Wellenformen, besser einzugrenzen.

Im Laufe der Jahre habe ich numerische und theoretische Methoden der Wellenforminversion entwickelt, die elastische und viskoelastische Eigenschaften der Medien auf verschiedenen Skalen berücksichtigen, und sie auf reale Daten angewandt.

Einer meiner wichtigsten Beiträge ist die Entwicklung der sogenannten *Box-Tomographie* auf mehreren Skalen. Sie bildet eine lokalisierte Region (die „Box“) aus seismischen Wellenformen ab, die nicht nur das Innere dieser Region, sondern auch ihre Umgebung durchlaufen haben.

Zunächst stelle ich die Finanzierungen vor, die meine Forschung ermöglicht haben. Dann zeige ich eine Reihe elastischer und anelastischer Bildgebungsstudien zur Mikrodynamik unter der Karolinenplatte, durchgeführt mit Geodynamikern und Petrologen. Anschließend formuliere ich offene Fragen zu Methoden, Ergebnissen und Interpretationen. Danach beschreibe ich den theoretischen und numerischen Werkzeugkasten, den ich im Laufe der Zeit für verschiedene wissenschaftliche Fragestellungen aufgebaut habe. Zum Schluss stelle ich das Forschungsprojekt vor, das ich mit meinen heutigen und künftigen Partnern verfolgen möchte.

![Schema Box-Tomographie](/images/schema_box.png)

*
Beispiele für Anwendungen der Box-Tomographie auf verschiedenen Skalen:
(a) in der globalen Seismologie werden teleseismische Beben genutzt, um lokalisierte Regionen abzubilden;  
(b) unter der Karolinenplatte: 1D- und 3D-Wellenforminversion für `Vs` und `Qs`;  
(c) 1D- und 3D-Inversion für `Vs` in der LLVP unter Hawaii;  
(d) Ausblick auf die Neutrino-Bildgebung;  
(e) Randbedingungen für den Aufstieg partieller Schmelze unter La Réunion;  
(f) 3D-Bildgebung von `Vp`, `Vs` und Dichte unter dem Tibet-Plateau, kürzlich erweitert auf den Fuji.
*
{{< /collapse >}}

{{< collapse title="Finanzierung" >}}

Zwei Drittel meiner Promotion wurden von der JSPS (Japan Society for the Promotion of Science) finanziert. In Japan erhielten Doktoranden bis Anfang der 2010er-Jahre nicht systematisch eine Finanzierung. Ich musste daher meinen eigenen Forschungsantrag schreiben, mit dem Schwerpunkt auf der Entwicklung der Wellenforminversion für Elastizität und Anelastizität – so gewann ich früh einen kritischen Blick auf das Verfassen wissenschaftlicher Anträge.

Von 2012 bis 2017 war ich Mitarbeiter und Hauptverantwortlicher für die Lehre im GPX-Konsortium für Explorationsgeophysik. Dieses Konsortium förderte Forschung und Ausbildung an der Schnittstelle von Universitäten und Industrie. Meine theoretischen Arbeiten zur lokalisierten Wellenforminversion und zu den Grundlagen der Berechnung synthetischer Seismogramme legten den Grundstein für meine heutige neue Methode: *optimale Operatoren für beliebige partielle Differentialgleichungen*.

Danach wirkte ich an den Vorstudien zum Seismometer der Mars-Mission InSight mit, was mich zur ersten Bestimmung von Herdmechanismen auf dem Mars mit meinen Inversionsmethoden führte.

Parallel dazu erhielt ich mehrere Förderungen für internationale Workshops, aus denen dauerhafte Kooperationen entstanden. Dank meiner engen Zusammenarbeit mit Frédéric Deschamps (Academia Sinica) war ich an mehreren französisch-taiwanischen Projekten beteiligt, in denen ich die unten beschriebene Reihe seismo-petrologischer Bildgebungsstudien entwickelte. Diese Partnerschaft ermöglichte es mir, im Rahmen der Ausschreibung MOPGA (*Make Our Planet Great Again*) meine erste offizielle Doktorandin, S.-T. Lai, zu betreuen.

Seit 2022 bin ich Junior-Mitglied des Institut universitaire de France (IUF) für Wissenschaftskommunikation, was mir Zeit sowohl für meine Forschung als auch für Vermittlungsarbeit mit der Öffentlichkeit gibt.

Kürzlich habe ich mehrere Promotionsfinanzierungen erhalten, insbesondere zur Charakterisierung des Fuji. Außerdem ist eine enge Zusammenarbeit mit Véronique Van Elewyck entstanden, mit der wir zwei Postdoc-Stellen zur Neutrino-Tomographie für die Abbildung der tiefen Erde aus geophysikalischen Observablen eingeworben haben.

{{< /collapse >}}


{{< collapse title="Bilanz: Mikrodynamik des Mantels unter der Karolinenplatte" >}}

![Schema Karolinenplatte](/images/caro_schema.jpg)

Vereinfachtes Schema einer Reihe tomographischer Studien des Mantels unter der Karolinenplatte. Unsere tomographischen Bilder, kombiniert mit petrologischen Vorhersagen, deuten darauf hin, dass ein tiefer Mantelplume in unmittelbarer Nähe des Randes der pazifischen/hawaiianischen LLVP Eisen von der Kern-Mantel-Grenze mitführen könnte. In der darüberliegenden Übergangszone erkennt man einen flacheren Plume, der den Eauripik-Rücken speist und zur schnellen Dynamik der Karolinen-Mikroplatte beitragen könnte.

In diesem Abschnitt stelle ich kurz meine Studien vor, die auf der von mir im Laufe meiner Laufbahn entwickelten Wellenforminversion beruhen, und beschränke mich auf die tomographischen Studien des oberen und unteren Mantels unter der Karolinenplatte. Oben ist diese Mikroplatte von großen alten Platten umgeben, während die Region am Boden des Mantels einer Zone niedriger Scherwellengeschwindigkeit (LLVP) unter Hawaii entspricht. Wir haben einen kleinen, wahrscheinlich eisenreichen Plume abgebildet, der vom Boden des Mantels aufsteigt, möglicherweise bis zur Speisung des Rückens der Karolinenplatte, und die Mikroplatte mit hoher Geschwindigkeit nach Süden schiebt, was zu einem *roll-over*-Subduktionsregime führt.

### Die Karolinenplatte

Die Karolinenplatte hat einen besonders komplexen geodynamischen Kontext: begrenzt von der Australischen, Philippinischen und Pazifischen Platte, liegt sie in einer Zone schneller Konvergenz mit aktiven und alten Subduktionen, Transformrändern, aufgegebenen Riften und anhaltendem Vulkanismus. Eine Hauptstruktur, der Eauripik-Rücken, durchzieht die Plattenmitte und bildet eine bedeutende topographische und magmatische Anomalie, die entweder als alter toter Rücken oder als Spur eines tiefen Plumes bzw. Hotspots gedeutet wird.

Die Geometrie der magnetischen Anomalien, die Bathymetrie und Strukturen wie der Sorol-Graben oder die Neuguinea-Gräben zeugen von einer noch kaum verstandenen Dynamik, die möglicherweise mit einem tiefen Mantelaufstieg an der Kern-Mantel-Grenze zusammenhängt.

### Tiefe Struktur und der Karolinen-Plume

Wir haben in dieser Region eine Reihe seismischer Bildgebungsstudien mit der Wellenforminversionsmethode durchgeführt, die ich während meiner Promotion und meines Postdocs entwickelt habe. Dieser Ansatz bildet die Scherwellengeschwindigkeit `Vs` und den Qualitätsfaktor `Qs`, die besonders empfindlich auf thermische Kontraste reagieren, hochaufgelöst ab. Mit Daten des japanischen F-net-Netzes für tiefe Beben in den Regionen Tonga und Fidschi haben wir eine ausgeprägte, lokalisierte Anomalie von `Vs` und `Qs` unter dem Karolinen-Plume nachgewiesen.

Die Interpretation deutet auf einen lokalen Temperaturüberschuss von etwa 100 K in der pazifischen LLVP sowie auf einen möglichen Beitrag eisenreichen Materials im Plume hin, der mit einem rein thermischen Modell unvereinbar ist. Die Analyse wurde auf andere Regionen des Pazifiks ausgedehnt, um den lokalen Charakter dieser Anomalien zu bestätigen. Geodynamische und mineralogische Modellierungen deuten auf eine mögliche Wechselwirkung mit der Kern-Mantel-Grenze über mehrere hundert Kilometer Höhe hin.

### Struktur der Übergangszone und des oberen Mantels

Schließlich führten wir eine Monte-Carlo-Inversion der Laufzeiten mehrerer Phasen durch, um die Struktur der Mantelübergangszone unter der Karolinenplatte einzugrenzen. Das endgültige Modell, basierend auf SS-Datensätzen und Wellenformmodellierung, zeigt eine anomal hohe Scherwellengeschwindigkeit im gesamten oberen Mantel. Nach mehreren geodynamischen Simulationen kamen wir zu dem Schluss, dass unser seismisches Modell auf mögliche *roll-over*-Subduktion vom südlichen und eventuell auch vom nördlichen Rand hinweist sowie auf plumeförmige Niedriggeschwindigkeitsanomalien bis mindestens 800 km Tiefe unter der Karolinenplatte. Unsere Simulationen zeigen außerdem, dass die *roll-over*-Subduktion einen relativ schnellen Plattenschub erfordert.

{{< /collapse >}}

{{< collapse title="Offene Fragen" >}}

Auch wenn dieser lokalisierte Bildgebungsansatz, die *Box-Tomographie*, einige für das Verständnis der Manteldynamik entscheidende Regionen beleuchtet hat, bleiben wissenschaftlich wie technisch viele Punkte zu verbessern oder zu klären.

Eine der Haupthürden dieser Methodik ist die Vernachlässigung der Heterogenitäten außerhalb der Box. Bisher haben wir nur sphärische 1D-Modelle zur Simulation des Wellenfelds verwendet – sowohl für die partiellen Ableitungen der Wellenformen als auch für die Rekonstruktion des Wellenfelds an den Boxrändern. Wir haben die Fehlerfortpflanzung dieser Näherung in einem kartesischen Rahmen abgeschätzt, doch das Fehlen einer rigorosen Behandlung äußerer Effekte bleibt eine wichtige Einschränkung, die künftig ernsthafter angegangen werden muss. Die Kopplung der Spektralelementmethode mit meiner DSM-Methode ist zwar vielversprechend, aber sehr ressourcenintensiv. Auch deshalb habe ich kürzlich eine vollständige Neuorganisation meines numerischen Werkzeugkastens begonnen.

Was den Aufstieg des Karolinen-Mantelplumes betrifft, bleibt der Mantelabschnitt zwischen 800 und 2500 km Tiefe noch abzubilden, um die mögliche Kontinuität der Plume-Säule von der Kern-Mantel-Grenze bis zur Oberfläche zu prüfen. Abgesehen von unseren Studien zur Basis des Plumes hatten wir noch keine Gelegenheit, die tomographischen Modelle quantitativ zu interpretieren; sie liegen bisher nur in seismologischen Parametern wie `Vs` und `Qs` vor. Es ist nun entscheidend, mit Petrologen, Geochemikern und Geodynamikern zusammenzuarbeiten, um die von der Seismologie aufgedeckten Strukturen besser zu interpretieren und zu nutzen. Dafür schlage ich einen innovativen seismischen Filteransatz namens *SeLFiE* vor.

{{< /collapse >}}

{{< collapse title="Numerische und theoretische Werkzeuge" >}}

![Codes und flexOPT](/images/codes.jpg)

Stand meiner Codes bis 2023 (links) und jüngste Entwicklung von `flexOPT.jl` (rechts). Die Abbildung fasst die Entwicklung meiner Werkzeuge zusammen – von den historischen Fortran-Codes bis zum generischen Julia-Metaprogramm, das automatisch optimale Operatoren für beliebige PDGL herleitet.

Was meinen Ansatz von dem anderer Seismologen unterscheidet: Ich interessiere mich für die Manteldynamik und die Rolle chemischer Prozesse darin und entwickle zugleich numerische Verfahren, sowohl für die Inversion als auch für die Vorwärtsmodellierung. Ich analysiere Daten und entwerfe gleichzeitig die theoretischen und numerischen Werkzeuge zu ihrer Interpretation.

Seit meiner Promotion habe ich zahlreiche Codes auf Basis der Direct Solution Method (DSM) im Frequenzbereich für sphärische Planeten sowie Finite-Differenzen-Codes im Zeitbereich mit modifizierten Operatoren entwickelt. Beide Ansätze beruhen auf einer gemeinsamen theoretischen Grundlage: den optimalen Operatoren. Einen großen Teil meiner Arbeit habe ich der numerischen Umsetzung dieser Theorie in eigenen Codes gewidmet.

Optimale Operatoren sind kompakte Operatoren, die mit derselben Anzahl von Raum- und Zeitpunkten eine höhere Genauigkeit erreichen als konventionelle Operatoren. Eine allgemeine Methode zu ihrer Herleitung war jedoch nie systematisch formuliert worden. Ich selbst habe zur Optimierung von Operatoren für Spektralelemente beigetragen, ohne mir vorzustellen, dass ein allgemeines Rezept erreichbar wäre.

Die meisten dieser Codes waren in Fortran geschrieben und schwer zu pflegen: ein Code pro Zweck, mit langem, mühsamem Debugging. Deshalb habe ich kürzlich beschlossen, bei null anzufangen und ein einziges Metaprogramm für viele Anwendungsfälle zu entwerfen. *Julia* war dank seiner Metaprogrammierung, symbolischen Fähigkeiten und guten Integration moderner Werkzeuge wie MPI oder GPUs die naheliegende Wahl.

In der Zusammenarbeit mit Thibault Duretz, der mehrere Testgleichungen und Optimierungsideen vorschlug, konnte ich eine allgemeine Methode formalisieren, um optimale Operatoren für beliebige partielle Differentialgleichungen automatisch herzuleiten. Ein Preprint dazu wurde bei *Computer Methods in Applied Mechanics and Engineering* eingereicht.

Neben Tests und Benchmarks wird `flexOPT.jl` bereits zur Lösung verschiedener partieller Differentialgleichungen eingesetzt, insbesondere von meiner Doktorandin Hesaneh Mohammadi in einem Tomographieprojekt zum Fuji, wo es mit anderen Referenzcodes verglichen wird.

{{< /collapse >}}

{{< collapse title="Forschungsprojekt: Gesamtüberblick" >}}

![Strategie Tomographie–Geodynamik–SeLFiE](/images/tomo_projet.jpg)

Schema der Forschungsprojekte, die ich durchführen möchte.  
Links: Verbesserung der Wellenformtomographie von der globalen bis zur lokalen Skala unter Berücksichtigung der Effekte außerhalb der Box.  
Mitte: lithologische Interpretation und seismologische Filterung mit dem *SeLFiE*-Ansatz.  
Rechts: Modellierung der Mantelkonvektion und Erzeugung virtueller Erden, deren seismische und Neutrino-Observablen berechnet werden können.

Wie oben erwähnt, schließen sich mehrere Projekte ganz natürlich an meine Forschung an. Da mein Projekt zur Modernisierung und Demokratisierung der optimalen Operatoren nun ausgereift ist, ist es an der Zeit, diese Errungenschaften voll einzusetzen, um seismologische und andere Daten neu zu betrachten und einige der großen Fragen der Geowissenschaften anzugehen: Wie haben sich die Planeten seit der Entstehung des Sonnensystems entwickelt, und wie werden sie sich künftig entwickeln? Was macht unseren Planeten unter seinen Nachbarn so einzigartig?

{{< /collapse >}}

{{< collapse title="Wellenformtomographie zwischen lokaler und globaler Skala" >}}

Die *Box-Tomographie* beruht auf der Annahme, dass das einfallende Wellenfeld hinreichend genau geschätzt werden kann – entweder aus einem 1D-Referenzmodell der Erde oder unter der Annahme ebener Wellen. Diese Näherung gilt recht gut für einige isolierte Ersteinsätze von Raumwellen wie direkte P-, PKP- oder S-Wellen. Bei hohen Frequenzen reicht sie jedoch nicht mehr aus, da die Kohärenz des globalen Wellenfelds nicht mehr gewährleistet ist.

Um diese Einschränkung zu überwinden, schlage ich vor, mehrere realistischere tomographische Modelle wie SEISGLOB2 zu verwenden, die die Ausbreitung komplexer Wellen besser abbilden, insbesondere in Regionen, in denen die Mantelheterogenität die beobachteten Phasen stark beeinflusst. Um die Unsicherheiten besser einzugrenzen, werde ich mehrere Modelle aus unterschiedlichen Observablen wie Oberflächenwellen oder Raumwellenlaufzeiten nutzen.

So werde ich meine Box-Tomographie aktualisieren und die Heterogenitäten jenseits der Zielregion berücksichtigen. Synthetische Tests wurden bereits in einem kartesischen Rahmen durchgeführt; die Anwendung in der globalen Seismologie wird eine Premiere sein. Diese neue Version erfordert Löser, die 3D-Medien in zwei verschachtelten Domänen (global und lokal) modellieren können – das war die Motivation für die Entwicklung von `flexOPT.jl`.

Insbesondere werde ich Phasen untersuchen, die die Region von der Mantelbasis bis zur Oberfläche der Karolinenplatte abbilden, für `Vs`, `Qs`, `Vp`, `Qp` und in einem zweiten Schritt die Anisotropie. Das wird helfen, die Dynamik des von mir abgebildeten Plumes von der Mantelbasis bis zum oberen Mantel zu verstehen. Die Region unter der Karolinen-Mikroplatte könnte eine nie beobachtete, geodynamisch exotische Situation am Rand der hawaiianischen LLVP bieten.

Ich plane außerdem, die Methode auf andere geodynamisch aktive Regionen anzuwenden, insbesondere den oberen Mantel und die Übergangszone unter Japan, La Réunion und dem Tibet-Plateau.

Indem wir globale Modelle nutzen, um das lokale Bild in den Boxen zu verfeinern, können wir die Auflösung der tiefen Erde Schritt für Schritt verbessern. Bekanntlich leidet die Wellenforminversion jedoch stärker unter Nicht-Eindeutigkeit und Nichtlinearität als die Inversion sekundärer Attribute wie Oberflächenwellendispersion oder Laufzeiten. Es ist daher entscheidend, von realistischen Startmodellen auszugehen. Außerdem werde ich die Interpretation tomographischer Modelle mit Petrologen fortsetzen, um sie in physikalisch-chemische Parameter zu übersetzen, die für die Manteldynamik aussagekräftiger sind.

{{< /collapse >}}

{{< collapse title="Tomographie mit Neutrinooszillationen" >}}

Seit Kurzem interessieren sich Hochenergiephysiker dafür, die Oszillationen von Neutrinos, die das Erdinnere durchqueren, zur Abbildung seiner Struktur zu nutzen. Seit 2022 betreuen Véronique Van Elewyck und ich gemeinsam zwei Postdocs und arbeiten an der Formalisierung des inversen Problems für diese Art von Daten. Wir untersuchen die Empfindlichkeit dieser Beobachtungen gegenüber der inneren Struktur der Erde.

Neutrinos entstehen in der Atmosphäre durch die Wechselwirkung kosmischer Strahlung mit atmosphärischen Teilchen und durchdringen dann die Erde. Ihre Wechselwirkung mit Materie ist extrem schwach, doch während ihrer Ausbreitung nahezu mit Lichtgeschwindigkeit können sie über einen Oszillationsmechanismus, der von der Elektronendichte entlang des Weges abhängt, ihren Flavour wechseln. Da Wasserstoff-1 praktisch das einzige Atom ohne Neutronen ist, könnten diese Beobachtungen indirekt den Wassergehalt des Erdinneren eingrenzen, auch wenn die räumliche Auflösung auf Skalen über 1000 km begrenzt bleibt.

Wir verwenden den Code EarthProb, eine spezialisierte Version der Software OscProb, um diese Flavour-Oszillationen zu simulieren. Ich integriere diesen Code derzeit in die Modellierungs- und Inversionsumgebung `flexOPT.jl`, um flexiblere inverse Konfigurationen zu untersuchen.

Zudem dürfte das künftige Hyper-Kamiokande, ein Neutrino-Observatorium der nächsten Generation, das 2027 in Japan in Betrieb gehen soll, die Auflösung und den nachweisbaren Energiebereich erheblich verbessern. Dieses neue Instrument könnte unsere Fähigkeit, das Erdinnere mit dieser Methode zu erkunden, grundlegend verändern.

{{< /collapse >}}

{{< collapse title="SeLFiE: Seismic and Lithological Filtering of Earth’s and planets’ models mit flexOPT.jl" >}}

Was wäre, wenn wir das Erdinnere mit einer Auflösung von wenigen Zentimetern abbilden könnten? Wäre das ein endgültiger Sieg? Selbst wenn es gelingt, die innere Dynamik durch Inversion geophysikalischer Daten besser einzugrenzen, ist das Verständnis der Entwicklung der tiefen Erde ein ganz anderes inverses Problem – diesmal mit nahezu unbegrenzt vielen Parametern.

Eine der großen anhaltenden Debatten der Geodynamik betrifft den Ursprung der LLVPs: Sind sie rein thermisch oder thermochemisch? Anders gesagt: Ist die Mantelkonvektion rein thermisch, oder spielt die Chemie eine wesentliche Rolle? Um solche Fragen zu entscheiden, wird das inverse Problem als Klassifikationsproblem umformuliert.

In diesem Zusammenhang ist es sinnvoll, die beobachteten seismischen Daten direkt mit den von geodynamischen Modellen vorhergesagten zu vergleichen. Konkret bedeutet das eine Modellierungskette von der Geodynamik bis zur Wellenformsimulation. Diesen Prozess habe ich *SeLFiE* getauft: **Se**ismic and **L**ithological **Fi**ltering of **E**arth’s (and planets’) models. Es geht darum, seismische Signale aus Momentaufnahmen numerischer Erdmodelle mit denen der realen Erde zu vergleichen – als machten wir ein *Selfie* vom Inneren unseres Planeten.

Ich verfüge bereits über mehrere Sammlungen globaler 2D- und 3D-Modelle thermischer Konvektion und habe kürzlich Funktionen zum Einlesen dieser Modelle in `flexOPT.jl` integriert. Damit lassen sich thermische und chemische Felder visualisieren, einschließlich der Wasserzirkulation im Mantel oder des Aufstiegs von Eisen von seiner Basis.

Anschließend übersetzen wir diese Modelle in Parameter, die für die Ausbreitung seismischer Wellen relevant sind – Dichte, Geschwindigkeiten `Vp` und `Vs`, Anisotropie, Dämpfung – ausgehend von den *in situ*-Phasen, in Zusammenarbeit mit Petrologen. Diese Umrechnung berücksichtigt Unsicherheiten über Look-up-Tabellen.

Aus diesen Modellen erzeugen wir synthetische Seismogramme, aus denen wir Wellenformattribute (*features*) für eine Klassifikation oder überwachtes Lernen mit künstlicher Intelligenz extrahieren. Die in Python verfügbaren Codes können in das Julia-Ökosystem integriert werden.

{{< /collapse >}}

{{< collapse title="Fuji – ein neues natürliches Labor" >}}

Seit einem M2-Praktikum, das ich 2022 mit Yosuke Aoki betreut habe, interessiere ich mich für die Struktur und seismische Aktivität des Fuji. Anders als man zunächst denken könnte, erhält der Fuji nicht die Aufmerksamkeit, die er verdient. In Japan werden mehr als 100 aktive Vulkane wegen häufiger Ausbrüche überwacht, während der Fuji seit über 300 Jahren nicht ausgebrochen ist. Diese Inaktivität erschwert Vulkanologen seine Untersuchung – Seismologen jedoch nicht.

Anschließend habe ich ein CNRS-MITI-Promotionsstipendium für Hesaneh Mohammadi erhalten, betreut von Stéphanie Durand und mir. Das Projekt befasst sich mit der seismischen 3D- und 4D-Bildgebung des Fuji. Wir planen eine *Box-Tomographie* bei sehr hohen Frequenzen (> 2 Hz), um die ersten 50 km unter dem Vulkan abzubilden. Hier sind 1D- oder Standard-Tomographiemodelle zur Berechnung der Wellenfelder außerhalb der Box nicht mehr anwendbar. Ich schlage daher vor, die Gültigkeit der Ebene-Wellen-Näherung für isolierte Einsätze wie P- und S-Wellen zu prüfen. Danach wollen wir die Wellenformen niederfrequenter Beben (LFE) unter dem Vulkan zurückpropagieren.

Parallel dazu wurde mit Béatrice Puyssegur und Manon Dalaison im Rahmen der Promotion von Lorette Drique ein Projekt gestartet, das einen Werkzeugkasten zur Verringerung vegetationsbedingter Fehler in InSAR-Bildern entwickeln soll. Auch wenn das Thema nicht direkt mit dem Fuji zusammenhängt, planen wir, diese Methoden im dritten Promotionsjahr anzuwenden, um mögliche Deformationen in der Umgebung des Vulkans zu analysieren.

{{< /collapse >}}

{{< collapse title="Planetologie mit Seismologie: InSight / FSS" >}}

![SeLFiE Planetologie](/images/optiSeLFiE_schema.jpg)

Erweiterung der *SeLFiE*-Methodik auf die Planetologie, um Szenarien der thermochemischen Entwicklung von Erde, Mars und Mond anhand numerischer Modelle und von Attributen zu unterscheiden, die mit künstlicher Intelligenz oder Citizen Science extrahiert werden.

Für einige Projekte arbeite ich weiterhin gelegentlich mit Marsdaten von InSight. Beim Projekt FSS (*FarSide Suite*) auf dem Mond 2026 werde ich wissenschaftlicher und künstlerischer Mitarbeiter sein.

Wir werden die *SeLFiE*-Filtermethode für drei tellurische Körper vorschlagen. Wir sammeln 1D-, 2D- und 3D-Szenarien der Abkühlung des Magmaozeans und der Mantelkonvektion für Erde, Mars und Mond auf Grundlage geophysikalischer, geochemischer und petrologischer Beobachtungen. Dann konstruieren wir – numerisch über Mantelkonvektionssimulationen oder konzeptionell – heutige Planetenmodelle, mit besonderem Augenmerk auf die Geometrie teilweise geschmolzener Schichten oder Plumes an der Mantelbasis.

Wir wandeln diese Modelle in viskoelastische Parameter um, um seismische Wellen für verschiedene Szenarien zu simulieren und mit `flexOPT.jl` Sensitivitätskerne zu berechnen, die die für die Struktur der Mantelbasis empfindlichen Phasen vorhersagen.

Wir vergleichen die synthetischen seismologischen Daten, die Informationen über die Mantelbasis der drei Körper enthalten, mit den beobachteten Daten. So können wir die Relevanz der vorgeschlagenen Modelle bewerten und unser Verständnis dieser tiefen Strukturen verfeinern.

Anschließend klassifizieren wir die Daten nach Szenarien mithilfe künstlicher Intelligenz, um die Unterscheidbarkeit der verschiedenen Szenarien der Mantelbildung zu maximieren.

Parallel dazu organisieren wir eine Ausstellung zur Wissenschaftskommunikation rund um das Hören von Klängen – Vermittlungskonzerte und Hörsitzungen synthetischer und beobachteter Daten –, die auf der Psychologie der kognitiven Kontrolle aufbaut und unsere Forschung zugleich mit von der Öffentlichkeit gesammelten Daten bereichert.

{{< /collapse >}}
