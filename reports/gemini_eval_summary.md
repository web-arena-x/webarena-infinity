# Gemini Evaluation Results Summary

Generated: 2026-03-16

All results use the **merged/** directory (best-of-N runs). Data sourced from `s3://mirror-mirror-results/`.

## Overall Performance by Pipeline Stage

| App | Func Tasks | Real Tasks | Hardening (new) | Final Regression | Pipeline |
|:----|:----------:|:----------:|:---------------:|:----------------:|:--------:|
| clio-matters | 9/57 (15%) | 5/60 (8%) | 3/60 (5%) | 14/177 (7%) | Full |
| elation-clinical-records | 55/55 (100%) | 60/60 (100%) | 38/60 (63%) | 152/175 (86%) | Full |
| elation-patient-communication | 19/58 (32%) | 44/120 (36%) | -- | -- | P3 |
| elation-prescriptions | 49/56 (87%) | 43/60 (71%) | 39/60 (65%) | 147/176 (83%) | Full |
| figma-slides | -- | 19/60 (31%) | 4/60 (6%) | 51/181 (28%) | Full |
| figma-text-and-typography | -- | 30/60 (50%) | 10/60 (16%) | 74/185 (40%) | Full |
| gitlab-plan-and-track | 54/55 (98%) | 51/80 (63%) | -- | -- | P3 |
| gmail | 53/55 (96%) | 43/60 (71%) | -- | -- | P3 |
| gmail-accounts-and-contacts | -- | 37/60 (61%) | 32/60 (53%) | 126/188 (67%) | Full |
| handshake-career-exploration | -- | -- | 26/60 (43%) | 154/255 (60%) | Full |
| linear-account-settings-v2 | 60/60 (100%) | 88/120 (73%) | -- | -- | P3 |
| paypal-my-wallet | 54/56 (96%) | 57/60 (95%) | 50/60 (83%) | 178/196 (90%) | Full |
| shopify-web-performance | 53/55 (96%) | -- | -- | -- | P2 |
| superhuman-general | 56/60 (93%) | 39/60 (65%) | 13/40 (32%) | 104/180 (57%) | Full |
| xero-invoicing | 55/58 (94%) | 97/120 (80%) | -- | -- | P3 |
| **TOTAL** | **517/625 (82%)** | **613/980 (62%)** | **215/520 (41%)** | **1000/1713 (58%)** | |

### Column Definitions

- **Func Tasks**: Phase 2b function-task eval (last audited run before hardening)
- **Real Tasks**: Phase 3b real-task eval (last audited run before hardening)
- **Hardening**: Phase 4 newly generated harder tasks (all 3 rounds aggregated)
- **Final Regression**: Phase 5 full-suite eval (function + real + hardened tasks combined)
- **Pipeline**: Full = all 5 phases; P3 = stopped after real tasks; P2 = stopped after function tasks

## Final Regression (P5) — Func Tasks vs Real Tasks Breakdown

| App | Func Tasks (P5) | Real Tasks (P5) | Combined |
|:----|:---------------:|:---------------:|:--------:|
| clio-matters | 8/57 (14%) | 6/120 (5%) | 14/177 (7%) |
| elation-clinical-records | 54/55 (98%) | 98/120 (81%) | 152/175 (86%) |
| elation-prescriptions | 50/56 (89%) | 97/120 (80%) | 147/176 (83%) |
| figma-slides | 28/61 (45%) | 23/120 (19%) | 51/181 (28%) |
| figma-text-and-typography | 36/65 (55%) | 38/120 (31%) | 74/185 (40%) |
| gmail-accounts-and-contacts | 52/68 (76%) | 74/120 (61%) | 126/188 (67%) |
| handshake-career-exploration | 53/55 (96%) | 101/200 (50%) | 154/255 (60%) |
| paypal-my-wallet | 54/56 (96%) | 124/140 (88%) | 178/196 (90%) |
| superhuman-general | 44/60 (73%) | 60/120 (50%) | 104/180 (57%) |

## Key Findings

**Top 3 apps** (final regression): paypal-my-wallet (90%), elation-clinical-records (86%), elation-prescriptions (83%)

**Bottom 3 apps** (final regression): clio-matters (7%), figma-slides (28%), figma-text-and-typography (40%)

**Difficulty ladder**: 82% func → 62% real → 41% hardening — confirms the task progression works as intended.

**Func vs Real gap in P5**: Func tasks are consistently easier. Largest gaps: figma-slides (45% vs 19%), handshake (96% vs 50%), superhuman (73% vs 50%).

**Pipeline completion**: 9/15 apps completed full pipeline, 5 stopped at P3, 1 at P2 (shopify-web-performance).
