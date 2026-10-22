+++
title = "Investigação"
draft = false
+++

Da tomografia global e regional à reconciliação das escalas graças a restrições mineralógicas, petrológicas e geodinâmicas, com a plataforma única `flexOPT.jl`

{{< collapse title="Introdução geral" >}}

O meu projeto de investigação tem como objetivo restringir melhor a evolução do interior dos corpos telúricos a partir da análise de dados (geo)físicos, em particular das formas de onda sísmicas.

Ao longo do tempo, desenvolvi métodos numéricos e teóricos de inversão de formas de onda, tendo em conta as propriedades elásticas e viscoelásticas dos meios, a diferentes escalas, e apliquei-os a dados reais.

Uma das minhas principais contribuições é o desenvolvimento da chamada *tomografia em caixa* (*box tomography*) a várias escalas, que permite obter imagens de uma região localizada (ou «caixa») a partir de formas de onda sísmicas que amostram não só o interior dessa região, mas também o seu exterior.

Começo por apresentar os financiamentos que tornaram possível a minha investigação. Ilustro depois uma série de trabalhos de imagiologia elástica e anelástica sobre a microdinâmica sob a placa Carolina, realizados com geodinamicistas e petrólogos. Formulo em seguida questões sobre os métodos, resultados e interpretações. Descrevo depois a caixa de ferramentas teóricas e numéricas que desenvolvi para responder a problemas científicos variados. Por fim, descrevo o projeto de investigação que desejo levar a cabo com os meus parceiros atuais e futuros.

![Esquema da tomografia em caixa](/images/schema_box.png)

*
Exemplos de aplicações da tomografia em caixa a diferentes escalas:
(a) em sismologia global, utilização de sismos telessísmicos para obter imagens de regiões localizadas;  
(b) sob a placa Carolina, inversão de formas de onda 1D e 3D para `Vs` e `Qs`;  
(c) inversão 1D e 3D para `Vs` na LLVP sob o Havai;  
(d) abertura à imagiologia por neutrinos;  
(e) restrições à ascensão de fusão parcial sob a Reunião;  
(f) imagiologia 3D de `Vp`, `Vs` e densidade sob o planalto do Tibete, recentemente alargada ao Monte Fuji.
*
{{< /collapse >}}

{{< collapse title="Financiamentos obtidos" >}}

Dois terços do meu doutoramento foram financiados pela JSPS (Sociedade Japonesa para a Promoção da Ciência). No Japão, até ao início dos anos 2010, os doutorandos não tinham sistematicamente financiamento. Tive por isso de redigir o meu próprio projeto, centrado no desenvolvimento da inversão de formas de onda para a elasticidade e a anelasticidade, o que me deu cedo um olhar crítico sobre a redação de projetos científicos.

Entre 2012 e 2017, fui colaborador e principal responsável pelo ensino no consórcio GPX, dedicado à geofísica de exploração. Este consórcio promoveu a investigação e a formação, ligando universidades e indústria. Os meus trabalhos teóricos sobre a inversão localizada de formas de onda e o desenvolvimento fundamental do cálculo de sismogramas sintéticos lançaram as bases do meu novo método atual: os *operadores ótimos para equações às derivadas parciais arbitrárias*.

Contribuí depois para os estudos preparatórios do sismómetro da missão InSight em Marte, o que me levou à primeira determinação de mecanismos focais em Marte com os meus métodos de inversão.

Paralelamente, obtive vários financiamentos para organizar workshops internacionais, que deram origem a colaborações duradouras. Graças à minha estreita colaboração com Frédéric Deschamps (Academia Sinica), participei em vários projetos franco-taiwaneses, nos quais desenvolvi a série de estudos de imagiologia sismo-petrológica descrita abaixo. Esta parceria permitiu-me orientar a minha primeira doutoranda oficial, S.-T. Lai, no âmbito do concurso MOPGA (*Make Our Planet Great Again*).

Desde 2022, sou membro júnior do Institut universitaire de France (IUF) em mediação científica, o que me permite dedicar tempo tanto à investigação como à divulgação junto do grande público.

Obtive recentemente vários financiamentos de doutoramento, nomeadamente sobre a caracterização do Monte Fuji. Iniciou-se também uma estreita colaboração com Véronique Van Elewyck, com quem obtivemos duas bolsas de pós-doutoramento em tomografia de neutrinos para a imagiologia da Terra profunda a partir de observáveis geofísicos.

