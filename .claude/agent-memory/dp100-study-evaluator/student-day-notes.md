# Per-Day Student Notes

## Day 5 — Sweep Jobs + Pipelines (Evaluated 2026-03-01)

**Verdict:** Needs More Work (sweep section: Almost Ready; pipeline section: Needs More Work)

**What was correct:**
- SweepJob submission pattern: command() -> .sweep() -> create_or_update() — correct flow
- No mlflow.start_run() in train_sweep.py sweep trial script — correct understanding that AML manages run context
- BanditPolicy instantiation and early_termination_policy= kwarg in .sweep() — correct
- ml_client.jobs.create_or_update() used correctly in cell-12 (fixed from earlier cell which used ml_client.create_or_update())
- max_total_trials + max_concurrent_trials + timeout set on sweep — correct
- pipeline @decorator pattern, chaining prep.outputs.output_data -> train input — correct
- Pipeline submitted successfully with ml_client.jobs.create_or_update()
- Reflection Q1 (sweep vs manual loop): strong — mentions early termination, Studio overview, sampling flexibility
- Reflection Q4 (separate prep step): good — reusability and modularity
- ModelSignature in train_sweep.py — correct and imports present at module level (fixed from Day 3 issue)
- log_model with signature and correct artifact_path="model" string — correct in train_sweep.py

**Bugs found in pipeline scripts — would fail on remote:**

1. CRITICAL — prep_step.py line 35: `args.model_dir` used but argument is defined as `--output_data` with `dest="output_data"`. AttributeError on remote. Should be `args.output_data`.
2. CRITICAL — train_step.py line 36: `--solver` argument has `dest="reg"` (should be `dest="solver"`) — silently overwrites args.reg with the solver string. Then `type=float` on solver means argparse tries to cast "liblinear" to float -> ValueError crash.
3. HIGH — train_step.py line 80: `mlflow.sklearn.log_model(model, artifact_path=out_dir, ...)` — artifact_path must be a string name (like "model"), not a Path object. This will either crash or produce a malformed artifact path.
4. HIGH — train_step.py line 62: `with mlflow.start_run()` inside a pipeline step script — creates a nested run inside AML's managed run context. Same pattern as Day 2 mistake. Metrics logged inside the with block will be logged to the child run, not the pipeline step's run.
5. MEDIUM — train_step.py lines 5+10: `import mlflow` appears twice (cosmetic but sloppy).
6. MEDIUM — train_step.py line 36: `default="liblinear"` on an argument declared as `type=float` — type conflict would cause a crash at parse time if the default is used.
7. NOTE: The pipeline command for train_step.py passes `--reg 0.05` but NOT `--solver`, even though solver is required=True. This means the pipeline would always crash on the solver argument.

**Conceptual gaps:**
- Intermediate data storage (Reflection Q5): Student says "stored in docker runtime" — WRONG. Correct answer: Azure Blob Storage (workspaceblobstore), auto-generated path under the pipeline job run. Student partially correct that "you control via inputs" but misses that Azure ML auto-generates intermediate paths.
- Bayesian + early termination (Reflection Q3): Student admits "I don't know." Key concept: Bayesian uses the history of previous trials to decide WHICH hyperparams to try next. Early termination kills trials before they complete. If you kill a trial early, its metric is unreliable — Bayesian can't learn from incomplete data, so its model of the search space degrades. Hence: early termination is incompatible with Bayesian sampling.
- Bayesian Q2 (partial): Correctly states Bayesian learns direction and needs continuous params. Missing: requires >= 20 trials to work well.

**Search space issue:**
- Used Choice([0.001, 0.05, 0.1]) for reg instead of LogUniform(-3, 0). This works but misses the purpose — LogUniform is appropriate for regularization which varies over orders of magnitude.

**On-disk src/train.py state:**
- Now has `with mlflow.start_run(run_name=f"sweep-lr-reg-{args.reg}")` at line 83 — this is the Day 3 anti-pattern (nested run) still present. The new train_sweep.py correctly removes this. Student created train_sweep.py as a clean copy; however train.py still has the bug.

**Key file bugs to fix before Day 6:**
- /Users/gade/Knowit/DP100/src/prep_step.py line 35: args.model_dir -> args.output_data
- /Users/gade/Knowit/DP100/src/train_step.py line 36: dest="reg" -> dest="solver", type=float -> type=str
- /Users/gade/Knowit/DP100/src/train_step.py line 80: artifact_path=out_dir -> artifact_path="model"
- /Users/gade/Knowit/DP100/src/train_step.py line 62: remove mlflow.start_run() wrapper

## Day 4 — AutoML (Evaluated 2026-02-24)

**Verdict:** Almost Ready

