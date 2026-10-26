+++
title = "Investigación"
draft = false
+++

De la tomografía global y regional a la reconciliación de escalas gracias a restricciones mineralógicas, petrológicas y geodinámicas, con la plataforma única `flexOPT.jl`

{{< collapse title="Introducción general" >}}

Mi proyecto de investigación busca restringir mejor la evolución del interior de los cuerpos telúricos a partir del análisis de datos (geo)físicos, en particular de las formas de onda sísmicas.

Con el tiempo he desarrollado métodos numéricos y teóricos de inversión de formas de onda que tienen en cuenta las propiedades elásticas y viscoelásticas de los medios a distintas escalas, y los he aplicado a datos reales.

Una de mis principales contribuciones es el desarrollo de la llamada *tomografía en caja* (*box tomography*) a varias escalas, que permite obtener la imagen de una región localizada (o «caja») a partir de formas de onda sísmicas que muestrean no solo el interior de esa región sino también su entorno.

Presento primero la financiación que ha hecho posible mi investigación. Ilustro después una serie de trabajos de imagen elástica y anelástica sobre la microdinámica bajo la placa de las Carolinas, realizados con geodinamistas y petrólogos. Planteo luego preguntas sobre los métodos, los resultados y las interpretaciones. A continuación describo la caja de herramientas teóricas y numéricas que he desarrollado para responder a problemas científicos variados. Por último, describo el proyecto de investigación que deseo llevar adelante con mis socios actuales y futuros.

![Esquema de la tomografía en caja](/images/schema_box.png)

*
Algunos ejemplos de aplicación de la tomografía en caja a distintas escalas:
(a) en sismología global, uso de eventos telesísmicos para obtener imágenes de regiones localizadas;  
(b) bajo la placa de las Carolinas, inversión de formas de onda 1D y 3D para `Vs` y `Qs`;  
(c) inversión 1D y 3D para `Vs` en la LLVP bajo Hawái;  
(d) apertura hacia la imagen con neutrinos;  
(e) restricciones sobre el ascenso de fusión parcial bajo La Reunión;  
(f) imagen 3D de `Vp`, `Vs` y densidad bajo la meseta tibetana, extendida recientemente al monte Fuji.
*
{{< /collapse >}}

{{< collapse title="Financiación obtenida" >}}

Dos tercios de mi doctorado fueron financiados por la JSPS (Sociedad Japonesa para la Promoción de la Ciencia). En Japón, hasta comienzos de la década de 2010, los doctorandos no recibían financiación de forma sistemática. Tuve, pues, que redactar mi propio proyecto, centrado en el desarrollo de la inversión de formas de onda para la elasticidad y la anelasticidad, lo que me dio pronto una mirada crítica sobre la redacción de proyectos científicos.

Entre 2012 y 2017 fui colaborador y principal responsable de la docencia en el consorcio GPX, dedicado a la geofísica de exploración. Este consorcio impulsó la investigación y la formación, conectando universidades e industria. Mis trabajos teóricos sobre la inversión localizada de formas de onda y el desarrollo fundamental del cálculo de sismogramas sintéticos sentaron las bases de mi nuevo método actual: los *operadores óptimos para ecuaciones en derivadas parciales arbitrarias*.

Después contribuí a los estudios preparatorios del sismómetro de la misión InSight a Marte, lo que me llevó a la primera determinación de mecanismos focales en Marte con mis métodos de inversión.

Paralelamente, obtuve varias ayudas para organizar talleres internacionales que dieron lugar a colaboraciones duraderas. Gracias a mi estrecha colaboración con Frédéric Deschamps (Academia Sinica), participé en varios proyectos franco-taiwaneses en los que desarrollé la serie de estudios de imagen sismo-petrológica descrita más abajo. Esta alianza me permitió dirigir a mi primera doctoranda oficial, S.-T. Lai, en el marco de la convocatoria MOPGA (*Make Our Planet Great Again*).

Desde 2022 soy miembro junior del Institut universitaire de France (IUF) en mediación científica, lo que me permite dedicar tiempo tanto a la investigación como a la divulgación para el gran público.