{{< /collapse >}}


{{< collapse title="Balanço: microdinâmica do manto sob a placa Carolina" >}}

![Esquema da placa Carolina](/images/caro_schema.jpg)

Esquema simplificado de uma série de estudos tomográficos do manto sob a placa Carolina. As nossas imagens, combinadas com previsões petrológicas, sugerem que uma pluma mantélica profunda, junto ao limite da LLVP do Pacífico/Havai, poderá arrastar ferro desde o limite núcleo-manto. Na zona de transição acima, identifica-se uma pluma mais superficial, que alimenta a dorsal de Eauripik e poderá contribuir para a dinâmica rápida da microplaca Carolina.

Nesta secção, apresento brevemente os meus estudos baseados na inversão de formas de onda que desenvolvi ao longo da carreira, limitando-me à série de estudos tomográficos do manto superior e inferior sob a placa Carolina. Em cima, esta microplaca está rodeada de grandes placas antigas, enquanto, na base do manto, a região corresponde a uma zona de baixa velocidade das ondas de corte (LLVP) sob o Havai. Obtivemos a imagem de uma pequena pluma vinda do fundo do manto, provavelmente rica em ferro, que talvez suba até alimentar a dorsal da placa Carolina, empurrando a microplaca para sul a grande velocidade, o que conduz a um regime de subducção do tipo *roll-over*.

### A placa Carolina

A placa Carolina apresenta um contexto geodinâmico particularmente complexo: enquadrada pelas placas australiana, filipina e do Pacífico, situa-se numa zona de convergência rápida, marcada por subducções ativas e antigas, margens transformantes, rifts abandonados e uma atividade vulcânica sustentada. Uma estrutura importante, a dorsal de Eauripik, perturba o centro da placa e constitui uma anomalia topográfica e magmática notável, interpretada quer como uma antiga dorsal morta, quer como o rasto de uma pluma profunda ou de um ponto quente.

A geometria das anomalias magnéticas, a batimetria e estruturas como a fossa de Sorol ou as fossas da Nova Guiné revelam uma dinâmica ainda mal compreendida, possivelmente ligada a uma ascensão mantélica profunda a partir do limite núcleo-manto.

### Estrutura profunda e pluma da Carolina

Realizámos uma série de estudos de imagiologia sísmica nesta região com o método de inversão de formas de onda que desenvolvi durante o doutoramento e o pós-doutoramento. Esta abordagem permite obter imagens de alta resolução da velocidade de corte `Vs` e do fator de qualidade `Qs`, particularmente sensíveis aos contrastes térmicos. Com dados da rede japonesa F-net, para sismos profundos nas regiões de Tonga e Fiji, evidenciámos uma anomalia marcada e localizada de `Vs` e `Qs`, centrada sob a pluma da Carolina.

A interpretação sugere um excesso de temperatura localizado de cerca de 100 K na LLVP do Pacífico, bem como uma possível contribuição de material enriquecido em ferro na pluma, incompatível com um modelo puramente térmico. A análise foi alargada a outras regiões do Pacífico para confirmar o caráter localizado destas anomalias. A modelação geodinâmica e mineralógica indica uma possível interação com o limite núcleo-manto ao longo de várias centenas de quilómetros de altura.

### Estrutura da zona de transição e do manto superior

Por fim, realizámos uma inversão de Monte Carlo dos tempos de chegada de várias fases para restringir a estrutura da zona de transição do manto sob a placa Carolina. O modelo final, baseado em conjuntos de dados SS e em modelação de formas de onda, revela uma velocidade de corte anormalmente elevada em todo o manto superior. Após várias simulações geodinâmicas, concluímos que o nosso modelo sísmico indica a possibilidade de subducções de placa do tipo *roll-over* a partir do limite sul e, eventualmente, também do limite norte, bem como anomalias de baixa velocidade em forma de pluma que se estendem até pelo menos 800 km de profundidade sob a placa Carolina. As simulações mostram ainda que a subducção *roll-over* requer uma velocidade de empurrão da placa relativamente rápida.

{{< /collapse >}}

