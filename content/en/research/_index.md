+++
title = "Research"
draft = false
+++

from the global and regional tomography to scale reconcilation using mineralogic, petrologic and geodynamic constraints via a unique platform `flexOPT.jl`


{{< collapse title="Introduction générale" >}}

The aim of my research is to better understand the evolution of the interior of telluric bodies, by extracting maximum information from (geo)physical observations, particularly seismic waveforms.

I have been developing numerical and theoretical methods to invert seismic waveform data for elastic and anelastic parameters of the media at different scales, and I apply them to the real data.

One of my major contributions is the devlopment of the method called *box tomography* at different scales, in order to image a localised region (or "box") from the waveforms that have propagated not only inside the region but also the exteior of it.

Here, I present first the financements that I obtained to realise my research activities. Then I will take one example of my studies on the elastic and anelastic images to understand the micro dynamics below the Caroline plate, in collaboration with geodynamicists and petrologists. I will then ask questions on the chain of inverse problem, followed by examples of numerical and theoretical developments. At last, I will present my long-term dream.

![Schéma box-tomographie](/images/schema_box.png)

*
Some example of applications of box tomography at different scales:
(a) in global seismology, we use the teleseismic events in order to image localised regions; 
(b) below the Caroline plate, 1D and 3D waveform inversion for `Vs` and `Qs` is performed;
(c) 1D and 3D inversion for `Vs` in the LLVP beneath Hawaii;
(d) a new technology of tomography using neutrino oscillations;
(e) partial melts beneath the Réunion island;
(f) 3D imaging of Tibetan plateau and Mount Fuji.
*
{{< /collapse >}}

{{< collapse title="Financements obtenus" >}}

Tous les financements obtenus pour réaliser mes recherches sont détaillés dans la section consacrée aux financements. Deux tiers de ma thèse ont été financés par la JSPS (Société japonaise pour la promotion de la Science). Au Japon, jusqu’au début des années 2010, les doctorants ne bénéficiaient pas systématiquement d’un financement doctoral. J’ai donc dû rédiger mon propre projet de recherche, centré sur le développement de l’inversion des formes d’ondes pour l’élasticité et l’anélasticité, ce qui m’a permis d’acquérir dès cette époque un recul critique sur la rédaction de projets scientifiques.

Entre 2012 et 2017, j’ai été collaborateur et responsable principal de l’enseignement au sein du consortium GPX, dédié à l’exploration géophysique. Ce consortium a favorisé la recherche et la formation, en lien entre les universités et l’industrie. Mes travaux théoriques sur l’inversion localisée des formes d’ondes et le développement fondamental du calcul de sismogrammes synthétiques ont posé les bases de ma nouvelle méthode actuelle : les *opérateurs optimaux pour les équations aux dérivées partielles arbitraires*.

J’ai ensuite contribué aux études préparatoires du sismomètre de la mission InSight sur Mars, ce qui m’a conduit à travailler sur la première détermination des mécanismes au foyer sur Mars à l’aide de mes méthodes d’inversion.

Parallèlement, j’ai obtenu plusieurs financements pour organiser des workshops internationaux, qui ont permis de nouer des collaborations pérennes. Grâce à ma collaboration étroite avec Frédéric Deschamps (Academia Sinica), j’ai participé à plusieurs projets franco-taïwanais, au sein desquels j’ai pu développer la série d’études en imagerie sismo-pétrologique décrite ci-dessous. Ce partenariat m’a permis de diriger ma première doctorante officielle, S.-T. Lai, dans le cadre de l’appel MOPGA (*Make Our Planet Great Again*).

Depuis 2022, je suis membre junior de l’Institut universitaire de France (IUF) en médiation scientifique, ce qui me permet de consacrer du temps à la fois à mes recherches et à mes activités de médiation auprès du grand public.

