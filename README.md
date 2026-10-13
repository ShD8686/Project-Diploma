# Shaded Routing — pedestrian routes that avoid the sun

Algorithm and software system for planning pedestrian routes that take **urban shading** into account.
Given a start, a destination, a date and a time, the system builds three walking routes
(shortest, balanced, shadiest) and reports their length, share of shade and detour.

> **Status:** work in progress (bachelor thesis project, Astana IT University).
> Sections marked _(planned)_ describe the target state and are not implemented yet.

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

## Quick start _(planned)_

```bash
git clone <repo-url>
cd <repo>
docker compose -f deploy/docker-compose.yml up
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

## Author

Damir Sheneussizov — Astana IT University, Software Engineering, 3rd year.
Supervisor: Zhanna Sadirmekova.