{{< collapse title="Questões em aberto" >}}

Embora esta abordagem de imagiologia localizada, a *tomografia em caixa*, tenha permitido esclarecer algumas regiões críticas para a compreensão da dinâmica do manto, muitos pontos ainda precisam de ser melhorados ou esclarecidos, tanto do ponto de vista científico como técnico.

Um dos principais obstáculos desta metodologia reside na negligência das heterogeneidades situadas fora da caixa. Até agora, usámos apenas modelos esféricos 1D para simular o campo de ondas, tanto no cálculo das derivadas parciais das formas de onda como na reconstrução do campo de ondas nos limites da caixa. Avaliámos a propagação de erros ligada a esta aproximação num quadro cartesiano, mas a falta de um tratamento rigoroso dos efeitos exteriores continua a ser uma limitação importante a encarar mais seriamente no futuro. O acoplamento entre o método dos elementos espectrais e o meu método DSM, embora promissor, continua muito dispendioso. É, entre outras razões, para responder a este desafio que empreendi recentemente uma reorganização completa da minha caixa de ferramentas numéricas.

Além disso, quanto à ascensão da pluma mantélica da Carolina, falta obter imagens da porção do manto entre 800 km e 2500 km de profundidade, para verificar a eventual continuidade da coluna da pluma desde o limite núcleo-manto até à superfície. Exceto nos estudos que fizemos sobre a base da pluma, ainda não tivemos ocasião de interpretar quantitativamente os modelos tomográficos obtidos, que por enquanto só estão expressos em parâmetros sismológicos como `Vs` e `Qs`. É agora essencial colaborar com petrólogos, geoquímicos e geodinamicistas para melhor interpretar e valorizar as estruturas reveladas pela sismologia. Nesta perspetiva, proponho uma abordagem inovadora de filtragem sísmica, a que chamei *SeLFiE*.

{{< /collapse >}}

{{< collapse title="Ferramentas numéricas e teóricas" >}}

![Códigos e flexOPT](/images/codes.jpg)

Estado dos meus códigos até 2023 (esquerda) e desenvolvimento recente do `flexOPT.jl` (direita). A figura resume a evolução das minhas ferramentas, desde os desenvolvimentos históricos em Fortran até ao metaprograma genérico em Julia, capaz de derivar automaticamente operadores ótimos para EDP arbitrárias.

O que distingue a minha abordagem da de outros sismólogos é que me interesso pela dinâmica do manto e pelo papel dos processos químicos nessa dinâmica, sendo ao mesmo tempo programador de esquemas numéricos, tanto para a inversão como para a modelação direta. Analiso os dados ao mesmo tempo que concebo as ferramentas teóricas e numéricas para os interpretar.

Desde o doutoramento, desenvolvi numerosos códigos baseados no Direct Solution Method (DSM) no domínio da frequência para planetas esféricos, bem como no método das diferenças finitas no domínio do tempo com operadores modificados. Ambas as abordagens assentam numa base teórica comum: os operadores ótimos. Dediquei uma parte importante do meu trabalho à implementação numérica desta teoria, desenvolvendo códigos específicos.

Os operadores ótimos são operadores compactos que atingem uma precisão superior à dos operadores convencionais com o mesmo número de pontos no espaço e no tempo. No entanto, o método geral para os derivar nunca tinha sido formulado de forma sistemática. Eu próprio contribuí para a otimização dos operadores para elementos espectrais, sem imaginar que uma receita geral estivesse ao nosso alcance.

A maioria destes códigos estava escrita em Fortran, o que se revelou difícil de manter: um código para cada objetivo, com uma depuração longa e fastidiosa. Decidi por isso recomeçar do zero e conceber um metaprograma único, capaz de cobrir muitos casos de uso. A linguagem *Julia* impôs-se como escolha natural, graças às suas capacidades de metaprogramação e de manipulação simbólica e à sua integração fluida com ferramentas modernas como MPI ou GPU.

Trabalhando neste projeto com Thibault Duretz, que me sugeriu várias equações de teste e pistas de otimização do código, pude formalizar um método geral para derivar automaticamente operadores ótimos para equações às derivadas parciais arbitrárias. Um preprint que apresenta esta abordagem foi submetido à *Computer Methods in Applied Mechanics and Engineering*.

