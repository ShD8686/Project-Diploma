# Technology comparison

Choices are justified by the requirements in `06-requirements.md`. "Easy/hard" judgements are the author's engineering estimates and will be tested by the prototype.

| Decision | Alternatives | Chosen and why | Requirements |
|---|---|---|---|
| T1. Routing service | Go custom router (in-memory graph); pgRouting (SQL); openrouteservice (Java) | **Go.** Stack chosen by the author; graph in memory, Dijkstra/A*, lambda can change per request, single binary. Drawback: the router is written by us, so a Python reference (NetworkX/OSMnx) is used for correctness checks. pgRouting is the fallback; ORS rejected (heavy setup, shade weight baked into the graph at build time). | FR-3, FR-4, NFR-1 |
| T2. Shadow computation | Python: footprint projection (Shapely + pvlib); ray tracing (trimesh + Embree); raster DSM (UMEP) | **Shapely 2.5D.** Only footprints and heights are needed (scope); computation is offline, so speed is not critical. Ray tracing is kept as a cross-check. UMEP rejected: needs a DSM, LiDAR is often unavailable. | FR-2, NFR-2, NFR-7 |
| T3. Data storage | PostgreSQL + PostGIS; GeoParquet / binary files; SQLite + SpatiaLite | **PostGIS.** Shared store: Python writes `edge_shade`, Go reads it at start; spatial indexes; fallback path to pgRouting. Files are used for experiment results. | NFR-4, NFR-5 |
| T4. Component interaction | REST + GeoJSON with weights passed through the DB; gRPC between Go and Python; GraphQL | **REST/GeoJSON.** 3-4 endpoints, easy for the map and external clients, OpenAPI schema. Python and Go never call each other at runtime: Python writes weights to the DB, Go reads them, which makes testing simpler. | FR-6, NFR-4 |
| T5. Browser map | MapLibre GL JS; Leaflet; CesiumJS (3D) | **MapLibre.** Vector map, open licence, shade/sun colouring of routes. Leaflet is the fallback; Cesium is heavy for an MVP. | FR-1, FR-5 |

Open assumption: shade quality depends on building heights in OSM (`height`, `building:levels`) for Astana.
TODO: name the pilot district and compute the share of buildings with a height through Overpass.