J’ai récemment obtenu plusieurs financements doctoraux, notamment autour de la caractérisation du mont Fuji. Une collaboration étroite s’est également engagée avec Véronique Van Elewyck, avec qui nous avons obtenu deux bourses postdoctorales sur la tomographie neutrino pour l’imagerie de la Terre profonde à partir d’observables géophysiques.

{{< /collapse >}}


{{< collapse title="Bilan : micro-dynamique du manteau sous la plaque Caroline" >}}

![Schéma Caroline](/images/caro_schema.jpg)

*Figure suggérée — `caro_schema.jpg`*  
Schéma simplifié d’une série d’études tomographiques ciblant le manteau sous la plaque Caroline. Nos images tomographiques, couplées à des prédictions pétrologiques, suggèrent qu’un panache mantellique profond, à proximité immédiate de la limite du LLVP pacifique/hawaïen, pourrait entraîner du fer depuis la limite noyau-manteau. Dans la zone de transition située au-dessus, on identifie un panache plus superficiel, qui alimente la dorsale d’Eauripik et pourrait contribuer à la dynamique rapide de la microplaque Caroline.

Dans cette section, je présente brièvement mes études basées sur l’inversion de formes d’ondes que j’ai développée tout au long de ma carrière. Je me limite à présenter la série d’études tomographiques du manteau supérieur et inférieur sous la plaque Caroline. En haut, cette microplaque est entourée de grandes plaques anciennes tandis qu’en bas du manteau, la région correspond à une zone de faible vitesse de propagation des ondes sismiques (LLVP) sous Hawaï. Nous avons imagé un petit panache venant du fond du manteau, probablement riche en fer, remontant peut-être jusqu’à l’alimentation de la dorsale de la plaque Caroline, poussant la microplaque vers le sud avec une grande vitesse, ce qui entraîne un régime de subduction de type *roll-over*.

### Plaque Caroline

La plaque Caroline présente un contexte géodynamique particulièrement complexe : encadrée par les plaques australienne, philippine et pacifique, elle se situe dans une zone à convergence rapide, marquée par des subductions actives et anciennes, des marges transformantes, des rifts abandonnés et une activité volcanique soutenue. Une structure majeure, la dorsale d’Eauripik, perturbe le centre de la plaque et constitue une anomalie topographique et magmatique notable, interprétée soit comme une ancienne dorsale morte, soit comme la trace d’un panache profond ou d’un point chaud.

La géométrie des anomalies magnétiques, la bathymétrie, et des structures comme la fosse de Sorol ou les fosses de Nouvelle-Guinée témoignent d’une dynamique encore mal comprise, et potentiellement liée à une remontée mantellique profonde à la limite noyau-manteau.

### Structure profonde et panache de Caroline

Nous avons mené une série d’études d’imagerie sismique dans cette région en appliquant la méthode d’inversion des formes d’ondes, que j’ai développée au cours de ma thèse et de mon post-doctorat. Cette approche permet d’imager à haute résolution les vitesses de cisaillement `Vs` et les facteurs de qualité `Qs`, particulièrement sensibles aux contrastes thermiques. En exploitant les données du réseau japonais F-net, pour des séismes profonds situés dans les régions de Tonga et Fidji, nous avons mis en évidence une anomalie marquée et localisée de `Vs` et `Qs`, centrée sous le panache de Caroline.

L’interprétation des résultats suggère un excès de température localisé d’environ 100 K dans le LLVP pacifique, ainsi qu’une possible contribution d’un matériau enrichi en fer dans le panache, incompatible avec un modèle purement thermique. L’analyse a été étendue à d’autres régions du Pacifique pour confirmer le caractère localisé de ces anomalies. La modélisation géodynamique et minéralogique indique une interaction possible avec la limite noyau-manteau sur plusieurs centaines de kilomètres de hauteur.

### Structure de la zone de transition et du manteau supérieur

