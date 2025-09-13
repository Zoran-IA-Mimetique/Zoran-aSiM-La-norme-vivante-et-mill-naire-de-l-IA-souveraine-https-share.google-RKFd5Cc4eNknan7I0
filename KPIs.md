# KPIs — Cibles et mesures


| KPI | Cible | Méthode de mesure |
|---|---:|---|
| Reproductibilité (3 seeds 13/42/101) | ≥ 98 % | Variance ±2 % sur 10 runs |
| Traçabilité C2PA | 100 % | Manifeste signé par artefact |
| Overhead p95 vs baseline | ≤ +12 % | Bench reproductible `make reproduce_all` |
| Interopérabilité (connecteurs publics) | ≥ 60 % | Matrice interop.csv |
| Conformité AI Act / ISO 42001 | ≥ 65 % (audit externe) | Mapping YAML + audit log |
| Fail-rate après 3 Self-Patch | ÷2 | Logs ΔM11.3 et quorum |
| Énergie/req (proxy) | plafonds/année | energy_budget.json |