Paralelamente aos testes e ao benchmarking, o código `flexOPT.jl` já é utilizado para resolver diversas equações às derivadas parciais, nomeadamente pela minha doutoranda Hesaneh Mohammadi num projeto de tomografia do Monte Fuji, onde é comparado com outros códigos de referência.

{{< /collapse >}}

{{< collapse title="Projeto de investigação: visão de conjunto" >}}

![Estratégia tomografia–geodinâmica–SeLFiE](/images/tomo_projet.jpg)

Esquema dos projetos de investigação que desejo realizar.  
À esquerda: melhoria da tomografia de formas de onda, da escala global à local, tendo em conta os efeitos exteriores à caixa.  
Ao centro: interpretação litológica e filtragem sismológica pela abordagem *SeLFiE*.  
À direita: modelação da convecção do manto e geração de Terras virtuais cujos observáveis sísmicos e de neutrinos podem ser calculados.

Como referido acima, vários projetos inscrevem-se naturalmente na continuidade da minha investigação. Agora que o meu projeto de modernização e democratização dos operadores ótimos chega à maturidade, é tempo de mobilizar plenamente estes resultados para revisitar dados sismológicos, mas também outros tipos de dados, a fim de responder a algumas das grandes questões das geociências: como evoluíram os planetas desde a formação do Sistema Solar, e como evoluirão no futuro? O que torna o nosso planeta tão único entre os seus vizinhos?

{{< /collapse >}}

{{< collapse title="Tomografia de formas de onda, entre as escalas local e global" >}}

A *tomografia em caixa* assenta na hipótese de que o campo de ondas incidente pode ser estimado com precisão suficiente, quer a partir de um modelo 1D de referência da Terra, quer supondo que as ondas incidentes se comportam como ondas planas. Esta aproximação é razoavelmente válida para algumas primeiras chegadas isoladas de ondas de volume, como as ondas P diretas, PKP ou S. No entanto, torna-se insuficiente a alta frequência, onde a coerência do campo de ondas global já não pode ser garantida.

Para contornar esta limitação, proponho utilizar vários modelos tomográficos mais realistas, como o SEISGLOB2, que representam mais fielmente a propagação de ondas complexas, sobretudo nas regiões onde a heterogeneidade do manto influencia fortemente as fases observadas. Para melhor restringir as incertezas, utilizarei vários modelos obtidos a partir de diferentes observáveis, como as ondas de superfície ou os tempos de chegada das ondas de volume.

Vou assim atualizar o meu método de tomografia em caixa tendo em conta as heterogeneidades para lá da região de interesse. Embora já tenham sido feitos testes sintéticos num quadro cartesiano, a aplicação deste método em sismologia global será inédita. Esta nova versão requer solvers capazes de modelar meios 3D em dois domínios encaixados (global e local), o que motivou o desenvolvimento do `flexOPT.jl`.

Vou explorar, em particular, fases que permitam obter imagens da região desde a base do manto até à superfície da placa Carolina, para `Vs`, `Qs`, `Vp`, `Qp` e, numa segunda fase, a anisotropia. Isto contribuirá para compreender a dinâmica da pluma de que obtive imagens, desde a base do manto até ao manto superior. A região sob a microplaca Carolina poderá oferecer um cenário nunca antes observado, exótico do ponto de vista geodinâmico, no limite da LLVP havaiana.

Pretendo também aplicar este método a outras regiões geodinamicamente ativas, nomeadamente o manto superior e a zona de transição sob o Japão, a Reunião e o planalto do Tibete.

Usando os modelos globais para refinar a imagem local nas caixas, poderemos fazer progredir a resolução da Terra profunda, passo a passo. É, contudo, bem sabido que a inversão de formas de onda sofre mais de não unicidade e não linearidade do que a inversão de atributos secundários como a dispersão das ondas de superfície ou os tempos de chegada. É, por isso, crucial partir de modelos iniciais realistas. Continuarei também a interpretar os modelos tomográficos com petrólogos, para os traduzir em parâmetros físico-químicos mais relevantes para restringir a dinâmica do manto.

{{< /collapse >}}

{{< collapse title="Tomografia das oscilações de neutrinos" >}}

