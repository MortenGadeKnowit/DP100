# DP-100 Læringsplan

## Eksamensfordeling (Microsoft Learn)
| Sektion | Vægt | Status |
|---------|------|--------|
| Design and prepare a machine learning solution | 20-25% | God |
| Explore data, and run experiments | 20-25% | Middel |
| Train and deploy models | 25-30% | Svag (deployment) |
| Optimize language models for AI applications | 25-30% | Svag |

---

## Plan (10 dage, ~1-2 timer/dag)

### Fase 1: Design & Prepare (Dag 1-2)
| Dag | Emne | Notebook | Nøglebegreber |
|-----|------|----------|---------------|
| 1 | Compute + Data assets | `notebooks/01.ipynb` | AmlCompute, Data, Datastore, URI_FILE/URI_FOLDER/MLTABLE |
| 2 | Environments + Command Jobs | `notebooks/02.ipynb` | Environment (curated vs custom), command(), Input/Output |

### Fase 2: Explore data & Experiments (Dag 3-4)
| Dag | Emne | Notebook | Nøglebegreber |
|-----|------|----------|---------------|
| 3 | MLflow logging + tracking | `notebooks/03.ipynb` | log_metric, log_param, log_model, autolog, runs, experiments |
| 4 | AutoML | `notebooks/04.ipynb` | automl.classification/regression, featurization, primary_metric |

### Fase 3: Train and Deploy (Dag 5-7)
| Dag | Emne | Notebook | Nøglebegreber |
|-----|------|----------|---------------|
| 5 | Sweep Jobs + Pipelines | `notebooks/05.ipynb` | SweepJob, search_space, sampling, early_termination, @pipeline |
| 6 | Online Endpoints | `notebooks/06.ipynb` | ManagedOnlineEndpoint, ManagedOnlineDeployment, scoring_script, blue/green |
| 7 | Batch Endpoints + Model Registry | `notebooks/07.ipynb` | BatchEndpoint, BatchDeployment, Model, register_model |

### Fase 4: Optimize Language Models (Dag 8-10)
| Dag | Emne | Notebook | Nøglebegreber |
|-----|------|----------|---------------|
| 8 | Azure AI Foundry | `notebooks/08.ipynb` | Hub vs Project, AI Foundry vs AML, model catalog, deployments |
| 9 | Prompt Flow | `notebooks/09.ipynb` | Flow types (standard/chat/eval), connections, tools, deployment |
| 10 | AI Search + RAG + Responsible AI | `notebooks/10.ipynb` | Index, indexer, semantic/vector search, RAG pattern, RAI dashboard |

---

## Repo-struktur
```
notebooks/
  01.ipynb  - Compute + Data
  02.ipynb  - Environments + Command Jobs
  03.ipynb  - MLflow
  04.ipynb  - AutoML
  05.ipynb  - Sweep Jobs + Pipelines
  06.ipynb  - Online Endpoints
  07.ipynb  - Batch Endpoints + Model Registry
  08.ipynb  - Azure AI Foundry
  09.ipynb  - Prompt Flow
  10.ipynb  - AI Search + RAG + Responsible AI
src/
  train.py   - Træningsscript til jobs
  score.py   - Scoring script til online endpoint
```