**What was correct:**
- Input(type=AssetTypes.MLTABLE) with azureml: path notation — correct
- automl.classification() with all required params — correct
- set_limits() / set_featurization() chained correctly on job object — correct
- ml_client.jobs.create_or_update() + stream() — correct
- search_runs() by experiment_id with pandas sort fallback — consistent pragmatic pattern
- Registered best model using Model(path=azureml://jobs/...) + AssetTypes.MLFLOW_MODEL — correct SDK v2 pattern
- download_artifacts() to inspect MLmodel/conda.yaml locally — good exploratory behavior
- Regression bonus: complete automl.regression() job including limits and featurization — excellent
- Reflection Q1 (AUC_weighted vs accuracy): correct reasoning about imbalanced data and dummy classifier risk
- Reflection Q3 (timeout vs trial_timeout): correctly explained both levels
- Reflection Q5 (manual vs AutoML): strong answer — causal inference, theoretical model choice, specific featurization

**Issues found:**
1. primary_metric="AUC_WEIGHTED" (uppercase) in cell-8, but task instructed "AUC_weighted" — SDK normalizes to lowercase on display (confirmed: output shows "auc_weighted"), so this works but is inconsistent with documentation casing. Low severity.
2. best_run_id selection: student uses iloc[1,0] (second-best trial) instead of iloc[0,0] (best). The parent job run_id "quirky_nerve_rd6x9cq0tg" has the same AUC=0.816534 as the top child, so student correctly selects a child run — but the logic is fragile. Should explicitly exclude parent run or filter by child_run tag.
3. azureml.training.tabular dependency error — student correctly identified and documented the issue. The model.pkl was serialized on Python 3.10 + azureml.training.tabular; the local env is Python 3.12 without that package. This is a known/expected limitation. Student handled it correctly by pivoting to Model registration and download_artifacts() for inspection.
4. Reflection Q2 (featurization): Correct on imputation/encoding, but description of one-hot encoding is slightly off. AutoML uses ordinal encoding for high-cardinality features and one-hot for low-cardinality — it doesn't always produce one column per feature. Also, "Gender_Male" column name is illustrative but not how Azure AutoML names encoded features internally.
5. Reflection Q4 (min/max direction): "tænker man kan sætte det" — student doesn't know the answer. AutoML infers direction from a hardcoded metric registry. Student should know: AUC_weighted is maximized; NRMSE is minimized. The direction is NOT configurable by the user.
6. Inference cell (cell-19): Only partial — loads data and drops Attrition column, but never calls predict(). The cell is incomplete; no prediction output.

**Key observation:** Student is developing a consistent pattern of using search_runs() with experiment_id (hardcoded) + pandas sort. This works but hardcodes experiment IDs, which breaks if workspace changes. Better pattern: retrieve experiment ID programmatically via mlflow.get_experiment_by_name().

## Day 3 — MLflow Logging + Tracking (Evaluated 2026-02-23)

**Verdict:** Almost Ready

**What was correct:**
- Tracking URI retrieval and mlflow.set_tracking_uri() + mlflow.set_experiment() used correctly
- mlflow.log_params(dict) / log_metrics(dict) / set_tag() — all correct
- mlflow.sklearn.log_model() with manually defined ModelSignature — correct and shows depth (vs Day 2)
- log_artifact() for coefficient plot — correct use
- autolog() called BEFORE training, disabled after with disable=True — correct pattern
- Manually logging test metrics on top of autolog (since autolog doesn't capture test-set metrics) — shows real understanding
- mlflow.start_run() in command job used for run naming, not to fight AML's context — Day 2 issue resolved
- matplotlib.use("Agg") — correct for headless server environments
- Bonus: iterated 3 reg values across separate jobs, compared via search_runs — good initiative
- search_runs fallback to pandas filtering: pragmatic workaround for Azure ML backend limitation

**Issues found:**
1. CRITICAL: Notebook cell-14 (%%writefile) defines Schema, ColSpec, ModelSignature at module level BEFORE importing them — imports are missing (NameError on remote compute). However, the actual on-disk train.py is a different version that drops the signature entirely. The two versions are inconsistent.
2. On-disk train.py: mlflow.sklearn.log_model(model, artifact_path="model") — no signature= arg. Best practice is always to pass signature for deployment safety.
3. Reflection Q1: Conceptual gap — student confused about where log_model writes. Answer: MLflow artifact store = Azure Blob Storage container linked to the workspace. log_model writes to the run's artifact URI within that store.
4. Reflection Q3: Student says "jeg vil altid bruge with mlflow.start_run()" but doesn't explain the real value (run naming, nested run control, explicit context). Acceptable but shallow.

**Key file:** /Users/gade/Knowit/DP100/src/train.py
- Line 94: mlflow.sklearn.log_model(model, artifact_path="model") — missing signature= (minor)
- Notebook cell-14 vs on-disk train.py are inconsistent — cell-14 has NameError-inducing code

## Day 2 — Environments + Command Jobs (Evaluated 2026-02-23)

**Verdict:** Almost Ready

**What was correct:**
- command() function used correctly with all required parameters
- Input(type=URI_FILE) / Output(type=URI_FOLDER) syntax correct
- Environment(image=, conda_file=) + create_or_update() correct
- Curated environment discovery with AzureML- prefix filter
- argparse args match command string placeholders exactly
- Job completed successfully end-to-end
- Used AssetTypes constants (not raw strings)

**Issues found:**
1. mlflow.start_run() / mlflow.end_run() called manually — creates nested run inside AML command job
2. mlflow.log_artifact() used instead of mlflow.sklearn.log_model() — breaks model registry workflow for Day 7
3. Conda spec is bloated (20+ packages, many unrelated to training: py-spy, debugpy, kagglehub, etc.)
4. Output(path=None) — explicit None triggers SDK warning, should just omit path
5. No description on Environment object (minor, best practice)

**Key file:** /Users/gade/Knowit/DP100/src/train.py
- Line 47: mlflow.start_run() — problematic
- Line 93: mlflow.log_artifact() — should be mlflow.sklearn.log_model()
- Line 95: mlflow.end_run() — problematic