Enfin, nous avons mené une inversion Monte Carlo des temps d’arrivée de phases multiples, pour contraindre la structure de la zone de transition du manteau sous la plaque Caroline. Le modèle final, basé sur des jeux de données SS et des modélisations de formes d’ondes, révèle une vitesse de cisaillement anormalement élevée dans tout le manteau supérieur. Après plusieurs simulations géodynamiques, nous avons conclu que notre modèle sismique indique la possibilité de subductions de plaque en rouleau *roll-over* à partir de la limite sud et éventuellement aussi de la limite nord, ainsi que la présence d’anomalies de vitesse basses en forme de panache s’étendant au moins à 800 km de profondeur sous la plaque Caroline. Nos simulations géodynamiques montrent en outre que la subduction *roll-over* nécessite une vitesse de poussée de la plaque relativement rapide.

{{< /collapse >}}

{{< collapse title="Questions ouvertes" >}}

Même si cette approche d’imagerie localisée, dite *box-tomographie*, a permis d’éclairer certaines régions critiques pour la compréhension de la dynamique du manteau terrestre, de nombreux points restent encore à améliorer ou à élucider, tant du point de vue scientifique que technique.

L’un des verrous majeurs de cette méthodologie réside dans la négligence des hétérogénéités situées en dehors de la boîte d’étude. Jusqu’à présent, nous avons utilisé uniquement des modèles sphériques 1D pour simuler le champ d’ondes, aussi bien lors du calcul des dérivées partielles des formes d’ondes que pour la reconstruction du champ d’ondes aux limites de la boîte. Nous avons évalué la propagation d’erreurs liée à cette approximation dans un cadre cartésien, mais l’absence de traitement rigoureux des effets extérieurs reste une limitation importante à prendre en compte plus sérieusement à l’avenir. Le couplage entre la méthode des éléments spectraux et ma méthode DSM, bien que prometteur, reste très coûteux en ressources. C’est entre autres pour répondre à ce défi que j’ai entrepris récemment une réorganisation complète de ma boîte à outils numériques.

Par ailleurs, concernant la remontée du panache mantellique de Caroline, la portion du manteau située entre 800 km et 2500 km de profondeur reste à imager. L’objectif est de vérifier la continuité éventuelle de la colonne panachique depuis la limite noyau-manteau jusqu’à la surface. Excepté des études que nous avons menées sur la base du panache, nous n’avons pas encore eu l’occasion d’interpréter quantitativement les modèles tomographiques obtenus, qui restent pour l’instant exprimés uniquement en termes de paramètres sismologiques tels que `Vs` et `Qs`. Il devient désormais essentiel d’engager des collaborations avec des pétrologues, des géochimistes et des géodynamiciens afin de mieux interpréter et valoriser les structures mises en évidence par la sismologie. Dans cette perspective, je propose une démarche de filtrage sismique innovante, baptisée *SeLFiE*.

{{< /collapse >}}

{{< collapse title="Outils numériques et théoriques" >}}

![Codes et flexOPT](/images/codes.jpg)

*Figure suggérée — `codes.jpg`*  
État de mes codes jusqu’à 2023 (gauche) et développement récent de `flexOPT.jl` (droite). Cette figure résume l’évolution de mes outils, depuis les développements Fortran historiques jusqu’au méta-programme générique en Julia capable de dériver automatiquement des opérateurs optimaux pour des EDP arbitraires.

Ce qui distingue mon approche de celle d’autres sismologues, c’est que je m’intéresse à la dynamique du manteau et à l’apport des processus chimiques dans cette dynamique, tout en étant également développeur de schémas numériques, aussi bien pour l’inversion que pour la modélisation directe. J’analyse les données en même temps que je conçois les outils théoriques et numériques pour les interpréter.

Depuis ma thèse, j’ai développé de nombreux codes basés sur la méthode DSM (*Direct Solution Method*) en domaine fréquentiel pour des planètes sphériques, ainsi que sur la méthode des différences finies en domaine temporel avec des opérateurs modifiés. Ces deux approches reposent sur une base théorique commune : celle des opérateurs optimaux. J’ai consacré une partie importante de mon travail à la mise en œuvre numérique de cette théorie, en développant des codes spécifiques.

