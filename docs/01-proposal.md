# Project proposal

**Title:** Development of an Algorithm and Software System for Planning Pedestrian Routes Considering Urban Shading
**Author:** Damir Sheneussizov, Astana IT University, Software Engineering, 3rd year (individual project)
**Supervisor:** Zhanna Sadirmekova

## Problem statement
In the hot season, direct sunlight and UV radiation cause discomfort and health risks for pedestrians.
Popular mobile services optimise distance or time and ignore the shade cast by buildings, which depends on building
height, the date and the time of day.

## Target users
- Pedestrians in Astana: students, residents, elderly people, parents with strollers (primary users).
- External clients that call the API (apps, scripts).
- Researchers and urban planners who evaluate shade along routes.

## Aim
Develop an algorithm and a software system that generates pedestrian routes by minimising a weighted cost based on
distance and solar exposure, accounting for building-induced shading at a selected time.

## Objectives
1. Review the literature and compare existing shade-aware routing systems.
2. Collect evidence of relevance from users (survey + interviews).
3. Specify requirements with measurable acceptance criteria.
4. Design the architecture (Go routing service, Python shadow module, PostGIS, web client).
5. Implement the shadow module, router, API and web client for pilot districts of Astana.
6. Evaluate against a shortest-path baseline: shade accuracy, detour, response time.

## Expected outcomes
Open repository, REST API, web client, and an evaluation report. Targets (to be approved by the supervisor, not yet measured):
median reduction of sun-exposed path length >= 20% at lambda = 0.7, median detour <= 15% (max <= 30%),
shade accuracy >= 85% against field observations, p95 response time <= 2 s.

## Scope
**In scope:** selected districts of Astana; shade from buildings (footprints + heights from OSM / open data);
selected date and time; three route modes (shortest, balanced, shadiest); user-set shade priority lambda and detour limit.
**Out of scope (MVP):** tree shadows, weather and clouds, reflected radiation, wind, mobile app, real-time GNSS navigation.

## Complexity
Time-dependent edge costs from solar geometry, a custom router with a detour constraint, an offline-precompute pipeline,
data-quality handling (building heights, pedestrian graph connectivity) and quantitative field validation.

## Cost function
`w(e, t) = l(e) * [ (1 - lambda) + lambda * s(e, t) ]`, where `l(e)` is edge length and `s(e, t)` is the sun fraction
of the edge at slot `t`. lambda = 0 gives the shortest path; lambda = 1 minimises length walked in the sun.
