# Workflow: YouTrack <-> Git

Project key: `SHADE` (any key is fine; examples in the course use `DIP-23`).

- **Task:** every work item is a YouTrack task with responsible student, expected outcome, acceptance criteria, deadline.
- **Branch:** `SHADE-<n>-short-description`, e.g. `SHADE-12-shadow-module`.
- **Commit:** `SHADE-12: add sun position and edge sampling` (one coherent change per commit).
- **Pull request:** explain the change, reference the task, describe how it was checked. Individual project: the supervisor reviews selected significant changes at agreed checkpoints.
- **main** is the reviewed baseline. Do not push work directly to main after the first documentation commit.
- **Link back:** paste the PR/commit link into the YouTrack task. Mark the task done only when acceptance criteria are met.
- **Tags:** `prob-period-1`, `prob-period-2`, `final-prob-period`. Never move or replace a tag already submitted.
- **Secrets:** never commit passwords, API keys, personal data. Use `.env.example` with placeholders.
