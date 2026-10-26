+++
title = "Research"
draft = false
+++

From global and regional tomography to scale reconciliation through mineralogical, petrological and geodynamic constraints, with the unique platform `flexOPT.jl`

{{< collapse title="General introduction" >}}

The aim of my research is to better constrain the evolution of the interior of telluric bodies by analysing (geo)physical data, in particular seismic waveforms.

Over the years, I have developed numerical and theoretical methods for waveform inversion, taking into account the elastic and viscoelastic properties of the media at different scales, and I have applied them to real data.

One of my major contributions is the development of the so-called *box tomography* at several scales, which images a localised region (or "box") from seismic waveforms that sample not only the inside of this region but also its surroundings.

I first present the funding that made my research possible. I then illustrate a series of elastic and anelastic imaging studies on the micro-dynamics beneath the Caroline plate, carried out with geodynamicists and petrologists. Next, I raise open questions on methods, results and interpretations. I then describe the theoretical and numerical toolbox I have built over time to address a variety of scientific problems. Finally, I describe the research project I wish to lead with my current and future partners.

![Box tomography schematic](/images/schema_box.png)

*
Examples of applications of box tomography at different scales:
(a) in global seismology, teleseismic events are used to image localised regions;  
(b) beneath the Caroline plate, 1D and 3D waveform inversion for `Vs` and `Qs`;  
(c) 1D and 3D inversion for `Vs` in the LLVP beneath Hawaii;  
(d) towards neutrino imaging;  
(e) constraints on the ascent of partial melt beneath La Réunion;  
(f) 3D imaging of `Vp`, `Vs` and density beneath the Tibetan Plateau, recently extended to Mount Fuji.
*
{{< /collapse >}}

{{< collapse title="Funding" >}}

Two thirds of my PhD were funded by the JSPS (Japan Society for the Promotion of Science). In Japan, until the early 2010s, PhD students did not systematically receive funding. I therefore had to write my own research proposal, centred on developing waveform inversion for elasticity and anelasticity, which gave me early on a critical perspective on writing scientific proposals.

From 2012 to 2017, I was a collaborator and the main person in charge of teaching within the GPX consortium, dedicated to exploration geophysics. This consortium fostered research and training linking universities and industry. My theoretical work on localised waveform inversion and on the fundamentals of synthetic seismogram computation laid the groundwork for my current new method: *optimal operators for arbitrary partial differential equations*.

I then contributed to the preparatory studies for the seismometer of the InSight mission to Mars, which led me to work on the first determination of focal mechanisms on Mars with my inversion methods.

In parallel, I obtained several grants to organise international workshops, which led to lasting collaborations. Thanks to my close collaboration with Frédéric Deschamps (Academia Sinica), I took part in several French-Taiwanese projects, within which I developed the series of seismo-petrological imaging studies described below. This partnership allowed me to supervise my first official PhD student, S.-T. Lai, under the MOPGA (*Make Our Planet Great Again*) call.

Since 2022, I have been a junior member of the Institut universitaire de France (IUF) for science outreach, which allows me to devote time both to my research and to outreach for the general public.

I recently obtained several PhD grants, in particular on the characterisation of Mount Fuji. A close collaboration has also started with Véronique Van Elewyck, with whom we obtained two postdoctoral fellowships on neutrino tomography for imaging the deep Earth from geophysical observables.

{{< /collapse >}}


{{< collapse title="Results: mantle micro-dynamics beneath the Caroline plate" >}}

![Caroline schematic](/images/caro_schema.jpg)

Simplified schematic of a series of tomographic studies of the mantle beneath the Caroline plate. Our tomographic images, combined with petrological predictions, suggest that a deep mantle plume, right next to the edge of the Pacific/Hawaiian LLVP, may entrain iron from the core-mantle boundary. In the transition zone above, a shallower plume is identified, which feeds the Eauripik ridge and may contribute to the fast dynamics of the Caroline microplate.

In this section, I briefly present my studies based on the waveform inversion I have developed throughout my career, limiting myself to the series of tomographic studies of the upper and lower mantle beneath the Caroline plate. At the top, this microplate is surrounded by large old plates, while at the bottom of the mantle the region corresponds to a large low shear velocity province (LLVP) beneath Hawaii. We imaged a small plume rising from the bottom of the mantle, probably iron-rich, possibly rising all the way to feed the ridge of the Caroline plate and pushing the microplate southward at high speed, leading to a *roll-over* subduction regime.

### The Caroline plate

The Caroline plate has a particularly complex geodynamic setting: bounded by the Australian, Philippine and Pacific plates, it lies in a fast-converging zone marked by active and ancient subductions, transform margins, abandoned rifts and sustained volcanic activity. A major structure, the Eauripik ridge, disrupts the centre of the plate and forms a notable topographic and magmatic anomaly, interpreted either as an old dead ridge or as the trace of a deep plume or hotspot.