Les opérateurs optimaux sont des opérateurs compacts qui permettent d’atteindre une précision supérieure à celle des opérateurs conventionnels utilisant le même nombre de points en espace et en temps. Toutefois, la méthode générale pour dériver ces opérateurs n’avait jamais été formulée de manière systématique. J’ai moi-même contribué à l’optimisation des opérateurs pour les éléments spectraux, sans pour autant imaginer qu’une recette générale serait accessible.

La plupart de ces codes étaient écrits en Fortran, ce qui s’est avéré difficile à maintenir : un code pour chaque objectif spécifique, avec un débogage long et fastidieux. J’ai donc récemment décidé de repartir de zéro pour concevoir un méta-programme unique, capable de couvrir de nombreux cas d’usage. Le langage *Julia* s’est imposé comme un choix naturel, grâce à ses capacités de méta-programmation, de manipulation symbolique et à son intégration fluide avec des outils modernes tels que MPI ou les GPU.

En travaillant sur ce projet avec Thibault Duretz, qui m’a suggéré plusieurs équations tests ainsi que des pistes d’optimisation du code, j’ai pu formaliser une méthode générale permettant de dériver automatiquement des opérateurs optimaux pour des équations aux dérivées partielles arbitraires. Un préprint présentant cette approche est actuellement soumis à *Computer Methods in Applied Mechanics and Engineering*.

Parallèlement aux tests et au benchmarking, le code `flexOPT.jl` est d’ores et déjà utilisé pour la résolution de diverses équations aux dérivées partielles. Il est notamment mis en œuvre par ma doctorante Hesaneh Mohammadi dans le cadre d’un projet de tomographie du mont Fuji, où il est comparé à d’autres codes de référence.

{{< /collapse >}}

{{< collapse title="Projet de recherche : vision d’ensemble" >}}

![Stratégie tomographie-géodynamique-SeLFiE](/images/tomo_projet.jpg)

*Figure suggérée — `tomo_projet.jpg`*  
Schéma illustrant les projets de recherche que je souhaite mener.  
À gauche : amélioration de la tomographie des formes d’ondes, de l’échelle globale à l’échelle locale, avec prise en compte des effets extérieurs à la boîte.  
Au centre : interprétation lithologique et filtrage sismologique par l’approche *SeLFiE*.  
À droite : modélisation de la convection du manteau et génération de Terres virtuelles dont on peut calculer les observables sismiques et neutrino.

Comme évoqué plus haut, plusieurs projets s’inscrivent naturellement dans la continuité de mes activités de recherche. Maintenant que mon projet de modernisation et de démocratisation des opérateurs optimaux arrive à maturité, il est temps pour moi de mobiliser pleinement ces acquis afin de revisiter des données sismologiques, mais aussi d’autres types de données, dans le but de répondre à certaines des grandes questions qui traversent les géosciences : comment les planètes ont-elles évolué depuis la formation du système solaire, et comment évolueront-elles dans le futur ? Qu’est-ce qui rend notre planète si unique parmi ses voisines ?



{{< /collapse >}}

{{< collapse title="Tomographie des formes d’ondes, de/à l’échelle locale à/de l’échelle globale" >}}

L’approche de *box-tomographie* repose sur l’hypothèse que le champ d’onde incident peut être estimé avec une précision suffisante, soit à partir d’un modèle 1D de référence de la Terre, soit en supposant que les ondes incidentes se comportent comme des ondes planes. Cette approximation est raisonnablement valable pour certaines premières ondes de volume isolées, comme les ondes P directes, PKP ou S. Toutefois, elle devient insuffisante à haute fréquence, où la cohérence du champ d’onde global ne peut plus être garantie.

