# Verification and evaluation plan

The aim is achieved if, on the same data, the shaded route has less path in the sun than the baseline at an acceptable detour,
and the shade calculation agrees with real observations. All thresholds are proposals to be approved by the supervisor.

## Baselines
- **B1 (main):** shortest path (lambda = 0) on the same graph. CoolWalks, Vartholomaios and Mansour use the same comparison, so results are comparable in meaning, not in numbers (different cities).
- **B2 (correctness):** the same algorithm in Python (NetworkX/OSMnx); paths of the Go router must match.
- **External system (optional):** if Astana is covered, compare the shade share of the Yandex Maps "Green" route and ours on the same pairs (manually).

## Metrics and targets
| No. | Metric | Definition | Target | Requirement |
|---|---|---|---|---|
| M1 | Shade accuracy | Share of matching shade/sun labels on control points (+ Cohen's kappa) | >= 85% | FR-2 |
| M2 | Reduction of sun-exposed length | (baseline sun-exposed length - route sun-exposed length) / baseline, median over pairs, lambda = 0.7 | >= 20% | FR-3 |
| M3 | Detour | (route length - baseline length) / baseline | median <= 15%, max <= 30% | FR-7 |
| M4 | Response time | p95 of /route | <= 2 s | NFR-1 |
| M5 | Connectivity | Share of point pairs with a route | >= 98% | NFR-5 |
| M6 | Sun position | Azimuth/elevation deviation from reference | <= 1 degree | NFR-2 |
| M7 | Usability | Task time and SUS, 5 participants | <= 60 s; SUS >= 68 | NFR-8 |

For context, CoolWalks reports that sun-exposed length falls by 20-90% while total length grows by at most 10% at alpha <= 2 (p. 11); this is a reference for M2-M3, not a commitment.

## Measurement conditions
- **Area:** pilot district of Astana (TODO: choose; TUM used 2.6 km2).
- **Time:** 3 dates (summer, spring, autumn) x 10:00, 13:00, 16:00.
- **Point pairs:** 100 random pairs with a shortest path of 500-1500 m, fixed seed.
- **Preference:** lambda in {0, 0.25, 0.5, 0.75, 1}, all pairs and times - the detour-vs-shade curve.
- **Rig:** 4 vCPU / 8 GB, PostgreSQL and the Go service in Docker; 10 parallel clients for M4.
- **Field validation (M1):** at least 60 points x 3 times of day; the observer records shade/sun and takes a time-stamped photo; predictions are computed before the comparison.

## Statistics and tests
Differences in M2-M3 between route and baseline are analysed in pairs: median, interquartile range and the Wilcoxon signed-rank test.
Tests: unit (shade, weights), integration (API + DB), system (evaluation script on 100 pairs) - all in CI on every commit, except field validation and the user test.

## Success criterion
M1-M4 are met. If M1 fails, it is a data problem (risk R1), not an algorithm problem; in that case switch to building height = floors x 3 m (as Wang & Hou do).