The geometry of magnetic anomalies, the bathymetry, and structures such as the Sorol trough or the New Guinea trenches point to dynamics that are still poorly understood and potentially related to deep mantle upwelling from the core-mantle boundary.

### Deep structure and the Caroline plume

We carried out a series of seismic imaging studies in this region using the waveform inversion method I developed during my PhD and postdoc. This approach images at high resolution the shear velocity `Vs` and quality factor `Qs`, which are particularly sensitive to thermal contrasts. Using data from the Japanese F-net network for deep earthquakes in the Tonga and Fiji regions, we found a marked, localised `Vs` and `Qs` anomaly centred beneath the Caroline plume.

Our interpretation suggests a localised temperature excess of about 100 K within the Pacific LLVP, as well as a possible contribution of iron-enriched material in the plume, incompatible with a purely thermal model. The analysis was extended to other Pacific regions to confirm the localised character of these anomalies. Geodynamic and mineralogical modelling indicates a possible interaction with the core-mantle boundary over several hundred kilometres in height.

### Structure of the transition zone and upper mantle

Finally, we carried out a Monte Carlo inversion of multiple-phase travel times to constrain the structure of the mantle transition zone beneath the Caroline plate. The final model, based on SS datasets and waveform modelling, reveals an anomalously high shear velocity throughout the upper mantle. After several geodynamic simulations, we concluded that our seismic model points to possible *roll-over* slab subduction from the southern and possibly the northern boundary, as well as plume-shaped low-velocity anomalies extending to at least 800 km depth beneath the Caroline plate. Our simulations further show that *roll-over* subduction requires a relatively fast plate push.

{{< /collapse >}}

{{< collapse title="Open questions" >}}

Although this localised imaging approach, *box tomography*, has shed light on some regions critical for understanding mantle dynamics, many points remain to be improved or clarified, both scientifically and technically.

One of the main bottlenecks of the methodology is that heterogeneities outside the box are neglected. So far, we have used only 1D spherical models to simulate the wavefield, both to compute waveform partial derivatives and to reconstruct the wavefield at the box boundaries. We assessed the error propagation due to this approximation in a Cartesian framework, but the lack of a rigorous treatment of external effects remains an important limitation that must be addressed more seriously in the future. Coupling the spectral-element method with my DSM method, although promising, remains very costly. This challenge is one of the reasons why I recently undertook a complete reorganisation of my numerical toolbox.

Moreover, regarding the ascent of the Caroline mantle plume, the part of the mantle between 800 and 2500 km depth remains to be imaged, in order to check whether the plume conduit is continuous from the core-mantle boundary to the surface. Apart from our studies of the base of the plume, we have not yet had the opportunity to interpret quantitatively the tomographic models obtained, which are so far expressed only in seismological parameters such as `Vs` and `Qs`. It is now essential to work with petrologists, geochemists and geodynamicists to better interpret and exploit the structures revealed by seismology. To this end, I propose an innovative seismic filtering approach called *SeLFiE*.

{{< /collapse >}}

{{< collapse title="Numerical and theoretical tools" >}}

![Codes and flexOPT](/images/codes.jpg)

State of my codes until 2023 (left) and recent development of `flexOPT.jl` (right). This figure summarises the evolution of my tools, from historical Fortran developments to the generic Julia meta-programme that automatically derives optimal operators for arbitrary PDEs.

What distinguishes my approach from that of other seismologists is that I am interested in mantle dynamics and in the role of chemical processes in it, while also developing numerical schemes, both for inversion and for forward modelling. I analyse data while designing the theoretical and numerical tools to interpret them.

Since my PhD, I have developed many codes based on the frequency-domain Direct Solution Method (DSM) for spherical planets, as well as time-domain finite-difference codes with modified operators. Both approaches rest on a common theoretical basis: optimal operators. I have devoted a large part of my work to the numerical implementation of this theory through dedicated codes.

Optimal operators are compact operators that achieve higher accuracy than conventional operators using the same number of points in space and time. However, the general method to derive them had never been formulated systematically. I myself contributed to optimising operators for spectral elements, without imagining that a general recipe would be within reach.

Most of these codes were written in Fortran, which proved hard to maintain: one code per specific purpose, with long and tedious debugging. I therefore recently decided to start from scratch and design a single meta-programme covering many use cases. *Julia* was a natural choice, thanks to its meta-programming and symbolic capabilities and its smooth integration with modern tools such as MPI or GPUs.