Pour contourner cette limitation, je propose d’utiliser plusieurs modèles tomographiques plus réalistes, tels que SEISGLOB2, permettant une représentation plus fidèle de la propagation des ondes complexes, en particulier dans les régions où l’hétérogénéité du manteau influence fortement les phases observées. Afin de mieux contraindre les incertitudes, j’utiliserai plusieurs modèles issus de différentes observables, telles que les ondes de surface ou les temps d’arrivée des ondes de volume.

Je vais ainsi mettre à jour ma méthode de box-tomographie en tenant compte des hétérogénéités au-delà de la région d’intérêt. Si des tests synthétiques ont déjà été menés dans un cadre cartésien, l’application de cette méthode en sismologie globale constituera une première. Cette nouvelle version de la box-tomographie nécessite des solveurs capables de modéliser des milieux 3D dans deux domaines imbriqués (global et local), ce qui a motivé le développement de la méthode `flexOPT.jl`.

Je vais notamment explorer des phases permettant d’imager la région s’étendant de la base du manteau jusqu’à la surface de la plaque de Caroline, pour les paramètres `Vs`, `Qs`, `Vp`, `Qp`, ainsi que, dans un second temps, l’anisotropie. Cela contribuera à mieux comprendre la dynamique du panache que j’ai imaginé, depuis la base du manteau jusqu’au manteau supérieur. La région sous la microplaque de Caroline pourrait offrir une scène encore jamais observée, exotique du point de vue de la géodynamique, à la bordure de la LLVP hawaïenne.

J’envisage également d’appliquer cette méthode à d’autres régions géodynamiquement actives, notamment le manteau supérieur et la zone de transition sous le Japon, La Réunion et le plateau Tibétain.

En utilisant les modèles globaux pour affiner l’image locale dans les boîtes, nous pourrons faire progresser la résolution de la Terre profonde, étape par étape. Cependant, il est bien connu que l’inversion des formes d’ondes souffre plus fortement de non-unicité et de non-linéarité que l’inversion d’attributs secondaires comme la dispersion des ondes de surface ou les temps d’arrivée. Il est donc crucial de démarrer l’inversion à partir de modèles initiaux réalistes. Je poursuivrai également le travail d’interprétation des modèles tomographiques en collaboration avec des pétrologues, pour traduire ces modèles en paramètres physico-chimiques plus pertinents pour contraindre la dynamique du manteau.

{{< /collapse >}}

{{< collapse title="Tomographie des oscillations de neutrinos" >}}

Récemment, les physiciens des hautes énergies ont commencé à s’intéresser à l’utilisation des oscillations de neutrinos traversant l’intérieur de la Terre pour en imager la structure. Depuis 2022, en collaboration avec Véronique Van Elewyck, nous co-encadrons deux postdoctorants et travaillons à la formalisation du problème inverse associé à ce type de données. Nous évaluons la sensibilité de ces observations aux structures internes de la Terre.

Les neutrinos sont produits dans l’atmosphère à la suite de l’interaction des rayons cosmiques avec les particules atmosphériques, puis pénètrent dans la Terre. Leur interaction avec la matière est extrêmement faible, mais au cours de leur propagation – à une vitesse proche de celle de la lumière – ils peuvent changer de saveur via un mécanisme d’oscillation sensible à la densité électronique rencontrée le long du trajet. Comme l’hydrogène-1 est pratiquement le seul atome dont le nombre de neutrons est nul, ces observations pourraient permettre de contraindre indirectement la teneur en eau de l’intérieur de la Terre, bien que la résolution spatiale reste limitée à des échelles supérieures à 1000 km.

Nous utilisons le code EarthProb, une version spécialisée du logiciel OscProb, pour simuler ces oscillations de saveur. Je suis en train d’intégrer ce code dans l’environnement de modélisation et d’inversion `flexOPT.jl`, afin de pouvoir explorer des configurations inverses plus flexibles.

