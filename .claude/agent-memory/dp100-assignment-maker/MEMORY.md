# DP-100 Assignment Maker Memory

## Project structure
- Notebooks: `notebooks/01.ipynb` through `notebooks/10.ipynb`
- Training script: `src/train.py` (sklearn LogisticRegression on IBM HR attrition/churn data)
- Utility: `src/utils.py` — `init_ml_client()` reads credentials from `.env` via dotenv
- Data: `data/churn-raw.csv` (IBM HR Attrition, Kaggle: pavansubhasht/ibm-hr-analytics-attrition-dataset)
- Workspace: subscription `9bf05e2c-7ab6-4705-b7af-45b13a47bfe2`, rg `data-scientist-cert-rg`, ws `data-scientist-cert`, location `swedencentral`
- Compute: `my-cluster` (AmlCompute, STANDARD_D2S_V3, 0-4 nodes)
- Custom environment: `custom-environment` (openmpi5.0-ubuntu24.04 base + conda_dependencies.yaml)
- Data asset: `ibm-churn-file:1` (URI_FILE), `ibm-churn-folder:1` (URI_FOLDER), `ibm-churn-mltable:1` (MLTABLE)
- Datastore: `blob_training_data`, `workspaceblobstore` (default)

## CRITICAL: Student writes the code
- **Do NOT provide complete solutions in code cells.** The student explicitly requested this.
- Code cells must be mostly empty with `# TODO:` and `# HINT:` comments only.
- Only pre-fill boilerplate: imports, MLClient connection, env var loading.
- For `%%writefile` scripts: provide function signatures and docstrings, but leave bodies as TODO blocks.
- Markdown cells explain the task and expected outcome; code cells are for the student to fill in.

## Notebook conventions (confirmed from 01.ipynb and 02.ipynb)
- Language: Danish throughout (section headers, task descriptions, hints)
- Task pattern: `**Opgave:**` for task description, `*Hint:*` for hints
- Section numbering: `## 1.`, `## 2.`, etc. with short Danish title
- MLClient: always via `from src.utils import init_ml_client` + `sys.path.append("..")`
- No elaborate markdown decorators — minimal but clear
- Outputs embedded in notebook (cells show real run output)
- Bonus exercise at end (no mandatory outputs expected)
- `%%writefile` pattern used when modifying src/ scripts from the notebook

## Learning plan day-to-topic mapping
- Day 1: Compute + Data assets (01.ipynb) — AmlCompute, URI_FILE/FOLDER/MLTABLE, Datastores
- Day 2: Environments + Command Jobs (02.ipynb) — curated vs custom env, command(), Input/Output
- Day 3: MLflow logging + tracking (03.ipynb) — log_metric, log_param, log_model, autolog, runs, experiments
- Day 4: AutoML (04.ipynb) — automl.classification/regression, featurization, primary_metric
- Day 5: Sweep Jobs + Pipelines (05.ipynb) — SweepJob, search_space, sampling, early_termination, @pipeline
- Day 6: Online Endpoints (06.ipynb) — ManagedOnlineEndpoint, ManagedOnlineDeployment, scoring_script, blue/green
- Day 7: Batch Endpoints + Model Registry (07.ipynb) — BatchEndpoint, BatchDeployment, Model, register_model
- Day 8: Azure AI Foundry (08.ipynb) — Hub vs Project, model catalog, deployments
- Day 9: Prompt Flow (09.ipynb) — Flow types, connections, tools, deployment
- Day 10: AI Search + RAG + Responsible AI (10.ipynb) — Index, semantic/vector search, RAG, RAI dashboard

## Notebooks created
- 01.ipynb: Complete (compute + data assets) — student has run it
- 02.ipynb: Complete (environments + command jobs) — student has run it, train.py written
- 03.ipynb: Created 2026-02-23 — MLflow logging (10 sections + bonus)
- 04.ipynb: Created 2026-02-23 — AutoML (10 sections + bonus regression): automl.classification, featurization, primary_metric, set_limits, mlflow.pyfunc.load_model
- 05.ipynb: Created 2026-02-24 — Sweep Jobs + Pipelines (12 sections + bonus): search_space, Choice/LogUniform, sampling_algorithm, BanditPolicy, @pipeline, prep.py trin, pipeline output kobling

## SDK v2 patterns used in this project
- Always `from azure.ai.ml import MLClient, command, Input, Output`
- `from azure.ai.ml.entities import AmlCompute, Data, Environment`
- `from azure.ai.ml.constants import AssetTypes`
- `from azure.identity import DefaultAzureCredential`
- Environment reference: `"custom-environment@latest"` or `"custom-environment:2"`
- NEVER use `azureml.core` (SDK v1)

## train.py evolution
- v1 (Dag 2): basic log_metric/log_param, mlflow.sklearn.save_model
- v2 (Dag 3): wrapped in mlflow.start_run(), uses log_model instead of save_model, adds log_artifact for coef plot, run_name set dynamically
- v3 (Dag 5): adds --solver argparse argument, logs solver param, uses args.solver in LogisticRegression

## Sweep Job patterns
- Trial command: `command()` with `${{search_space.PARAM}}` placeholders in command string
- Convert to sweep: `trial_command.sweep(sampling_algorithm=..., primary_metric=..., goal=...)`
- Set limits: `sweep_job.set_limits(max_total_trials=N, max_concurrent_trials=M)`
- Early termination: `from azure.ai.ml.sweep import BanditPolicy` — NOT compatible with bayesian sampling
- Best run: `mlflow.search_runs(experiment_names=[...], order_by=[\"metrics.METRIC DESC\"])`

## Pipeline patterns
- Decorator: `from azure.ai.ml.dsl import pipeline` then `@pipeline(default_compute=..., experiment_name=...)`
- Trin kobling: `step2_input = step1.outputs.output_name`
- Returns dict: `return {\"key\": step.outputs.name}`
- Instansiér: `job = my_pipeline(arg=Input(...))` then `ml_client.jobs.create_or_update(job)`
- Sweep in pipeline: call `.sweep(...)` on a command() inside the @pipeline function body