Recentemente, os físicos de altas energias começaram a interessar-se pela utilização das oscilações dos neutrinos que atravessam o interior da Terra para obter imagens da sua estrutura. Desde 2022, em colaboração com Véronique Van Elewyck, coorientamos dois pós-doutorandos e trabalhamos na formalização do problema inverso associado a este tipo de dados. Avaliamos a sensibilidade destas observações às estruturas internas da Terra.

Os neutrinos são produzidos na atmosfera pela interação dos raios cósmicos com as partículas atmosféricas e penetram depois na Terra. A sua interação com a matéria é extremamente fraca, mas, ao propagarem-se a uma velocidade próxima da da luz, podem mudar de sabor através de um mecanismo de oscilação sensível à densidade eletrónica ao longo do trajeto. Como o hidrogénio-1 é praticamente o único átomo sem neutrões, estas observações poderão permitir restringir indiretamente o teor em água do interior da Terra, embora a resolução espacial se limite a escalas superiores a 1000 km.

Utilizamos o código EarthProb, uma versão especializada do software OscProb, para simular estas oscilações de sabor. Estou a integrar este código no ambiente de modelação e inversão `flexOPT.jl`, para poder explorar configurações inversas mais flexíveis.

Além disso, a chegada próxima do Hyper-Kamiokande, um observatório de neutrinos de nova geração cuja entrada em funcionamento está prevista no Japão em 2027, deverá melhorar consideravelmente a resolução e a gama de energias detetáveis. Este novo instrumento poderá transformar profundamente a nossa capacidade de sondar o interior da Terra por este método.

{{< /collapse >}}

{{< collapse title="SeLFiE: Seismic and Lithological Filtering of Earth’s and planets’ models com flexOPT.jl" >}}

O que aconteceria se conseguíssemos obter imagens do interior da Terra com uma resolução de alguns centímetros? Seria uma vitória definitiva? Mesmo que consigamos restringir melhor a dinâmica interna pela inversão de dados geofísicos, compreender a evolução da Terra profunda constitui um problema inverso completamente diferente, desta vez com parâmetros quase ilimitados.

Um dos grandes debates persistentes em geodinâmica diz respeito à origem das LLVP: são de origem puramente térmica ou termoquímica? Por outras palavras, a convecção do manto é apenas térmica, ou a química desempenha nela um papel essencial? Para decidir este tipo de questões, o problema inverso reformula-se como um problema de classificação.

Neste contexto, torna-se pertinente examinar diretamente os dados sísmicos observados, comparados com os previstos por modelos geodinâmicos. Concretamente, isto implica uma modelação em cadeia, da geodinâmica à simulação das formas de onda. Chamei a este processo *SeLFiE*: **Se**ismic and **L**ithological **Fi**ltering of **E**arth’s (and planets’) models. Trata-se de confrontar os sinais sísmicos gerados a partir de instantâneos de modelos numéricos da Terra com os da Terra real, como se tirássemos uma *selfie* do interior do nosso planeta.

Disponho já de várias coleções de modelos globais de convecção térmica 2D e 3D. Integrei recentemente funcionalidades para ler estes modelos no `flexOPT.jl`, o que permite visualizar os campos térmicos e químicos, incluindo a circulação da água no manto ou a ascensão de ferro a partir da sua base.

Traduzimos depois estes modelos em parâmetros físicos relevantes para a propagação das ondas sísmicas — densidade, velocidades `Vp` e `Vs`, anisotropia, atenuação — a partir das fases *in situ*, em colaboração com petrólogos. Esta conversão tem em conta as incertezas através de tabelas de correspondência (*look-up tables*).

A partir destes modelos, geramos sismogramas sintéticos, dos quais extraímos atributos (*features*) de forma de onda para uma classificação ou aprendizagem supervisionada por inteligência artificial. Os códigos, disponíveis em Python, poderão ser integrados no ecossistema Julia.

{{< /collapse >}}

{{< collapse title="Monte Fuji – novo laboratório natural" >}}

Representação das coerências temporais entre dados contínuos registados em seis estações à volta do Monte Fuji durante o ano de 2008, projetadas com *UMAP*. Esta representação permite visualizar a evolução temporal dos regimes sísmicos e identificar sinais associados a *Low Frequency Earthquakes* (LFE) e a outros eventos tectónicos.