Working on this project with Thibault Duretz, who suggested several test equations and ways to optimise the code, I was able to formalise a general method to automatically derive optimal operators for arbitrary partial differential equations. A preprint presenting this approach has been submitted to *Computer Methods in Applied Mechanics and Engineering*.

Alongside testing and benchmarking, `flexOPT.jl` is already being used to solve various partial differential equations. In particular, my PhD student Hesaneh Mohammadi uses it in a tomography project on Mount Fuji, where it is compared with other reference codes.

{{< /collapse >}}

{{< collapse title="Research project: overview" >}}

![Tomography–geodynamics–SeLFiE strategy](/images/tomo_projet.jpg)

Schematic of the research projects I wish to carry out.  
Left: improving waveform tomography from global to local scales, accounting for effects outside the box.  
Centre: lithological interpretation and seismological filtering with the *SeLFiE* approach.  
Right: mantle convection modelling and generation of virtual Earths whose seismic and neutrino observables can be computed.

As mentioned above, several projects naturally follow from my research activities. Now that my project to modernise and democratise optimal operators is reaching maturity, it is time for me to fully mobilise these achievements to revisit seismological data, as well as other types of data, in order to address some of the big questions in geosciences: how have planets evolved since the formation of the Solar System, and how will they evolve in the future? What makes our planet so unique among its neighbours?

{{< /collapse >}}

{{< collapse title="Waveform tomography, from local to global scales and back" >}}

*Box tomography* relies on the assumption that the incident wavefield can be estimated accurately enough, either from a 1D reference Earth model or by assuming that incident waves behave as plane waves. This approximation is reasonably valid for some isolated first-arriving body waves, such as direct P, PKP or S waves. However, it becomes insufficient at high frequency, where the coherence of the global wavefield can no longer be guaranteed.

To overcome this limitation, I propose to use several more realistic tomographic models, such as SEISGLOB2, which better represent the propagation of complex waves, particularly in regions where mantle heterogeneity strongly affects the observed phases. To better constrain uncertainties, I will use several models derived from different observables, such as surface waves or body-wave travel times.

I will thus update my box tomography method to account for heterogeneities beyond the region of interest. Synthetic tests have already been performed in a Cartesian framework, but applying this method in global seismology will be a first. This new version of box tomography requires solvers able to model 3D media in two nested domains (global and local), which motivated the development of `flexOPT.jl`.

In particular, I will explore phases that image the region from the base of the mantle up to the surface of the Caroline plate, for `Vs`, `Qs`, `Vp`, `Qp` and, in a second stage, anisotropy. This will help understand the dynamics of the plume I imaged, from the base of the mantle to the upper mantle. The region beneath the Caroline microplate could offer a never-before-seen scene, exotic from a geodynamic point of view, at the edge of the Hawaiian LLVP.

I also plan to apply this method to other geodynamically active regions, notably the upper mantle and transition zone beneath Japan, La Réunion and the Tibetan Plateau.

By using global models to refine the local image inside the boxes, we will be able to improve the resolution of the deep Earth step by step. However, it is well known that waveform inversion suffers more strongly from non-uniqueness and non-linearity than the inversion of secondary attributes such as surface-wave dispersion or travel times. It is therefore crucial to start from realistic initial models. I will also continue interpreting tomographic models with petrologists, to translate them into physico-chemical parameters more relevant for constraining mantle dynamics.

{{< /collapse >}}

{{< collapse title="Neutrino oscillation tomography" >}}

Recently, high-energy physicists have become interested in using the oscillations of neutrinos crossing the Earth to image its structure. Since 2022, together with Véronique Van Elewyck, we have co-supervised two postdocs and worked on formalising the inverse problem for this type of data. We are assessing the sensitivity of these observations to the Earth's internal structure.

Neutrinos are produced in the atmosphere by the interaction of cosmic rays with atmospheric particles, and then pass through the Earth. They interact extremely weakly with matter, but as they propagate, at nearly the speed of light, they can change flavour through an oscillation mechanism sensitive to the electron density along their path. As hydrogen-1 is practically the only atom with no neutrons, these observations could indirectly constrain the water content of the Earth's interior, although spatial resolution remains limited to scales above 1000 km.

We use the EarthProb code, a specialised version of the OscProb software, to simulate these flavour oscillations. I am integrating this code into the `flexOPT.jl` modelling and inversion environment, to explore more flexible inverse configurations.

Moreover, the upcoming Hyper-Kamiokande, a next-generation neutrino observatory scheduled to start operating in Japan in 2027, should considerably improve resolution and the detectable energy range. This new instrument could profoundly transform our ability to probe the Earth's interior with this method.

{{< /collapse >}}

{{< collapse title="SeLFiE: Seismic and Lithological Filtering of Earth’s and planets’ models with flexOPT.jl" >}}

