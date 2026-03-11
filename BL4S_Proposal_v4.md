# BeamScan: A Particle-Beam Material Classifier: From Recycling to Heritage Science

**Team:** Álvarez Jeremías, Baraldo Vargas Paula, Blanco Tomás, Bustillo Federico, Carabajal Ricardo, Cores Fiorella, Medina Giovanini Lorenzo, Rodríguez Matías, Yallbi Maia.
**Coaches:** García Iskya, Rodríguez Agustina
**Assessed by:** Sánchez Pineda Arturo

![Team 2026](docs/figures/teamcoaches2026.png)

**Instituto San Francisco de Asís, Santa Rosa de Calamuchita, Córdoba, Argentina.**
**March 2026.**


## 1. Motivation to Participate

We are students and teachers from Instituto San Francisco de Asís in Santa Rosa de Calamuchita, Córdoba, Argentina. 2,000 years ago, the Comechingón people carved and shaped the rock of our region — and those artefacts still cannot be studied without risking damage. Today, a single piece of PVC, indistinguishable to the naked eye, can contaminate an entire recycling batch [1]. Same challenge, 2,000 years apart: characterising a material without destroying it. Particle physics offers a single answer to both: multiple Coulomb scattering reveals atomic composition through deflection angles alone. Participating in BL4S would allow us to experimentally validate this approach.

---

## 2. Experiment Idea

## The Question

Can we build a "BeamScan Atlas" — a classification chart that identifies materials by measuring how charged particles scatter through them? We aim to demonstrate this for two real-world domains in one experiment: identifying plastics for recycling quality control and classifying geological reference materials relevant to heritage science.

## The Physics

When a charged particle travels through matter at GeV-scale energies, it does not go straight — it deflects slightly each time it passes near an atomic nucleus. The cumulative effect of thousands of these tiny deflections is called multiple Coulomb scattering (MCS) [2]. The resulting angular spread θ₀ follows the Highland formula:

![Highland formula](docs/figures/Highland.png)

## Predicted Separation

Using the Highland formula with PDG radiation lengths [3], we calculated expected scattering angles at 3 GeV/c through 10 mm targets. The results split naturally into two families: Plastics (C, H, O, N — light atoms, long X₀): PE and PP sit at θ₀ ≈ 0.56 mrad, a pure carbon-hydrogen baseline. PS, PMMA and PET follow at 0.60–0.74 mrad. PVC stands apart at θ₀ ≈ 0.90 mrad — its chlorine atom (Z = 17) dramatically increases scattering. Geological materials (Si, Ca, Al, Fe): quartz, calcite, alumina and iron oxide scatter at θ₀ = 1.17–2.38 mrad, well separated from the plastics cluster. That gap is itself the scientific result: MCS naturally sorts materials by composition. Our Geant4 [4] simulations confirm that even the closest pairs (PS vs PMMA) need fewer than 2,000 events at 3σ — seconds of beam time. PVC versus PE needs only ~83 events. The full atlas requires under one hour of data.

![Discrimination matrix](docs/figures/discrimination_matrix.png)

Figure 1: Discrimination matrix. Number of events needed for 3σ separation between each material pair at 3 GeV/c, 10 mm thickness. PE/PP is the hardest pair; most cross-family separations need fewer than 100 events.

## Experimental Setup (facility-agnostic)

Our core measurement requires only four Delay Wire Chambers (DWCs) [5] and a target holder — standard equipment at all BL4S facilities:

![BeamScan experimental setup](docs/figures/setup_schematic.png)

Figure 2: Schematic representation of the BeamScan experimental setup (facility-agnostic).

Two upstream trackers measure the incoming particle direction, two downstream measure it after the target.
Subtracting the beam's natural divergence — measured in dedicated no-target runs — we extract the scattering signal from the material alone. The layout works with Delay Wire Chambers at CERN, beam telescopes at DESY [6], and the available tracking detectors at ELSA [7].

## Targets and Facility Considerations

CERN and DESY accept only non-combustible targets; ELSA permits combustible materials too. Our plan adapts accordingly: at ELSA we run the full set — plastics (PE, PP, PS, PMMA, PET, Nylon, PVC) [8] plus geological references (quartz, calcite, alumina, iron oxide) [9], including the PVC "hero result." At CERN or DESY we run geological references plus graphite and metal foils as low-Z anchors — still spanning a wide X₀ range.

## Measurement Program

![Measurement phases and goals](docs/figures/Phases_measurement_goal.png)

## The Deliverable: BeamScan Atlas

A measured classification table and plot of θ₀ (and extracted X₀) for each material. Every data point has a physical interpretation, a real-world application, and a simulation prediction to compare against. Where available, a second axis (e.g. dE/dx or calorimeter response) strengthens the classification. The atlas is a scientific result, a practical reference, and a memorable visualisation.

![Physics explanation gap](docs/figures/physics_explanation_gap.png)

Figure 3: Natural material separation and resulting scattering-angle gap. Left: Radiation length versus effective atomic number shows the clear separation between organic (low-Z) and inorganic (higher-Z) materials. Right: The corresponding scattering angles at 3 GeV/c (10 mm thickness) reveal a natural gap between the two material classes.

## Simulation and Open Science