Par ailleurs, l’arrivée prochaine de Hyper-Kamiokande, un observatoire de neutrinos de nouvelle génération dont la mise en service est prévue au Japon en 2027, devrait considérablement améliorer la résolution et la gamme d’énergie détectable. Ce nouvel instrument pourrait transformer profondément notre capacité à sonder l’intérieur de la Terre par cette méthode.

{{< /collapse >}}

{{< collapse title="SeLFiE : Seismic and Lithological Filtering of Earth’s and planets’ models avec flexOPT.jl" >}}

Que se passerait-il si nous parvenions à imager l’intérieur de la Terre avec une résolution de quelques centimètres ? Serait-ce une victoire définitive ? Même si l’on parvient à mieux contraindre la dynamique interne par inversion des données géophysiques, comprendre l’évolution de la Terre profonde constitue un tout autre problème inverse, cette fois à paramètres quasi illimités.

L’un des grands débats persistants en géodynamique concerne l’origine des LLVPs : sont-elles d’origine purement thermique ou bien thermochimique ? En d’autres termes, la convection du manteau est-elle uniquement thermique, ou bien la chimie y joue-t-elle un rôle essentiel ? Pour trancher ce type de questions, le problème inverse se reformule en un problème de classification.

Dans ce contexte, il devient pertinent d’examiner directement les données sismiques observées, comparées à celles prédites par des modèles géodynamiques. Concrètement, cela implique une modélisation en chaîne allant de la géodynamique à la simulation des formes d’onde. J’ai baptisé ce processus *SeLFiE :* **Se**ismic and **L**ithological **Fi**ltering of **E**arth’s (and planets’) models. Il s’agit de confronter les signaux sismiques générés à partir d’instantanés de modèles numériques de la Terre à ceux de la Terre réelle, comme si nous prenions un *selfie* de l’intérieur de notre planète.

Je dispose déjà de plusieurs collections de modèles globaux de convection thermique 2D et 3D. Récemment, j’ai intégré des fonctionnalités pour lire ces modèles dans le cadre de `flexOPT.jl`. Cela permet de visualiser les champs thermiques et chimiques, incluant la circulation de l’eau dans le manteau ou encore la remontée de fer depuis sa base.

Nous traduisons ensuite ces modèles en paramètres physiques pertinents pour la propagation des ondes sismiques — densité, vitesses `Vp` et `Vs`, anisotropie, atténuation — à partir des phases *in situ*, en collaboration avec des pétrologues. Cette conversion tient compte des incertitudes grâce à des tables de correspondance (*look-up tables*).

À partir de ces modèles, nous générons des sismogrammes synthétiques, sur lesquels nous extrayons des attributs (*features*) de forme d’onde, en vue d’une classification ou d’un apprentissage supervisé par intelligence artificielle. Les codes, disponibles en Python, pourront être intégrés dans l’écosystème Julia.

{{< /collapse >}}

{{< collapse title="Mont Fuji – nouveau laboratoire naturel" >}}

Représentation des cohérences temporelles entre des données continues enregistrées à six stations autour du mont Fuji durant l’année 2008, projetées via *UMAP*. Cette représentation permet de visualiser l’évolution temporelle des régimes sismiques et d’identifier des signaux associés à des *Low Frequency Earthquakes* (LFE) ainsi que d’autres événements tectoniques.

Depuis le stage d’Adèle Doucet, que j’ai co-encadré avec Yosuke Aoki en 2022, je m’intéresse à la structure et à l’activité sismique du mont Fuji. Contrairement à ce que l’on pourrait penser au premier abord, le mont Fuji ne reçoit pas l’attention qu’il mérite. Au Japon, plus de 100 volcans actifs sont surveillés en raison d’éruptions fréquentes, tandis que le mont Fuji n’a connu aucune éruption depuis plus de 300 ans. Cette inactivité rend son étude plus difficile pour les volcanologues, à l’exception des sismologues.