What if we could image the Earth's interior with a resolution of a few centimetres? Would that be a definitive victory? Even if we manage to better constrain internal dynamics by inverting geophysical data, understanding the evolution of the deep Earth is a completely different inverse problem, this time with almost unlimited parameters.

One of the long-standing debates in geodynamics concerns the origin of the LLVPs: are they purely thermal or thermochemical? In other words, is mantle convection purely thermal, or does chemistry play an essential role? To settle such questions, the inverse problem is reformulated as a classification problem.

In this context, it becomes relevant to examine the observed seismic data directly, compared with those predicted by geodynamic models. In practice, this means a modelling chain from geodynamics to waveform simulation. I named this process *SeLFiE*: **Se**ismic and **L**ithological **Fi**ltering of **E**arth’s (and planets’) models. The idea is to compare seismic signals generated from snapshots of numerical Earth models with those of the real Earth, as if we were taking a *selfie* of our planet's interior.

I already have several collections of 2D and 3D global thermal convection models. I recently added functions to read these models in `flexOPT.jl`, which makes it possible to visualise thermal and chemical fields, including water circulation in the mantle or the rise of iron from its base.

We then translate these models into physical parameters relevant for seismic wave propagation — density, `Vp` and `Vs` velocities, anisotropy, attenuation — from *in situ* phases, in collaboration with petrologists. This conversion accounts for uncertainties through look-up tables.

From these models we generate synthetic seismograms, from which we extract waveform features for classification or supervised learning with artificial intelligence. The codes, available in Python, can be integrated into the Julia ecosystem.

{{< /collapse >}}

{{< collapse title="Mount Fuji – a new natural laboratory" >}}

Since an M2 internship I co-supervised with Yosuke Aoki in 2022, I have been interested in the structure and seismic activity of Mount Fuji. Contrary to what one might think at first, Mount Fuji does not receive the attention it deserves. In Japan, more than 100 active volcanoes are monitored because of frequent eruptions, whereas Mount Fuji has not erupted for more than 300 years. This inactivity makes it harder to study for volcanologists — but not for seismologists.

I then obtained a CNRS-MITI PhD grant for Hesaneh Mohammadi, co-supervised by Stéphanie Durand and me. The project focuses on 3D and 4D seismic imaging of Mount Fuji. We plan to carry out very high-frequency (> 2 Hz) *box tomography* to image the first 50 km beneath the volcano. In this approach, using 1D or standard tomographic models to compute wavefields outside the box becomes inapplicable. I therefore propose to assess the validity of the plane-wave approximation for isolated arrivals such as P and S waves. Once this step is completed, we will try to back-propagate the waveforms of low-frequency earthquakes (LFE) beneath the volcano.

In parallel, a project was launched with Béatrice Puyssegur and Manon Dalaison as part of Lorette Drique's PhD. This thesis aims to develop a toolbox to mitigate errors in InSAR images caused by vegetation. Although this topic is not directly related to Mount Fuji, we plan to apply these methods during the third year of the PhD to analyse possible deformation of the region around the volcano.

{{< /collapse >}}

{{< collapse title="Planetary science with seismology: InSight / FSS" >}}

![SeLFiE planetology](/images/optiSeLFiE_schema.jpg)

Extension of the *SeLFiE* methodology to planetary science, to distinguish thermo-chemical evolution scenarios of the Earth, Mars and the Moon from numerical models and from features extracted by artificial intelligence or citizen science.

I still occasionally work on Martian InSight data for some projects. For the FSS (*FarSide Suite*) project on the Moon in 2026, I will be a scientific and artistic collaborator.

We will propose the *SeLFiE* filtering method for three telluric bodies. We will collect 1D, 2D and 3D scenarios of magma-ocean cooling and mantle convection for the Earth, Mars and the Moon, based on geophysical, geochemical and petrological observations. We will then build present-day planetary models, numerically through mantle convection simulations or conceptually, with particular emphasis on the geometry of partially molten layers or plumes at the base of the mantle.

We will convert these models into viscoelastic parameters to simulate seismic waves for different scenarios and compute sensitivity kernels predicting the phases sensitive to the structure of the base of the mantle with `flexOPT.jl`.

We will compare the synthetic seismological data, which carry information on the base of the mantle of the three telluric bodies, with the observed data. This will allow us to assess the relevance of the proposed models and refine our understanding of these deep structures.

We will then classify the data according to the scenarios with artificial intelligence, maximising the ability to distinguish the different mantle formation scenarios.

In parallel, we will organise a science outreach exhibition focused on listening to sounds — outreach concerts and listening sessions of synthetic and observed data — drawing on the psychology of cognitive control, and also to enrich our research with data collected from the general public.

{{< /collapse >}}
