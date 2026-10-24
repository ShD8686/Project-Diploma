# Requirements specification

Priorities (MoSCoW): M = must, S = should, C = could, W = won't in the MVP. Numeric thresholds are proposals to be approved by the supervisor.
Every Must has a measurable acceptance criterion and a verification method.

## Functional requirements
| ID | Requirement | Priority | Acceptance criterion | Method |
|---|---|---|---|---|
| FR-1 | Choose start, destination, date and time on the map | M | Parameters go to the API without typing coordinates; 10 of 10 manual UI tests pass | UI test |
| FR-2 | Compute the sun fraction s(e,t) for every pedestrian edge and time slot (Python) | M | At least 85% agreement with field observations on at least 60 control points, 3 times of day | Field validation |
| FR-3 | Route by w = l*[(1-lambda)+lambda*s], lambda in [0,1] | M | lambda = 0 equals the shortest path in 100% of 50 pairs; at lambda = 1 the sun-exposed length is not larger than for the shortest path in 100% of pairs | Automated test |
| FR-4 | Three modes: shortest, balanced, shadiest, each with length, shade share, detour | M | All fields present; shade share equals a recount by segments within 1% | Automated test |
| FR-5 | Draw routes on the map with shade/sun colours and a comparison | M | Segments are distinguishable, legend present | Demo |
| FR-6 | REST API with an OpenAPI description (route, shade, health) | M | Schema valid; contract tests 100% | Automated test |
| FR-7 | Detour limit (maximum % over the shortest path), default +30% | S | None of 100 routes exceeds the limit | Automated test |
| FR-8 | Export route as GeoJSON/GPX | C | File opens in QGIS | Demo |
| FR-9 | Tree shadows, weather/cloud cover, mobile app, GNSS navigation | W | - | - |

## Non-functional requirements
| ID | Requirement | Priority | Acceptance criterion | Method |
|---|---|---|---|---|
| NFR-1 | Response time of /route | M | p95 <= 2 s on the pilot district, 4 vCPU / 8 GB, 10 parallel clients | Load test (k6 / Locust) |
| NFR-2 | Sun position accuracy | M | Azimuth and elevation deviate from a reference by <= 1 degree for 10 moments | Automated test |
| NFR-3 | Open data only, licences respected | M | Attribution in the client; list of sources and licences in the repository | Review |
| NFR-4 | Reproducibility | M | `docker compose up` on a clean machine following the README in <= 30 min | Manual run |
| NFR-5 | Pedestrian graph connectivity | M | >= 98% of random point pairs have a route | Automated test |
| NFR-6 | Testability | S | Core coverage (Go router, Python shadow module) >= 70% | go test / pytest-cov |
| NFR-7 | Precompute time | S | One date for the pilot district in <= 30 min (4 vCPU) | Measurement |
| NFR-8 | Usability | S | 5 users: route built in <= 60 s without hints; SUS >= 68 | Questionnaire |

## Traceability to the gap (see `04-existing-systems-comparison.md`)
Time of day -> FR-1, FR-2; user-set shade weight -> FR-3, FR-4; open code and API -> FR-6, NFR-3, NFR-4;
quantitative evaluation -> FR-2, NFR-1, NFR-2, NFR-8 (plan in `09-verification-plan.md`).
