# Existing systems comparison

Five systems were selected because they implement shade- or sun-aware routing and have public information.
Google Maps is not included: the "Prefer shade" option was found only in an APK teardown and did not work (version 25.45.02, 6 Nov 2025).

**Evidence level:** A = primary artefact opened by the author (code, README); B = official project page opened, app not run;
C = peer-reviewed paper only; D = press or company claim only.

| Criterion | CoolWalks (Wolf 2025) | Cool Routes (ASU, 2026) | HEAL / shaded.ORS (HeiGIT) | Feng et al. (TUM, 2024) | Yandex Maps "Green" (2026) | This project |
|---|---|---|---|---|---|---|
| Shade source | Building outlines, one height (2.5D); no trees | Radiant-temperature forecast from buildings and trees | DSM/DTM + OSM: buildings, vegetation, covered passages | LoD2 buildings (12 281), ray tracing; no trees | Tree crowns from satellite; buildings not mentioned | Building footprints + heights (OSM); trees later |
| Time dependence | Fixed moments, 15-min step, one date | Hourly weather forecast | Precomputed: May-Aug, 4 times a day | Any date/time per request | Not disclosed | Chosen date; precomputed time slots |
| Routing and shade weight | Dijkstra; "perceived length", alpha 1.1-10 | Not described | ORS engine (GraphHopper fork); exposure index = 1 - mean shade | Dijkstra (pgRouting); w = alpha*shade + (1-alpha)*length | Not disclosed | Own Go router; w = l*[(1-lambda)+lambda*s] |
| User control | No UI | Not stated | Yes (influence factor) | Yes (slider) | No | lambda, detour limit, 3 modes |
| Delivery | Code only | Web app | Web app | Web 3D (Cesium) | Yandex Maps app | REST API + web client |
| Coverage | Parts of Manhattan, Barcelona, Valencia | ASU campus | 80 German cities | 2.6 km2, Munich | Tashkent | Astana (selected districts) |
| Openness | MIT code + data (Zenodo) | Claimed open; repository not found | Claimed open; repositories not named | Not stated | Closed | Open source (licence TBD) |
| Quality evaluation | Numeric analysis only: up to +10% length at alpha <= 2 | Claimed: 12 days of campus tests (press) | Not stated | Compute time only (40 000 points ~ 0.4 s) | ~90% crown accuracy claimed; no independent check | Shade accuracy, detour, delay |
| Evidence level | A (code opened, not run) | B | B | C | D | - |

Discrepancy to check: the mean reduction in heat load for Cool Routes is about 4.5 C in the ASU release and about 2.5 C in Techloy.
Verify against the original paper (Building and Environment) before citing.

## Gap this project addresses
- No system combines time-of-day shade, a user-set shade weight, open code with an API, and quantitative evaluation (shade accuracy, detour, delay).
- The closest analogue (TUM) works in real time, but only computation speed was evaluated.
- Open, verifiable code exists only for CoolWalks, which has no interface or service.

## Checks the author still has to do (TODO)
| System | What to do | Evidence to add |
|---|---|---|
| Cool Routes | Open coolroutes.sensableheatscapes.com, build a route, record settings, time, coverage | 2-3 screenshots in `docs/evidence/` |
| HEAL / shaded.ORS | Open shaded.openrouteservice.org, choose a city and time, check for a slider | 2-3 screenshots |
| Yandex Maps | Walking route in Astana and Tashkent, check the "Green" variant | Screenshot of the options list |
| Google Maps | Walking route settings: is there "Prefer shade"? | Screenshot of the settings |

After the screenshots, the evidence level of these rows rises to A.