Desde um estágio de M2 que coorientei com Yosuke Aoki em 2022, interesso-me pela estrutura e pela atividade sísmica do Monte Fuji. Ao contrário do que se poderia pensar à primeira vista, o Monte Fuji não recebe a atenção que merece. No Japão, mais de 100 vulcões ativos são vigiados devido a erupções frequentes, enquanto o Monte Fuji não tem uma erupção há mais de 300 anos. Esta inatividade torna o seu estudo mais difícil para os vulcanólogos — mas não para os sismólogos.

Com Léonard Seydoux e Jean-Philippe Métaxian, trabalhámos no desenvolvimento de um método de monitorização de dados sísmicos contínuos com aprendizagem automática, nomeadamente através do *UMAP*. Ao definir atributos de coerência entre seis estações sísmicas à volta do Monte Fuji, conseguimos classificar automaticamente os *Low Frequency Earthquakes* (LFE), bem como outros eventos sísmicos de origem tectónica.

Desde este primeiro estudo, obtive uma bolsa de doutoramento CNRS-MITI para Hesaneh Mohammadi, coorientada por Stéphanie Durand e por mim. O projeto incide sobre a imagiologia sísmica 3D e 4D do Monte Fuji. Prevemos realizar uma *tomografia em caixa* a muito alta frequência (> 2 Hz) para obter imagens dos primeiros 50 km sob o vulcão. Nesta abordagem, os modelos 1D ou tomográficos padrão deixam de ser aplicáveis para calcular os campos de ondas exteriores à caixa. Proponho, por isso, avaliar a validade da aproximação por ondas planas para chegadas isoladas, como as ondas P e S. Ultrapassada esta etapa, procuraremos retropropagar as formas de onda associadas aos LFE assim identificados.

Paralelamente, foi lançado um projeto com Béatrice Puyssegur e Manon Dalaison no âmbito do doutoramento de Lorette Drique, que visa desenvolver uma caixa de ferramentas para atenuar os erros das imagens InSAR devidos à vegetação. Embora este tema não esteja diretamente ligado ao Monte Fuji, prevemos aplicar estes métodos no terceiro ano do doutoramento para analisar eventuais deformações da região em torno do vulcão.

{{< /collapse >}}

{{< collapse title="Planetologia com sismologia: InSight / FSS" >}}

![SeLFiE planetologia](/images/optiSeLFiE_schema.jpg)

Extensão da metodologia *SeLFiE* à planetologia, para distinguir cenários de evolução termoquímica da Terra, de Marte e da Lua a partir de modelos numéricos e de atributos extraídos por inteligência artificial ou ciência cidadã.

Continuo a trabalhar ocasionalmente com dados marcianos do InSight em alguns projetos. No projeto FSS (*FarSide Suite*) na Lua, em 2026, serei colaborador científico e artístico.

Vamos propor o método de filtragem *SeLFiE* para três corpos telúricos. Recolheremos cenários 1D, 2D e 3D de arrefecimento do oceano magmático e de convecção mantélica para a Terra, Marte e a Lua, com base em observações geofísicas, geoquímicas e petrológicas. Construiremos depois, numericamente através de simulações de convecção mantélica, ou conceptualmente, modelos planetários atuais, com especial atenção à geometria das camadas parcialmente fundidas ou das plumas na base do manto.

Converteremos estes modelos em parâmetros viscoelásticos para simular as ondas sísmicas em diferentes cenários e calcular, com o `flexOPT.jl`, núcleos de sensibilidade que permitam prever as fases sensíveis à estrutura da base do manto.

Compararemos os dados sismológicos sintéticos, que contêm informação sobre a base do manto dos três corpos telúricos, com os dados observados. Isto permitir-nos-á avaliar a pertinência dos modelos propostos e refinar a nossa compreensão destas estruturas profundas.

Depois, classificaremos os dados segundo os cenários com inteligência artificial, maximizando a capacidade de distinguir os diferentes cenários de formação do manto.

Paralelamente, organizaremos uma exposição de divulgação científica centrada na escuta dos sons — concertos de divulgação e sessões de escuta de dados sintéticos e observados — recorrendo à psicologia do controlo cognitivo, e também para enriquecer a nossa investigação com os dados recolhidos junto do grande público.

{{< /collapse >}}
