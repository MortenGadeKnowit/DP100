# DP-100 Student Profile — Persistent Memory

## Student Self-Assessment
- Strong: Phase 1 (Design & Prepare)
- Medium: Phase 2 (Explore Data & Experiments)
- Weak: Phase 3 (Train/Deploy) and Phase 4 (Language Models)

## Progress Through 10-Day Plan
- Day 1 (Compute, Data, Datastores): Completed — no direct evaluation yet
- Day 2 (Environments + Command Jobs): Completed — evaluated, Almost Ready
- Day 3 (MLflow logging + tracking): Completed — evaluated, Almost Ready
- Day 4 (AutoML): Completed — evaluated, Almost Ready
- Days 5-10: Not yet submitted

## Recurring Strengths
- SDK v2 syntax is fundamentally correct (command(), Input/Output, create_or_update())
- Understands curated vs. custom Environment distinction
- Good argparse/script structure — CLI args match command placeholders correctly
- Applies dual model persistence (joblib + mlflow) showing nuanced understanding
- Job completed successfully end-to-end

## Recurring Weaknesses / Watch Areas
- mlflow.start_run() in command jobs: Day 2 issue (nested run) now RESOLVED in Day 3 — student uses it correctly for run naming. Confirm understanding is solid.
- log_artifact vs log_model: RESOLVED in Day 3 — student now uses mlflow.sklearn.log_model() correctly.
- Bloated conda specs: Issue identified in Day 2 — not retested in Day 3 (environment was reused).
- Output(path=None): Day 2 issue, not retested in Day 3.
- ModelSignature in train.py: Day 3 — notebook cell-14 defines Schema/ColSpec at module level WITHOUT importing them (NameError on remote compute). The actual train.py on disk is a different/earlier version that omits the signature entirely. Student needs to reconcile these.
- log_model without signature: On-disk train.py calls mlflow.sklearn.log_model(model, artifact_path="model") with no signature= arg. Signature is best practice and enables safer deployment.
- Conceptual gap: log_model storage location — student wrote "den skriver vel til et eller andet sted?" (where does it write?). Does not yet understand MLflow artifact store backed by Azure Blob Storage behind the workspace.
- search_runs with experiment_names: Azure ML's MLflow backend does not reliably support experiment_names/experiment_ids params in search_runs() from a notebook context. Student's pandas-filter workaround is pragmatic and acceptable.
- Hardcoded experiment_id in search_runs(): Student consistently hardcodes experiment IDs instead of using mlflow.get_experiment_by_name(). Works but is fragile. Flag in Day 5+ if it recurs.
- AutoML model loading on local env: Student correctly hit the azureml.training.tabular Python 3.10 dependency wall — this is expected and student handled it well (pivot to Model registration + download_artifacts).

## Key Concepts Student Has Demonstrated Understanding Of
- Environment(image=, conda_file=) + create_or_update()
- AssetTypes.URI_FILE / URI_FOLDER
- ${{inputs.x}} / ${{outputs.y}} placeholder syntax
- ml_client.jobs.create_or_update()
- AzureML- prefix for curated environments

## Exam Areas Needing Extra Attention
- log_model vs log_artifact (Day 3/7 boundary — critical for model registry)
- Azure ML auto-managed MLflow run context in command jobs
- Minimal environment dependencies (azureml-mlflow is the key package)
- AutoML primary_metric min/max direction: student does not know this is hardcoded (not configurable)
- AutoML one-hot vs ordinal encoding: student oversimplified featurization behavior
- Incomplete inference cell in Day 4: student loaded data but never called predict() — inference pattern needs reinforcement before Day 6 (endpoints)

## Notes on Feedback Preferences
- Student writes in Danish; feedback provided in English (matching their code comments)
- Feedback should be direct and specific, not vague

See: student-day-notes.md for per-day details
