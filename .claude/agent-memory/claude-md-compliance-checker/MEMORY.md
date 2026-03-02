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

## Day 6+7 Key Concepts (notebooks/06_07.ipynb)
LEARNING_PLAN.md Day 6: ManagedOnlineEndpoint, ManagedOnlineDeployment, scoring_script, blue/green
LEARNING_PLAN.md Day 7: BatchEndpoint, BatchDeployment, Model, register_model
- All concepts confirmed present in notebooks/06_07.ipynb.
- Combined notebook (06_07.ipynb) covers both days. LEARNING_PLAN.md specifies 06.ipynb and 07.ipynb separately — structural variation (minor: combined file is a deliberate design choice).
- score.py written via %%writefile cell in notebook. On disk src/score.py does NOT exist until student executes that cell — same pattern as train.py across prior notebooks.
- No solution code in code cells: confirmed. All code cells use TODO/HINT pattern only.
- Danish language: confirmed throughout all markdown cells.
- SDK v2 only: confirmed. No azureml.core imports anywhere.
- init_ml_client() from src/utils: confirmed in cell-mlclient.
- register_model concept: covered via ml_client.models.create_or_update() — note LEARNING_PLAN.md says "register_model" but SDK v2 uses create_or_update(). This is the correct SDK v2 equivalent; not a violation.
- src/score.py: created via %%writefile in cell-score-write. Score.py on disk still does not exist (student must execute cell). This is expected behavior for assignment notebooks.

## Day 8+9 Key Concepts (notebooks/08_09.ipynb)
LEARNING_PLAN.md Day 8: Hub vs Project, AI Foundry vs AML, model catalog, deployments
LEARNING_PLAN.md Day 9: Flow types (standard/chat/eval), connections, tools, deployment
- Combined notebook (08_09.ipynb) covers both days. LEARNING_PLAN.md specifies 08.ipynb and 09.ipynb separately — structural variation (minor: combined file follows 06_07.ipynb precedent).
- All Day 8 concepts confirmed: Hub/Project distinction (extensive), AI Foundry vs AML mapping table, Model Catalog with deployment methods (Managed Compute, Serverless API), integration patterns.
- All Day 9 concepts confirmed: Three flow types (Standard, Chat, Evaluation) with section 8 definitions, Connections (type table, Key Vault storage, sharing), Tools (LLM, Python, Prompt with examples), Deployment (section 12).
- Additional coverage: groundedness evaluation metrics, RAG patterns, security (API keys in Key Vault), chat history, responsibility AI.
- Danish language: confirmed throughout all markdown and code comments.
- SDK v2 only: confirmed. No azureml.core imports. Uses azure.ai.ml exclusively.
- init_ml_client() from src/utils: confirmed in cell-mlclient.
- VIOLATION FOUND: Cell cell-mlclient line 11 contains `ml_client.models.list()` — actual solution code without TODO/HINT comment. Must remove or wrap in comment before student assignment.
- Exam quiz: 7 questions mimicking DP-100 format provided at end (reflection questions included per pattern).
- Content structure: 15 sections, exam tips throughout, key takeaways summary — pedagogically strong.

## Day 10 Key Concepts (notebooks/10.ipynb)
LEARNING_PLAN.md Day 10: Index, indexer, semantic/vector search, RAG pattern, RAI dashboard
- All five concepts confirmed present and well-explained:
  - Index & Indexer: Section 2 (index structure), Section 4 (indexers vs. indexes distinguished correctly)
  - Semantic/Vector Search: Section 3 (four search types: keyword, semantic, vector, hybrid with use cases)
  - RAG Pattern: Section 6 (three steps: retrieve → augment → generate), Section 7 (chunking, embeddings)
  - RAI Dashboard: Section 11 (four components: error analysis, explanations/SHAP, counterfactuals, causal)
- Additional coverage (acceptable): Skillsets (section 4), "On Your Data" (section 8), Six RAI principles (section 10), Content Safety (section 13)
- Code exercises: Section 5 (SearchIndexClient), Section 14 (MLClient registry) — both use TODO/HINT scaffolding only
- Danish language: confirmed throughout (titles, explanations, table headers, tips)
- SDK v2 only: azure.search.documents, azure.ai.ml, azure.identity used; no azureml.core
- init_ml_client() pattern: Section 14 correctly imports from src/utils
- Exam quiz: 12 questions covering all Day 10 topics with answer key and explanations (section 17)
- Structure: 18 sections, integrated exam tips, 4 reflection Q&A sections, key takeaways — excellent pedagogical design
- **COMPLIANCE STATUS: 0 violations found. Fully compliant with CLAUDE.md and LEARNING_PLAN.md.**

## Ambiguities / Notes
- CLAUDE.md itself contains no content correctness rules, naming conventions, or structural mandates beyond agent usage. All content rules are inferred from LEARNING_PLAN.md.
- mlflow.sklearn.save_model() vs log_model(): save_model() saves locally to a path; log_model() logs to MLflow tracking server. Day 3 requires log_model for tracking server integration. Day 2 used save_model as scaffolding — acceptable then but must be updated by Day 3.
- Day 2 key concepts do not explicitly list MLflow usage — MLflow is introduced in Day 3. However, train.py is a shared script used across days, so MLflow calls in train.py are acceptable scaffolding for Day 2.
- src/utils.py (init_ml_client helper) is used in notebooks starting from Day 3. Not listed in LEARNING_PLAN.md repo structure but its presence in src/ is consistent with the project pattern.
- Day 4: LEARNING_PLAN.md lists "AutoMLJob" as a key concept but the SDK v2 does not expose a class literally named AutoMLJob — the object returned by automl.classification() is of type AutoMLJob internally. Cell-0 header lists it explicitly as a term. Treat as compliant: concept is covered even if the class name is not directly imported by the student.