We have built a Geant4 Monte Carlo simulation of the full experiment, published in a public GitHub repository (https://github.com/los-topos-cosmicos/beam4school-proposal/tree/main). Every figure can be reproduced by editing a simple YAML file — no C++ or Geant4 needed. Our simulations (Geant4 11.3.2, FTFP_BERT, 2,000 events per configuration) validate the Highland predictions: across 10 of 11 materials at two momenta, Geant4 consistently exceeds Highland by 12 ± 3%, attributable to nuclear elastic scattering that the analytic formula omits. The exception is Fe₂O₃, where the ratio rises to ~1.4–1.5 — directly revealing the larger hadronic cross-section of iron nuclei — itself measurable from the same setup. This offset will calibrate our analysis: comparing real data to both Highland and Geant4 will let us separate analytic approximations from genuine detector effects.

![Geant4 Highland ratio](docs/figures/geant4_highland_ratio.png)

Figure 4: Geant4/Highland ratio for all materials at 3 and 6 GeV/c. Most materials fall within the 12 ± 3% band, consistent with nuclear elastic scattering omitted by Highland. Fe₂O₃ is a clear outlier, revealing the larger hadronic cross-section of iron nuclei.


## 3. What We Hope to Take Away

We want to return to Córdoba with a validated BeamScan Atlas, the experience of running a real experiment at a world-class facility, and a story to share. If students from Argentina can use a CERN beamline to help solve recycling challenges and study their country's archaeological heritage, it shows that fundamental physics belongs to everyone. We will share our results with local cooperatives, schools, and museums — and publish everything openly so others can build on our work.


## 4. Acknowledgement

We would like to sincerely thank Arturo Sánchez Pineda (PhD in Fundamental Physics, Senior DevOps Engineer & Researcher) for his guidance and support throughout this project, and the Museo Estanislao Baños (Santa Rosa de Calamuchita) for opening their doors to our team — their collection and archive are the root of the heritage science dimension of BeamScan.


## Outreach Activity

We built a public website — [BeamScan Atlas](https://los-topos-cosmicos.github.io/beam4school-proposal/) — where anyone can see the results of our experiment: how each material produces a different scattering angle, why that happens physically, and what it means for recycling or heritage science. All the data is downloadable and open.

We also set up a GitHub repository (https://github.com/los-topos-cosmicos/beam4school-proposal/tree/main) with our Geant4 simulations, analysis scripts, raw data, and tutorials written in Spanish and English. The idea is that any student — anywhere in Latin America — can fork the repo, edit a YAML file, and get their own scattering prediction in about 30 seconds, without installing anything. We wanted it to feel like something you can actually touch.

Finally, we're organizing outreach across our community — at the municipal cooperative, the town museum, and our school. By participating in our school's science fair, we become eligible to compete at regional and national levels, so our results could reach audiences well beyond Santa Rosa de Calamuchita. In every setting, the message is the same: the physics behind our experiment can help identify a 2,000-year-old Comechingón rock and detect PVC in a recycling stream.

Fundamental physics belongs to everyone.


## Bibliography

[1] M. Paci and F. P. La Mantia,
"Influence of small amounts of polyvinylchloride on the recycling of polyethyleneterephthalate,"
*Polymer Degradation and Stability*, vol. 63, no. 1, pp. 11–14, Jan. 1999.
https://doi.org/10.1016/S0141-3910(98)00053-6

[2] D. E. Groom and S. R. Klein,
"Passage of Particles Through Matter,"
in *Review of Particle Physics 2025*, Particle Data Group, 2025.
https://pdg.lbl.gov/2025/reviews/rpp2025-rev-passage-particles-matter.pdf

[3] Particle Data Group,
"Atomic and Nuclear Properties of Materials,"
in *Review of Particle Physics*, 2025.
https://pdg.lbl.gov/2025/AtomicNuclearProperties/

[4] Geant4 Collaboration,
*Geant4 User's Guide for Application Developers*.
http://geant4.web.cern.ch/

[5] A. Adıgüzel, E. Ergenlik, S. Gürbüz, Z. İstemihan, V. E. Özcan, and G. Ünel,
"Design, simulation and construction of a delay wire chamber,"
in *AIP Conference Proceedings*, vol. 1935, 070003,
33rd International Physics Congress of the Turkish Physical Society (TPS),
Bodrum, Türkiye, 6–10 Sept. 2017.
https://doi.org/10.1063/1.5025984

[6] H. Jansen, S. Spannagel, J. Behr, *et al.*,
"Performance of the EUDET-type beam telescopes,"
*EPJ Techniques and Instrumentation*, vol. 3, 7 (2016).
https://doi.org/10.1140/epjti/s40485-016-0033-2

[7] Physikalisches Institut, Universität Bonn,
"Hadron Physics – ELSA."
https://www-elsa.physik.uni-bonn.de/Hadronenphysik/index_en.html

[8] M. Tsakona and I. Rucevska,
"Plastic Waste Background Report,"
Secretariat of the Basel Convention, Plastic Waste Partnership Working Group,
Beau Vallon, Seychelles, 2–5 Mar. 2020.
https://gridarendal-website-live.s3.amazonaws.com/production/documents/:s_document/554/original/UNEP-CHW-PWPWG.1-INF-4.English.pdf

[9] M. Okrusch and H. E. Frimmel,
*Mineralogy: An Introduction to Minerals, Rocks, and Mineral Deposits*.
Springer, 2020.
https://doi.org/10.1007/978-3-662-57316-7

<div align="center">

**Built with ❤️ in Córdoba, Argentina for CERN Beamline for Schools 2026**

🇦🇷 → 🔬 → 🌍

*¡La física fundamental es para todos!*

</div>