Recientemente obtuve varias financiaciones de doctorado, en particular sobre la caracterización del monte Fuji. También ha comenzado una estrecha colaboración con Véronique Van Elewyck, con quien obtuvimos dos becas posdoctorales sobre tomografía de neutrinos para la imagen de la Tierra profunda a partir de observables geofísicos.

{{< /collapse >}}


{{< collapse title="Balance: microdinámica del manto bajo la placa de las Carolinas" >}}

![Esquema de la placa de las Carolinas](/images/caro_schema.jpg)

Esquema simplificado de una serie de estudios tomográficos del manto bajo la placa de las Carolinas. Nuestras imágenes tomográficas, combinadas con predicciones petrológicas, sugieren que una pluma mantélica profunda, junto al borde de la LLVP del Pacífico/Hawái, podría arrastrar hierro desde el límite núcleo-manto. En la zona de transición superior se identifica una pluma más somera, que alimenta la dorsal de Eauripik y podría contribuir a la rápida dinámica de la microplaca de las Carolinas.

En esta sección presento brevemente mis estudios basados en la inversión de formas de onda que he desarrollado a lo largo de mi carrera, limitándome a la serie de estudios tomográficos del manto superior e inferior bajo la placa de las Carolinas. Arriba, esta microplaca está rodeada de grandes placas antiguas, mientras que en la base del manto la región corresponde a una zona de baja velocidad de ondas de cizalla (LLVP) bajo Hawái. Obtuvimos la imagen de una pequeña pluma que asciende desde el fondo del manto, probablemente rica en hierro, quizá hasta alimentar la dorsal de la placa de las Carolinas, empujando la microplaca hacia el sur a gran velocidad, lo que da lugar a un régimen de subducción de tipo *roll-over*.

### La placa de las Carolinas

La placa de las Carolinas presenta un contexto geodinámico particularmente complejo: rodeada por las placas australiana, filipina y del Pacífico, se sitúa en una zona de convergencia rápida marcada por subducciones activas y antiguas, márgenes transformantes, rifts abandonados y una actividad volcánica sostenida. Una estructura mayor, la dorsal de Eauripik, atraviesa el centro de la placa y constituye una anomalía topográfica y magmática notable, interpretada como una antigua dorsal muerta o como la huella de una pluma profunda o de un punto caliente.

La geometría de las anomalías magnéticas, la batimetría y estructuras como la fosa de Sorol o las fosas de Nueva Guinea muestran una dinámica todavía mal comprendida, posiblemente ligada a un ascenso mantélico profundo desde el límite núcleo-manto.

### Estructura profunda y pluma de las Carolinas

Realizamos una serie de estudios de imagen sísmica en esta región con el método de inversión de formas de onda que desarrollé durante mi doctorado y mi posdoc. Este enfoque permite obtener imágenes de alta resolución de la velocidad de cizalla `Vs` y del factor de calidad `Qs`, especialmente sensibles a los contrastes térmicos. Con datos de la red japonesa F-net para sismos profundos en las regiones de Tonga y Fiyi, pusimos de manifiesto una anomalía marcada y localizada de `Vs` y `Qs`, centrada bajo la pluma de las Carolinas.

La interpretación sugiere un exceso de temperatura localizado de unos 100 K en la LLVP del Pacífico, así como una posible contribución de material enriquecido en hierro en la pluma, incompatible con un modelo puramente térmico. El análisis se extendió a otras regiones del Pacífico para confirmar el carácter localizado de estas anomalías. La modelización geodinámica y mineralógica indica una posible interacción con el límite núcleo-manto a lo largo de varios cientos de kilómetros de altura.

### Estructura de la zona de transición y del manto superior

Por último, realizamos una inversión de Monte Carlo de los tiempos de llegada de varias fases para restringir la estructura de la zona de transición del manto bajo la placa de las Carolinas. El modelo final, basado en conjuntos de datos SS y en la modelización de formas de onda, revela una velocidad de cizalla anormalmente alta en todo el manto superior. Tras varias simulaciones geodinámicas, concluimos que nuestro modelo sísmico apunta a posibles subducciones de placa de tipo *roll-over* desde el límite sur y, eventualmente, también desde el norte, así como a anomalías de baja velocidad en forma de pluma que se extienden al menos hasta 800 km de profundidad bajo la placa de las Carolinas. Las simulaciones muestran además que la subducción *roll-over* requiere un empuje de la placa relativamente rápido.