Avec Léonard Seydoux et Jean-Philippe Métaxian, nous avons commencé à encadrer la thèse d’Adèle Doucet, dont l’objectif est de développer une méthode de surveillance des données sismiques continues à l’aide de l’apprentissage automatique, notamment via la méthode *UMAP*. En définissant des attributs de cohérence entre six stations sismiques autour du mont Fuji, nous avons pu catégoriser automatiquement les *Low Frequency Earthquakes* (LFE), ainsi que d’autres événements sismiques d’origine tectonique.

Depuis cette première étude, j’ai obtenu une bourse de thèse CNRS-MITI pour Hesaneh Mohammadi, dont l’encadrement est assuré avec Stéphanie Durand et moi-même. Le projet porte sur l’imagerie sismologique 3D et 4D du mont Fuji. Nous prévoyons de mener une *box-tomographie* à très haute fréquence (> 2 Hz) pour imager les premiers 50 km sous le volcan. Dans cette approche, l’utilisation de modèles 1D ou tomographiques standards pour calculer les champs d’onde extérieurs à la boîte devient inapplicable. Je propose donc d’évaluer la validité de l’approximation par ondes planes pour des arrivées isolées telles que les ondes P et S. Une fois cette étape franchie, nous chercherons à rétro-propager les formes d’onde associées aux LFE identifiés pendant la thèse d’Adèle Doucet.

En parallèle, un projet a été lancé avec Béatrice Puyssegur et Manon Dalaison dans le cadre de la thèse de Lorette Drique. Cette thèse vise à développer une boîte à outils pour atténuer les erreurs affectant les images InSAR dues à la végétation. Bien que ce sujet ne soit pas directement lié au mont Fuji, nous envisageons d’appliquer ces méthodes durant la troisième année de thèse afin d’analyser les éventuelles déformations de la région entourant le volcan.

{{< /collapse >}}

{{< collapse title="Planétologie à l’aide de la sismologie : InSight / FSS" >}}

![SeLFiE planétologie](/images/optiSeLFiE_schema.jpg)

*Figure suggérée — `optiSeLFiE_schema.jpg`*  
Extension de la méthodologie *SeLFiE* à la planétologie pour distinguer des scénarios d’évolution thermo-chimique de la Terre, Mars et de la Lune à partir de modèles numériques et d’attributs extraits par intelligence artificielle ou science participative.

Je continue à travailler occasionnellement sur des données martiennes InSight pour certains projets. Pour le projet FSS (*FarSide Suite*) sur la Lune en 2026, je serai collaborateur scientifique et artistique.

Nous allons proposer la méthode de filtrage *SeLFiE* pour trois corps telluriques. Nous collecterons des scénarios 1D, 2D et 3D de refroidissement de l’océan magmatique et de convection mantellique pour la Terre, Mars et la Lune, basés sur des observations géophysiques, géochimiques et pétrologiques. Ensuite, nous construirons numériquement, via des simulations de convection mantellique, ou conceptuellement, des modèles planétaires actuels, en mettant un accent particulier sur la géométrie des couches partiellement fondues ou des panaches à la base du manteau.

Nous convertirons ces modèles en paramètres viscoélastiques afin de simuler les ondes sismiques pour différents scénarios et de calculer des noyaux de sensibilité permettant de prédire les phases sensibles à la structure de la base du manteau avec `flexOPT.jl`.

Nous comparerons les données sismologiques synthétiques, qui contiennent des informations sur la base du manteau des trois corps telluriques, avec les données observées. Cela nous permettra d’évaluer la pertinence des modèles proposés et d’affiner notre compréhension de ces structures profondes.

Ensuite, nous catégoriserons les données selon les scénarios à l’aide de l’intelligence artificielle, maximisant ainsi la capacité à distinguer les différents scénarios de formation du manteau.

En parallèle, nous organiserons une exposition de médiation scientifique axée sur l’écoute des sons — concerts de médiation scientifique et séances d’écoute des données synthétiques et observées — en utilisant la psychologie du contrôle cognitif, et aussi pour enrichir notre recherche avec les données collectées avec le grand public.

{{< /collapse >}}