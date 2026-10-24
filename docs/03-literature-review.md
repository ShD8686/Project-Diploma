# Literature review

Requirement: critical review + structured analysis table; >= 12 sources, >= 8 scientific publications, core from the last 5 years.

Current set: 12 sources (9 journal articles, 3 conference papers; 8 published 2023-2026). See the presentation, slide "Literature review".

## Structured analysis table (TODO: complete for all 12)
| # | Source | Year | Type | Method / data | Result | Limitation relevant to this project |
|---|---|---|---|---|---|---|
| 1 | Wolf, Viero, Szell - CoolWalks | 2025 | Journal | Dijkstra, building outlines (2.5D), perceived length factor alpha | Sun-exposed length down 20-90%, total length up to +10% (alpha <= 2) | No trees; no app; fixed moments |
| 2 | Feng et al. - Walking in the Shade (SIGSPATIAL) | 2024 | Conference | LoD2 buildings + ray tracing + pgRouting | 40 000 points on 4 tiles ~ 0.4 s | 2.6 km2, manual network correction, no quality evaluation |
| 3 | Al Shammas et al. | 2023 | Journal | 2D footprint shadows, ArcGIS, weather-aware index | Comfort route per user preference | Precomputed 228 polygons; desktop only |
| 4 | Vartholomaios - Follow the shade | 2023 | Conference | UMEP raster shadows, least-cost path | Paths +19% / +9% longer, cost -35% / -11% | Raster compute is costly |
| 5 | Olaverri-Monreal et al. | 2016 | Journal | Android + OSM, sun azimuth and building side | Shaded route ~55% darker, longer (765 -> 1020 m) | Heights unknown, n = 5 |
| 6 | Wang & Hou (CAADRIA) | 2025 | Conference | Grasshopper/Ladybug, A*, four weight formulas | Four route variants | No interface, untested in the field |
| 7 | Deilami et al. | 2020 | Journal | Review + focus groups, Bendigo | 52.3% of routes poor/no shade | Qualitative, tree-focused |
| 8 | Middel & Krayenhoff | 2019 | Journal | MaRTy measurements, Tempe | T_mrt up to 76.4 C; 35-40 C spatial range | Comfort, not routing |
| 9 | Taleghani et al. | 2016 | Journal | ENVI-met micrometeorological simulation | Cool pavements can raise PET at unshaded points | Comfort, not routing |
| 10-12 | TODO | | | | | |

> Note: type/year of each entry must be verified against the PDFs before submission (e.g. CoolWalks was first an arXiv preprint in 2024).

Mini conclusion: shade, not air temperature, drives pedestrian comfort; shade-aware routing works at the cost of a longer path;
a reproducible, user-tunable system with measured accuracy, detour and delay is missing.