{{< /collapse >}}

{{< collapse title="Preguntas abiertas" >}}

Aunque este enfoque de imagen localizada, la *tomografía en caja*, ha permitido esclarecer algunas regiones clave para entender la dinámica del manto, muchos puntos siguen pendientes de mejorar o aclarar, tanto en lo científico como en lo técnico.

Uno de los principales obstáculos de esta metodología es que se desprecian las heterogeneidades situadas fuera de la caja. Hasta ahora solo hemos usado modelos esféricos 1D para simular el campo de ondas, tanto para calcular las derivadas parciales de las formas de onda como para reconstruir el campo de ondas en los bordes de la caja. Evaluamos la propagación de errores debida a esta aproximación en un marco cartesiano, pero la falta de un tratamiento riguroso de los efectos externos sigue siendo una limitación importante que habrá que abordar con más seriedad. El acoplamiento entre el método de elementos espectrales y mi método DSM, aunque prometedor, sigue siendo muy costoso. Es, entre otras cosas, para responder a este reto que emprendí recientemente una reorganización completa de mi caja de herramientas numéricas.

Además, en cuanto al ascenso de la pluma mantélica de las Carolinas, falta obtener la imagen de la porción del manto entre 800 y 2500 km de profundidad, para verificar la posible continuidad de la columna de la pluma desde el límite núcleo-manto hasta la superficie. Salvo en los estudios sobre la base de la pluma, aún no hemos tenido ocasión de interpretar cuantitativamente los modelos tomográficos obtenidos, que de momento solo se expresan en parámetros sismológicos como `Vs` y `Qs`. Es ahora esencial colaborar con petrólogos, geoquímicos y geodinamistas para interpretar y valorizar mejor las estructuras reveladas por la sismología. Con este fin propongo un enfoque innovador de filtrado sísmico al que llamé *SeLFiE*.

{{< /collapse >}}

{{< collapse title="Herramientas numéricas y teóricas" >}}

![Códigos y flexOPT](/images/codes.jpg)

Estado de mis códigos hasta 2023 (izquierda) y desarrollo reciente de `flexOPT.jl` (derecha). La figura resume la evolución de mis herramientas, desde los desarrollos históricos en Fortran hasta el metaprograma genérico en Julia capaz de derivar automáticamente operadores óptimos para EDP arbitrarias.

Lo que distingue mi enfoque del de otros sismólogos es que me interesa la dinámica del manto y el papel de los procesos químicos en ella, siendo a la vez desarrollador de esquemas numéricos, tanto para la inversión como para la modelización directa. Analizo los datos al mismo tiempo que diseño las herramientas teóricas y numéricas para interpretarlos.

Desde mi doctorado he desarrollado numerosos códigos basados en el Direct Solution Method (DSM) en el dominio de la frecuencia para planetas esféricos, así como en diferencias finitas en el dominio del tiempo con operadores modificados. Ambos enfoques descansan sobre una base teórica común: los operadores óptimos. He dedicado una parte importante de mi trabajo a la implementación numérica de esta teoría mediante códigos específicos.

Los operadores óptimos son operadores compactos que alcanzan una precisión superior a la de los operadores convencionales con el mismo número de puntos en el espacio y en el tiempo. Sin embargo, el método general para derivarlos nunca se había formulado de forma sistemática. Yo mismo contribuí a optimizar operadores para elementos espectrales, sin imaginar que una receta general estuviera a nuestro alcance.

La mayoría de estos códigos estaban escritos en Fortran y resultaron difíciles de mantener: un código para cada propósito, con una depuración larga y tediosa. Por eso decidí recientemente empezar de cero y diseñar un único metaprograma capaz de cubrir muchos casos de uso. *Julia* se impuso como elección natural gracias a sus capacidades de metaprogramación y manipulación simbólica y a su integración fluida con herramientas modernas como MPI o las GPU.

