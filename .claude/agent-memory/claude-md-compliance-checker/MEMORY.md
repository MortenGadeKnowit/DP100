# CLAUDE.md Compliance Checker Memory

## Project Overview
- DP-100 Azure ML exam prep project. Learning plan in `/Users/gade/Knowit/DP100/docs/LEARNING_PLAN.md`.
- CLAUDE.md defines three agents: dp100-study-evaluator, claude-md-compliance-checker, dp100-assignment-maker. No structural or naming rules beyond what is in LEARNING_PLAN.md.
- Key content rules come from LEARNING_PLAN.md, not directly from CLAUDE.md.

## Key Rules from CLAUDE.md
1. After generating/modifying code/files: always run claude-md-compliance-checker before finishing.
2. After student submits work: run dp100-study-evaluator.
3. When student is ready for a new topic, use dp100-assignment-maker.
4. Agents can be run in parallel.
5. Agent rule #1 is IMPORTANT/highest priority.

## Repo Structure (from LEARNING_PLAN.md)
- notebooks/01-10.ipynb (numbered, topic-specific)
- src/train.py, src/score.py
- CLAUDE.md references src/train.py and src/score.py as primary script files.

## Day 2 Key Concepts (notebooks/02.ipynb)
Environment (curated vs custom), command(), Input/Output

## Day 3 Key Concepts (notebooks/03.ipynb)
log_metric, log_param, log_model, autolog, runs, experiments
- All six concepts confirmed present in notebooks/03.ipynb.
- train.py must use mlflow.start_run() + mlflow.sklearn.log_model() for Day 3 compliance.

## Patterns Observed
- src/train.py on disk uses mlflow.sklearn.save_model() (Day 2 version). Day 3 notebook cell 14 (%%writefile) defines the updated version with log_model + start_run. These must be kept in sync — a recurring violation risk.
- Notebook %%writefile cells must be executed to keep src/train.py on disk current. Always verify disk version matches notebook cell after a new notebook is created that rewrites train.py.
- Danish language used in notebook markdown cells — consistent with LEARNING_PLAN.md being in Danish.
- src/score.py does not yet exist — future requirement for Day 6 (Online Endpoints).

## Day 4 Key Concepts (notebooks/04.ipynb)
automl.classification, automl.regression, featurization, primary_metric, AutoMLJob
- All five concepts confirmed present in notebooks/04.ipynb.
- LEARNING_PLAN.md lists "automl.classification/regression, featurization, primary_metric" — AutoMLJob appears in cell-0 header but is not instantiated as a named class; the job object returned by automl.classification() IS an AutoMLJob instance, which is conceptually compliant.
- Notebook imports automl from azure.ai.ml and uses automl.regression() via direct import alias ("from azure.ai.ml.automl import regression") — both are valid SDK v2 patterns.

## Day 5 Key Concepts (notebooks/05.ipynb)
SweepJob, search_space, sampling_algorithm, early_termination, @pipeline, PipelineJob
- All six concepts confirmed present in notebooks/05.ipynb (cell-0 header + extensive coverage throughout).
- SweepJob: covered via `Sweep` class from `azure.ai.ml.sweep` (mentioned in section 2), `.sweep()` method pattern, BanditPolicy, etc.
- PipelineJob: listed in cell-0 header as a key concept but NOT instantiated directly — the pipeline function returns a PipelineJob when called. Same pattern as AutoMLJob in Day 4: treat as compliant.
- train.py %%writefile cell (cell-8) contains TODO scaffolding for --solver, args.solver usage, and mlflow.log_param("solver") — correctly NOT pre-filled (student must implement). However, the cell does contain partial implementation (hardcoded "liblinear" remains in LogisticRegression call) which is intentional scaffolding, not a violation.
- src/prep.py: new script created via %%writefile in cell-19. Not listed in LEARNING_PLAN.md repo structure but is a pipeline-step script for Day 5. Acceptable extension.
- Disk src/train.py is the Day 3/4 version (no --solver arg). The Day 5 %%writefile cell rewrites it with TODO placeholders. Student must execute cell-8 to update disk version.
- WARNING pattern: %%writefile cells with TODO stubs will write incomplete code to disk when executed. This is intentional for the assignment. Not a violation but worth noting.

## Ambiguities / Notes
- CLAUDE.md itself contains no content correctness rules, naming conventions, or structural mandates beyond agent usage. All content rules are inferred from LEARNING_PLAN.md.
- mlflow.sklearn.save_model() vs log_model(): save_model() saves locally to a path; log_model() logs to MLflow tracking server. Day 3 requires log_model for tracking server integration. Day 2 used save_model as scaffolding — acceptable then but must be updated by Day 3.
- Day 2 key concepts do not explicitly list MLflow usage — MLflow is introduced in Day 3. However, train.py is a shared script used across days, so MLflow calls in train.py are acceptable scaffolding for Day 2.
- src/utils.py (init_ml_client helper) is used in notebooks starting from Day 3. Not listed in LEARNING_PLAN.md repo structure but its presence in src/ is consistent with the project pattern.
- Day 4: LEARNING_PLAN.md lists "AutoMLJob" as a key concept but the SDK v2 does not expose a class literally named AutoMLJob — the object returned by automl.classification() is of type AutoMLJob internally. Cell-0 header lists it explicitly as a term. Treat as compliant: concept is covered even if the class name is not directly imported by the student.
