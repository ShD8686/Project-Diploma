# Shaded Routing — pedestrian routes that avoid the sun

Algorithm and software system for planning pedestrian routes that take **urban shading** into account.
Given a start, a destination, a date and a time, the system builds three walking routes
(shortest, balanced, shadiest) and reports their length, share of shade and detour.

> **Status (prob-period-1, 24 Oct 2026):** analysis, design and planning are done; implementation starts next.
> Sections marked _(planned)_ describe the target state and are not implemented yet.

## Project at a glance

| | |
|---|---|
| **Problem** | Heat and UV make walking uncomfortable; map services ignore the shade cast by buildings |
| **Target users** | Pedestrians in Astana (students, residents, elderly, parents with strollers); external API clients; researchers / planners |
| **Expected outcomes** | Open repo, REST API, web client, evaluation report (shade accuracy, detour, response time vs a shortest-path baseline) |
| **Scope** | Selected districts of Astana; building shade only; date and time selectable. Out of scope: trees, weather, wind, mobile app, GNSS |
| **Team** | Damir Sheneussizov — all work (analysis, algorithm, Go + Python implementation, evaluation, documentation) |
| **Supervisor** | Zhanna Sadirmekova |
| **Technologies** | Go, Python (Shapely, pvlib), PostgreSQL + PostGIS, MapLibre GL JS, Docker Compose, REST/GeoJSON |
| **YouTrack** | Project SHADE (TODO: add link) |
| **Documentation** | [`docs/`](docs/) — see the index below |

## Documentation index

| # | Document |
|---|---|
| 1 | [Project proposal](docs/01-proposal.md) |
| 2 | [Evidence of relevance](docs/02-relevance-evidence.md) · [survey](docs/survey/survey-en.md) |
| 3 | [Literature review](docs/03-literature-review.md) |
| 4 | [Existing systems comparison](docs/04-existing-systems-comparison.md) |
| 5 | [Technology comparison](docs/05-technology-comparison.md) |
| 6 | [Requirements and acceptance criteria](docs/06-requirements.md) |
| 7 | [Architecture and diagrams](docs/07-architecture.md) (editable sources in `docs/diagrams/source/`) |
| 8 | [UX / prototype](docs/08-prototype.md) |
| 9 | [Verification and evaluation plan](docs/09-verification-plan.md) |
| 10 | [Project management and risks](docs/10-project-management.md) |
| 11 | [Supervisor feedback](docs/11-supervisor-feedback.md) |
| – | [Git/YouTrack workflow](docs/workflow.md) |

## Why

In hot weather, direct sunlight causes discomfort and health risks for pedestrians.
Popular map services optimise distance or time and ignore shade cast by buildings, which depends on
building height, the date and the time of day. Existing shade-aware routers either have no interface,
cover a single campus, precompute only a few moments, or are closed. This project aims to combine
time-dependent shade, a user-set shade weight, open code with an API, and quantitative evaluation.

## How it works

Each walkable edge `e` gets a sun fraction `s(e, t)` for a time slot `t` (0 = full shade, 1 = full sun).
The routing cost is

```
w(e, t) = ℓ(e) · [ (1 − λ) + λ · s(e, t) ]
```

where `ℓ(e)` is the edge length and `λ ∈ [0, 1]` is the shade priority.
`λ = 0` gives the shortest path; `λ = 1` minimises the length walked in the sun.
An optional detour limit (default +30 % over the shortest path) keeps routes reasonable.

**Scope of the MVP:** selected districts of Astana; shade from buildings only (footprints + heights);
no trees, weather, reflected radiation or wind.

## Architecture

```
OSM / building heights ──► Python loader ──► PostgreSQL + PostGIS ◄── Python shadow module (offline precompute)
                                                   │
                                                   ▼  load at start
Web client (MapLibre) ──REST/GeoJSON──► Go router + API (graph and weights in memory)
Evaluation scripts ────REST──────────►
```

| Component | Tech | Role |
|---|---|---|
| `router/` | Go | REST API, in-memory graph, Dijkstra/A* with `w(e, t)` |
| `shade/` | Python (Shapely, pvlib) | Sun position, building shadows, `edge_shade` per time slot |
| `web/` | MapLibre GL JS | Map UI: points, date/time, λ slider, three route variants |
| `eval/` | Python | Baseline comparison and metrics |
| `deploy/` | Docker Compose | PostGIS + services |
| `docs/` | Markdown, diagrams | Requirements, architecture, evaluation plan |

## Repository layout

```
.
├── docs/        # requirements, diagrams, evaluation plan
├── shade/       # Python: OSM/height loader, shadow computation
├── router/      # Go: routing service and REST API
├── web/         # browser client
├── eval/        # evaluation scripts and field-validation data
├── deploy/      # docker-compose.yml, DB init
└── README.md
```

## Setup, run and test _(planned, no runnable code yet)_

```bash
git clone <repo-url>
cd <repo>
cp .env.example .env            # fill in placeholder values
docker compose -f deploy/docker-compose.yml up
# tests: go test ./router/...   and   pytest shade/ tests/
```

Target: a clean machine reaches a working demo in ≤ 30 minutes following this README.

## API _(planned)_

`POST /route`

```json
{
  "from": {"lat": 0.0, "lon": 0.0},
  "to":   {"lat": 0.0, "lon": 0.0},
  "datetime": "2026-07-15T15:00:00+05:00",
  "lambda": 0.7,
  "max_detour_pct": 30
}
```

Response: GeoJSON `FeatureCollection` with three features (`shortest`, `balanced`, `shadiest`);
each has `length_m`, `shaded_share`, `detour_pct` in `properties`.
Also: `GET /shade?bbox=…&datetime=…` (shade on edges in a map window) and `GET /health`.
Errors: `422` validation, `404` point outside coverage. The OpenAPI schema will live in `docs/`.

## Evaluation _(planned)_

Baseline: shortest path (λ = 0) on the same graph; a reference implementation in Python (NetworkX/OSMnx)
checks the Go router. Metrics: shade accuracy against field observations, reduction of sun-exposed
length, detour, response time (p95), graph connectivity, sun-position error, usability (SUS).
Targets are listed in `docs/`.

## Data and licences

Only open data is used: OpenStreetMap (© OpenStreetMap contributors, ODbL) and, where available,
open building-height data for Astana. Attribution is shown in the client.
Code licence: **TODO** (MIT is planned).

## Roadmap

- [ ] A. Data and graph for the pilot district
- [ ] B. Shadow module (Python), first field check
- [ ] C. Router and API (Go)
- [ ] D. Web client
- [ ] E. Evaluation
- [ ] F. Thesis defence

## Related work

CoolWalks (Wolf, Vierø, Szell), Feng et al. (SIGSPATIAL '24), HEAL / shaded.ORS (HeiGIT),
Al Shammas et al. (2023), Vartholomaios (2023), Olaverri-Monreal et al. (2016).

## Contributing workflow

Every change is tied to a YouTrack task: branch `SHADE-<n>-description`, commit `SHADE-<n>: message`, pull request with
the task link. See [`docs/workflow.md`](docs/workflow.md). Submitted versions are tagged `prob-period-1`, `prob-period-2`, `final-prob-period`.

## Author

Damir Sheneussizov — Astana IT University, Software Engineering, 3rd year. Supervisor: Zhanna Sadirmekova.