Trabajando en este proyecto con Thibault Duretz, que me sugirió varias ecuaciones de prueba y vías de optimización del código, pude formalizar un método general para derivar automáticamente operadores óptimos para ecuaciones en derivadas parciales arbitrarias. Un preprint que presenta este enfoque se ha enviado a *Computer Methods in Applied Mechanics and Engineering*.

Paralelamente a las pruebas y al benchmarking, el código `flexOPT.jl` ya se utiliza para resolver diversas ecuaciones en derivadas parciales, en particular por mi doctoranda Hesaneh Mohammadi en un proyecto de tomografía del monte Fuji, donde se compara con otros códigos de referencia.

{{< /collapse >}}

{{< collapse title="Proyecto de investigación: visión de conjunto" >}}

![Estrategia tomografía–geodinámica–SeLFiE](/images/tomo_projet.jpg)

Esquema de los proyectos de investigación que deseo llevar a cabo.  
A la izquierda: mejora de la tomografía de formas de onda, de la escala global a la local, teniendo en cuenta los efectos exteriores a la caja.  
En el centro: interpretación litológica y filtrado sismológico con el enfoque *SeLFiE*.  
A la derecha: modelización de la convección del manto y generación de Tierras virtuales cuyos observables sísmicos y de neutrinos pueden calcularse.

Como se ha mencionado, varios proyectos se inscriben de forma natural en la continuidad de mi investigación. Ahora que mi proyecto de modernización y democratización de los operadores óptimos llega a su madurez, es momento de movilizar plenamente estos logros para revisitar datos sismológicos, y también de otros tipos, con el fin de responder a algunas de las grandes preguntas de las geociencias: ¿cómo han evolucionado los planetas desde la formación del sistema solar y cómo evolucionarán en el futuro? ¿Qué hace que nuestro planeta sea tan único entre sus vecinos?

{{< /collapse >}}

{{< collapse title="Tomografía de formas de onda, entre la escala local y la global" >}}

La *tomografía en caja* se basa en la hipótesis de que el campo de ondas incidente puede estimarse con suficiente precisión, ya sea a partir de un modelo 1D de referencia de la Tierra o suponiendo que las ondas incidentes se comportan como ondas planas. Esta aproximación es razonablemente válida para algunas primeras llegadas aisladas de ondas de cuerpo, como las ondas P directas, PKP o S. Sin embargo, resulta insuficiente a alta frecuencia, donde ya no puede garantizarse la coherencia del campo de ondas global.

Para superar esta limitación, propongo usar varios modelos tomográficos más realistas, como SEISGLOB2, que representan con mayor fidelidad la propagación de ondas complejas, sobre todo en regiones donde la heterogeneidad del manto influye fuertemente en las fases observadas. Para restringir mejor las incertidumbres, utilizaré varios modelos obtenidos de distintos observables, como las ondas superficiales o los tiempos de llegada de las ondas de cuerpo.

Así actualizaré mi método de tomografía en caja teniendo en cuenta las heterogeneidades más allá de la región de interés. Aunque ya se han realizado pruebas sintéticas en un marco cartesiano, su aplicación en sismología global será una primicia. Esta nueva versión requiere solvers capaces de modelizar medios 3D en dos dominios anidados (global y local), lo que motivó el desarrollo de `flexOPT.jl`.

En particular, exploraré fases que permitan obtener la imagen de la región desde la base del manto hasta la superficie de la placa de las Carolinas, para `Vs`, `Qs`, `Vp`, `Qp` y, en una segunda etapa, la anisotropía. Esto ayudará a comprender la dinámica de la pluma cuya imagen obtuve, desde la base del manto hasta el manto superior. La región bajo la microplaca de las Carolinas podría ofrecer un escenario nunca antes observado, exótico desde el punto de vista geodinámico, en el borde de la LLVP hawaiana.

Tengo previsto aplicar este método a otras regiones geodinámicamente activas, en particular el manto superior y la zona de transición bajo Japón, La Reunión y la meseta tibetana.

