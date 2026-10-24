# Project management and risks

## Repository and tracker
| Item | Value |
|---|---|
| Git repository | https://github.com/ShD8686/Project-Diploma |
| Submitted version tag | `prob-period-1` |
| YouTrack project | SHADE (Shaded Routing) - TODO: add link |
| Layout | `docs/`, `shade/` (Python), `router/` (Go), `web/`, `eval/`, `deploy/`, `tests/` |
| Workflow | see `workflow.md`: task `SHADE-n`, branch `SHADE-n-description`, commit `SHADE-n: message`, pull request |

## Roles
| Role | Who | Responsibility |
|---|---|---|
| Author / developer | Damir Sheneussizov | Analysis, algorithm, code, evaluation, documentation |
| Supervisor | Zhanna Sadirmekova | Approval of thresholds and plan, review of milestones |
| Test participants | TODO: 5 people | SUS questionnaire and timed task (NFR-8) |
| Field observer | TODO | Shade field validation (M1) |

## Milestones and gates
Weeks are counted from the start of the implementation stage (TODO: map to calendar dates of the course).

| Milestone | Weeks | Gate (acceptance condition) | Requirements |
|---|---|---|---|
| M-A Data and graph | 1-3 | Pilot district in PostGIS, connectivity >= 98%, share of buildings with height computed | NFR-3, NFR-5 |
| M-B Shadow module (Python) | 3-6 | Sun position <= 1 degree; precompute of time slots; first field check (draft M1) | FR-2, NFR-2 |
| M-C Router and API (Go) | 6-9 | lambda = 0 gives the shortest path; OpenAPI valid; agreement with reference B2 | FR-3, FR-4, FR-6, FR-7 |
| M-D Web client | 9-11 | 3 scenarios from `08-prototype.md` pass a manual test | FR-1, FR-5 |
| M-E Evaluation | 11-13 | Metrics M1-M7 measured, report ready | `09-verification-plan.md` |
| M-F Defence | 14 | Thesis text, demo, reproducible repository | NFR-4 |

Dependencies: data -> shadow module -> router and API -> web client -> evaluation. Field validation and the user test do not depend on code and should be prepared early (season and weather).

## Risks
P/I = probability / impact (L low, M medium, H high), the author's estimate, reviewed at each milestone.

| ID | Risk | P/I | Response and trigger |
|---|---|---|---|
| R1 | No building heights in OSM for the pilot district of Astana | H/H | Trigger: height for < 50% of buildings. Use floors x 3 m; add heights manually for the pilot district |
| R2 | Pedestrian network incomplete or disconnected | H/H | Trigger: NFR-5 < 98%. Automated connectivity check + manual OSM fixes for the pilot district |
| R3 | Trees are not modelled (out of scope) | H/M | Recorded as a limitation (FR-9 is Won't); stated in the conclusions |
| R4 | Shadow precompute is slow | M/H | Trigger: > 30 min. Vectorise, 30-min slots, fewer dates |
| R5 | No time/weather for field validation | M/H | Start early; fallback: >= 30 points or clear photos, with a stated caveat |
| R6 | Go + Python integration and learning curve | M/M | Contract through the DB schema and OpenAPI; Go only for routing; Python reference B2 |
| R7 | Weak evidence about competitors (apps not run) | H/M | Screenshots by the author; otherwise keep levels C/D and say so explicitly |
| R8 | Scope creep (mobile app, GNSS) | H/M | FR-9 is Won't; new tasks only through the supervisor |