Usando los modelos globales para afinar la imagen local en las cajas, podremos mejorar paso a paso la resolución de la Tierra profunda. Sin embargo, es bien sabido que la inversión de formas de onda sufre más la falta de unicidad y la no linealidad que la inversión de atributos secundarios como la dispersión de ondas superficiales o los tiempos de llegada. Por eso es crucial partir de modelos iniciales realistas. Seguiré además interpretando los modelos tomográficos con petrólogos, para traducirlos en parámetros fisicoquímicos más pertinentes para restringir la dinámica del manto.

{{< /collapse >}}

{{< collapse title="Tomografía de las oscilaciones de neutrinos" >}}

Recientemente, los físicos de altas energías han empezado a interesarse por el uso de las oscilaciones de los neutrinos que atraviesan el interior de la Tierra para obtener la imagen de su estructura. Desde 2022, junto con Véronique Van Elewyck, codirigimos a dos posdocs y trabajamos en la formalización del problema inverso asociado a este tipo de datos. Evaluamos la sensibilidad de estas observaciones a las estructuras internas de la Tierra.

Los neutrinos se producen en la atmósfera por la interacción de los rayos cósmicos con las partículas atmosféricas y luego atraviesan la Tierra. Su interacción con la materia es extremadamente débil, pero al propagarse, a una velocidad cercana a la de la luz, pueden cambiar de sabor mediante un mecanismo de oscilación sensible a la densidad electrónica a lo largo de su trayectoria. Como el hidrógeno-1 es prácticamente el único átomo sin neutrones, estas observaciones podrían restringir indirectamente el contenido de agua del interior de la Tierra, aunque la resolución espacial se limita a escalas superiores a 1000 km.

Utilizamos el código EarthProb, una versión especializada del software OscProb, para simular estas oscilaciones de sabor. Estoy integrando este código en el entorno de modelización e inversión `flexOPT.jl` para poder explorar configuraciones inversas más flexibles.

Además, la próxima llegada de Hyper-Kamiokande, un observatorio de neutrinos de nueva generación cuya puesta en marcha está prevista en Japón en 2027, debería mejorar considerablemente la resolución y el rango de energías detectables. Este nuevo instrumento podría transformar profundamente nuestra capacidad de sondear el interior de la Tierra con este método.

{{< /collapse >}}

{{< collapse title="SeLFiE: Seismic and Lithological Filtering of Earth’s and planets’ models con flexOPT.jl" >}}

¿Qué pasaría si pudiéramos obtener imágenes del interior de la Tierra con una resolución de unos pocos centímetros? ¿Sería una victoria definitiva? Aunque logremos restringir mejor la dinámica interna mediante la inversión de datos geofísicos, comprender la evolución de la Tierra profunda es un problema inverso completamente distinto, esta vez con parámetros casi ilimitados.

Uno de los grandes debates persistentes en geodinámica se refiere al origen de las LLVP: ¿son de origen puramente térmico o termoquímico? Dicho de otro modo, ¿la convección del manto es solo térmica, o la química desempeña en ella un papel esencial? Para zanjar este tipo de preguntas, el problema inverso se reformula como un problema de clasificación.

En este contexto, resulta pertinente examinar directamente los datos sísmicos observados, comparados con los predichos por modelos geodinámicos. Concretamente, esto implica una modelización en cadena desde la geodinámica hasta la simulación de las formas de onda. Bauticé este proceso como *SeLFiE*: **Se**ismic and **L**ithological **Fi**ltering of **E**arth’s (and planets’) models. Se trata de comparar las señales sísmicas generadas a partir de instantáneas de modelos numéricos de la Tierra con las de la Tierra real, como si nos hiciéramos un *selfie* del interior de nuestro planeta.

Ya dispongo de varias colecciones de modelos globales de convección térmica 2D y 3D, y recientemente integré en `flexOPT.jl` funciones para leerlos. Esto permite visualizar los campos térmicos y químicos, incluida la circulación del agua en el manto o el ascenso de hierro desde su base.

Después traducimos estos modelos en parámetros físicos pertinentes para la propagación de las ondas sísmicas —densidad, velocidades `Vp` y `Vs`, anisotropía, atenuación— a partir de las fases *in situ*, en colaboración con petrólogos. Esta conversión tiene en cuenta las incertidumbres mediante tablas de correspondencia (*look-up tables*).

A partir de estos modelos generamos sismogramas sintéticos, de los que extraemos atributos (*features*) de forma de onda para una clasificación o un aprendizaje supervisado con inteligencia artificial. Los códigos, disponibles en Python, podrán integrarse en el ecosistema Julia.

{{< /collapse >}}

{{< collapse title="Monte Fuji – un nuevo laboratorio natural" >}}

Desde una pasantía de M2 que codirigí con Yosuke Aoki en 2022, me intereso por la estructura y la actividad sísmica del monte Fuji. Contrariamente a lo que podría pensarse, el monte Fuji no recibe la atención que merece. En Japón se vigilan más de 100 volcanes activos por sus frecuentes erupciones, mientras que el Fuji no ha entrado en erupción desde hace más de 300 años. Esta inactividad dificulta su estudio para los vulcanólogos, pero no para los sismólogos.

Después obtuve una beca de doctorado CNRS-MITI para Hesaneh Mohammadi, codirigida por Stéphanie Durand y por mí. El proyecto trata de la imagen sismológica 3D y 4D del monte Fuji. Prevemos realizar una *tomografía en caja* a muy alta frecuencia (> 2 Hz) para obtener la imagen de los primeros 50 km bajo el volcán. En este enfoque, los modelos 1D o tomográficos estándar ya no sirven para calcular los campos de ondas exteriores a la caja. Propongo, por tanto, evaluar la validez de la aproximación de onda plana para llegadas aisladas como las ondas P y S. Superada esta etapa, intentaremos retropropagar las formas de onda de los sismos de baja frecuencia (LFE) bajo el volcán.

Paralelamente se lanzó un proyecto con Béatrice Puyssegur y Manon Dalaison en el marco del doctorado de Lorette Drique, que busca desarrollar herramientas para atenuar los errores de las imágenes InSAR debidos a la vegetación. Aunque el tema no está directamente ligado al Fuji, prevemos aplicar estos métodos durante el tercer año del doctorado para analizar posibles deformaciones de la región que rodea al volcán.

{{< /collapse >}}

{{< collapse title="Planetología con sismología: InSight / FSS" >}}

![SeLFiE planetología](/images/optiSeLFiE_schema.jpg)

Extensión de la metodología *SeLFiE* a la planetología, para distinguir escenarios de evolución termoquímica de la Tierra, Marte y la Luna a partir de modelos numéricos y de atributos extraídos mediante inteligencia artificial o ciencia ciudadana.

Sigo trabajando ocasionalmente con datos marcianos de InSight en algunos proyectos. En el proyecto FSS (*FarSide Suite*) en la Luna, en 2026, seré colaborador científico y artístico.

Propondremos el método de filtrado *SeLFiE* para tres cuerpos telúricos. Reuniremos escenarios 1D, 2D y 3D de enfriamiento del océano de magma y de convección del manto para la Tierra, Marte y la Luna, basados en observaciones geofísicas, geoquímicas y petrológicas. Después construiremos, numéricamente mediante simulaciones de convección o de forma conceptual, modelos planetarios actuales, prestando especial atención a la geometría de las capas parcialmente fundidas o de las plumas en la base del manto.

Convertiremos estos modelos en parámetros viscoelásticos para simular las ondas sísmicas en distintos escenarios y calcular con `flexOPT.jl` núcleos de sensibilidad que permitan predecir las fases sensibles a la estructura de la base del manto.

Compararemos los datos sismológicos sintéticos, que contienen información sobre la base del manto de los tres cuerpos telúricos, con los datos observados. Esto nos permitirá evaluar la pertinencia de los modelos propuestos y afinar nuestra comprensión de estas estructuras profundas.

Luego clasificaremos los datos según los escenarios con inteligencia artificial, maximizando la capacidad de distinguir los distintos escenarios de formación del manto.

Paralelamente organizaremos una exposición de divulgación científica centrada en la escucha de sonidos —conciertos de divulgación y sesiones de escucha de datos sintéticos y observados— basándonos en la psicología del control cognitivo, y también para enriquecer nuestra investigación con los datos recogidos entre el gran público.

{{< /collapse >}}
