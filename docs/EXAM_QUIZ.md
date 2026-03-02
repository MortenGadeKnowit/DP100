# DP-100 Eksamensquiz

**Samlet:** 60 spørgsmål fordelt på de 4 officielle eksamensdomæner.
**Format:** Multiple choice (A-D). Facit med forklaringer i bunden af hvert domæne.

---

## Domæne 1: Design and Prepare a Machine Learning Solution (20-25%)

### Workspace, Compute & Data

**Q1.** Du skal opsætte et udviklingsmiljø til en data scientist, der skal køre Jupyter notebooks interaktivt. Hvilken compute-type vælger du?

A) Compute cluster (AmlCompute)
B) Compute instance
C) Attached Spark pool
D) Kubernetes compute

---

**Q2.** Du har et compute cluster med `min_nodes=0` og `max_nodes=4`. Hvad sker der, når der ikke er nogen aktive jobs?

A) Clusteret kører med én node for hurtig opstart
B) Clusteret skalerer ned til 0 noder og stopper fakturering af compute
C) Clusteret slettes automatisk efter 30 minutter
D) Clusteret forbliver på 4 noder indtil manuelt stoppet

---

**Q3.** Hvilken datatype bruger du, når du vil referere til en *enkelt CSV-fil* i Azure Blob Storage som et data asset?

A) `URI_FOLDER`
B) `URI_FILE`
C) `MLTABLE`
D) `CUSTOM_DATA`

---

**Q4.** Du har et datasæt med flere CSV-filer i en mappe og vil anvende et schema (kolonnetyper + subset af filer). Hvilken AssetType bruger du?

A) `URI_FILE`
B) `URI_FOLDER`
C) `MLTABLE`
D) `PARQUET`

---

**Q5.** Hvad er en **datastore** i Azure ML?

A) En kopi af datasættet gemt i workspace-storage
B) En reference til en ekstern storage-lokation med forbindelsesoplysninger
C) En database med metadata om alle data assets
D) En compute-ressource dedikeret til data processing

---

**Q6.** Du vil dele et custom environment mellem flere Azure ML workspaces i din organisation. Hvad bruger du?

A) Azure Container Registry
B) Azure ML Registry
C) Azure DevOps Artifacts
D) Kopiér environment-definitionen manuelt til hvert workspace

---

**Q7.** Hvad er forskellen mellem et **curated environment** og et **custom environment** i Azure ML?

A) Curated environments er gratis, custom environments koster ekstra
B) Curated environments vedligeholdes af Microsoft med populære ML-frameworks; custom environments defineres af brugeren
C) Custom environments kan kun bruges til training, ikke deployment
D) Curated environments er låst til specifikke compute-typer

---

**Q8.** Du konfigurerer et command job. Hvilket objekt bruger du til at angive inputdata?

A) `DataPath(datastore, path)`
B) `Input(type=AssetTypes.URI_FILE, path="azureml:my-data:1")`
C) `Dataset.get_by_name(workspace, "my-data")`
D) `DataReference(datastore, path_on_datastore)`

---

**Q9.** Hvad er formålet med Git-integration i et Azure ML workspace?

A) Automatisk deployment af modeller ved git push
B) Versionsstyring af notebooks og eksperimenter via source control
C) Synkronisering af data assets med et git repository
D) Automatisk oprettelse af pipelines fra git branches

---

**Q10.** Du vil oprette et compute cluster, der automatisk skalerer baseret på job-kø. Hvilken konfigurationsparameter styrer den maksimale kapacitet?

A) `max_replicas`
B) `max_nodes`
C) `max_instances`
D) `node_count`

---

### Facit: Domæne 1

| # | Svar | Forklaring |
|---|------|------------|
| Q1 | **B** | Compute instance er en single-node managed VM til interaktiv udvikling (notebooks, terminal). Compute cluster er til jobs. |
| Q2 | **B** | Med `min_nodes=0` skalerer clusteret ned til 0 noder når der ingen jobs er. Ingen compute-fakturering ved idle (du betaler kun for storage). |
| Q3 | **B** | `URI_FILE` refererer til en enkelt fil. `URI_FOLDER` til en mappe. `MLTABLE` til tabeldata med schema. |
| Q4 | **C** | `MLTABLE` understøtter schema-definition (kolonnetyper, filfiltrering) via en MLTable-fil. `URI_FOLDER` giver bare en sti uden schema. |
| Q5 | **B** | En datastore er en *reference* (connection string + credentials) til en ekstern storage-lokation (Blob, ADLS, SQL). Den kopierer ikke data. |
| Q6 | **B** | Azure ML Registry gør det muligt at dele assets (environments, models, components) på tværs af workspaces. |
| Q7 | **B** | Curated environments vedligeholdes af Microsoft (f.eks. AzureML-sklearn-1.0). Custom environments defineres af brugeren med Dockerfile eller conda spec. |
| Q8 | **B** | SDK v2 bruger `Input(type=AssetTypes.URI_FILE, path=...)`. Option C og D er SDK v1-patterns. |
| Q9 | **B** | Git-integration i Azure ML giver versionsstyring af kode og notebooks. Det er ikke en CI/CD-pipeline. |
| Q10 | **B** | `max_nodes` styrer den maksimale antal noder i et AmlCompute cluster. |

---

## Domæne 2: Explore Data, and Run Experiments (20-25%)

### AutoML

**Q11.** Du træner en AutoML-klassifikationsmodel på et datasæt med 95% negative og 5% positive klasser. Hvilken `primary_metric` er mest hensigtsmæssig?

A) `accuracy`
B) `AUC_weighted`
C) `f1_score_micro`
D) `log_loss`

---

**Q12.** Hvad gør `featurization="auto"` i en AutoML-konfiguration?

A) Bruger kun de features der er angivet i konfigurationen
B) Anvender automatisk imputation af missing values, encoding af kategoriske variable og feature scaling
C) Deaktiverer al feature engineering
D) Genererer kun polynomial features

---

**Q13.** Du kører AutoML til billedklassifikation. Hvilken `task` angiver du?

A) `classification`
B) `image_classification`
C) `vision`
D) `image-classification-multilabel`

---

**Q14.** Hvad bruges `set_limits()` til i en AutoML-konfiguration?

A) Begrænser antal features i modellen
B) Sætter grænser for træningstid, antal trials og concurrent runs
C) Begrænser datasættets størrelse
D) Sætter memory-limits for compute

---

**Q15.** Du har kørt et AutoML-eksperiment og vil se den bedste models feature importance. Hvad bruger du?

A) `mlflow.autolog()` output
B) AutoML Model Explanations i Azure ML Studio
C) `model.coef_` direkte på modellen
D) `shap.TreeExplainer` manuelt

---

### MLflow Tracking

**Q16.** Hvad er forskellen mellem `mlflow.log_metric()` og `mlflow.log_metrics()`?

A) `log_metric` logger til fil, `log_metrics` logger til MLflow server
B) `log_metric` logger én metrik, `log_metrics` logger flere metriks som et dict
C) `log_metrics` logger metriks over tid (step-baseret)
D) Der er ingen forskel, de er aliases

---

**Q17.** Du vil automatisk logge alle hyperparametre, metriks og model-artefakter under træning uden eksplicitte log-kald. Hvad bruger du?

A) `mlflow.start_run(log_all=True)`
B) `mlflow.autolog()`
C) `mlflow.set_tracking_uri("auto")`
D) `mlflow.enable_system_metrics_logging()`

---

**Q18.** Hvad definerer en **ModelSignature** i MLflow?

A) En digital signatur til at verificere modellens integritet
B) Et schema der beskriver modellens forventede input- og output-datatyper
C) En hash af modellens vægte og parametre
D) Metadata om hvem der har trænet modellen

---

**Q19.** Du kører et script som et Azure ML command job. MLflow tracking URI sættes automatisk. Hvor logges metrikkerne?

A) Til en lokal SQLite-database
B) Til Azure ML workspace's tracking server
C) Til en MLflow server du selv har opsat
D) Til Azure Application Insights

---

**Q20.** Hvad er forskellen mellem `mlflow.sklearn.log_model()` og `mlflow.sklearn.save_model()`?

A) `log_model` gemmer til MLflow tracking server som artifact; `save_model` gemmer til lokal sti
B) `log_model` kræver en aktiv run; `save_model` kræver ingen run
C) Begge A og B er korrekte
D) Der er ingen forskel

---

### Hyperparameter Tuning

**Q21.** Du vil prøve alle mulige kombinationer af hyperparametre: `learning_rate=[0.01, 0.1]` og `batch_size=[16, 32, 64]`. Hvilken sampling-metode bruger du?

A) Random sampling
B) Grid sampling
C) Bayesian sampling
D) Sobol sampling

---

**Q22.** Hvilken sampling-metode kan **ikke** kombineres med en early termination policy?

A) Random sampling
B) Grid sampling
C) Bayesian sampling
D) Alle tre kan kombineres med early termination

---

**Q23.** Du opsætter en `BanditPolicy` med `slack_factor=0.1` og `evaluation_interval=2`. Hvad betyder det?

A) Trials termineres hvis de er mere end 10% dårligere end den bedste trial, evalueret hvert 2. interval
B) 10% af trials termineres tilfældigt hvert 2. interval
C) Trials der ikke forbedres med 10% over 2 intervaller termineres
D) De 10% dårligste trials i hvert batch af 2 termineres

---

**Q24.** I en sweep job bruger du `Choice` til at definere search space for en hyperparameter. Hvad returnerer `Choice`?

A) En tilfældig værdi fra et kontinuert interval
B) En værdi valgt fra en diskret liste af foruddefinerede værdier
C) En logaritmisk samplet værdi
D) En normalfordelt værdi

---

**Q25.** Hvad er `primary_metric` i en sweep job?

A) Den metrik der bruges til at evaluere modellens performance på test-data
B) Den metrik sweep-jobbet optimerer — bruges til at sammenligne og rangere trials
C) Den første metrik der logges i et MLflow run
D) En built-in metrik fra sklearn

---

### Facit: Domæne 2

| # | Svar | Forklaring |
|---|------|------------|
| Q11 | **B** | Ved stærkt ubalancerede klasser er `accuracy` misvisende (95% accuracy ved altid at gætte negativ). `AUC_weighted` vægter klasserne og er robust mod ubalance. |
| Q12 | **B** | `featurization="auto"` imputer missing values, encoder kategoriske variable (one-hot/target encoding), og skalerer numeriske features automatisk. |
| Q13 | **B** | AutoML til billeder bruger `image_classification` (eller `image_classification_multilabel` for multi-label). `classification` er kun til tabeldata. |
| Q14 | **B** | `set_limits()` sætter `timeout_minutes`, `max_trials`, `max_concurrent_trials` m.fl. for at kontrollere AutoML-eksperimentet. |
| Q15 | **B** | Azure ML Studio viser automatisk Model Explanations (feature importance) for AutoML-modeller via Responsible AI integration. |
| Q16 | **B** | `log_metric("acc", 0.9)` logger én metrik. `log_metrics({"acc": 0.9, "loss": 0.1})` logger flere som dict. |
| Q17 | **B** | `mlflow.autolog()` aktiverer automatisk logging af params, metrics og artifacts for understøttede frameworks (sklearn, TensorFlow, PyTorch, m.fl.). |
| Q18 | **B** | ModelSignature definerer input/output-schema (kolonnenavne og datatyper). Bruges til validering ved inferens og no-code deployment. |
| Q19 | **B** | Azure ML command jobs sætter automatisk `MLFLOW_TRACKING_URI` til workspace's tracking endpoint. Alle metriks logges der. |
| Q20 | **C** | `log_model` logger modellen som et artifact i en aktiv MLflow run. `save_model` gemmer til en lokal sti uden at kræve en run. |
| Q21 | **B** | Grid sampling prøver alle kombinationer systematisk. 2×3 = 6 trials total. Random sampling vælger tilfældigt. |
| Q22 | **C** | Bayesian sampling er sekventiel og afhænger af resultater fra tidligere trials. Early termination forstyrrer denne proces, så de kan ikke kombineres. |
| Q23 | **A** | BanditPolicy med `slack_factor=0.1` terminerer trials der performer >10% dårligere end den bedste trial. `evaluation_interval=2` checker hvert 2. logging-interval. |
| Q24 | **B** | `Choice([0.01, 0.1, 1.0])` vælger fra en diskret liste. `Uniform`/`LogUniform` bruges til kontinuerte intervaller. |
| Q25 | **B** | `primary_metric` er den metrik sweep-jobbet bruger til at rangere trials og bestemme den bedste. Den skal logges med `mlflow.log_metric()` i træningsscriptet. |

---

## Domæne 3: Train and Deploy Models (25-30%)

### Jobs & Pipelines

**Q26.** Du vil køre et Python-script som et Azure ML job med specifikke inputdata og et custom environment. Hvilken funktion bruger du?

A) `ml_client.jobs.submit()`
B) `command(code="./src", command="python train.py", environment=..., inputs=...)`
C) `PythonScriptStep(script_name="train.py", ...)`
D) `RunConfiguration(script="train.py")`

---

**Q27.** I en Azure ML pipeline, hvordan sender du output fra step 1 som input til step 2?

A) Gem output til en delt fil og læs den i step 2
B) Brug `step2(input_data=step1.outputs.output_name)`
C) Brug en global variabel
D) Skriv til en database mellem steps

---

**Q28.** Hvad er en **component** i Azure ML pipelines?

A) En fysisk compute-node i et cluster
B) En genanvendelig, selvstændig enhed af kode med definerede inputs/outputs
C) Et Docker image til en pipeline
D) En type data asset

---

**Q29.** Hvor gemmes intermediate data mellem pipeline steps som standard?

A) I containerens lokale filsystem
B) I workspace's default datastore (workspaceblobstore)
C) I compute clusterets RAM
D) I Azure SQL Database

---

**Q30.** Du vil køre en pipeline automatisk hver mandag kl. 08:00. Hvad bruger du?

A) Azure Functions timer trigger
B) `ml_client.schedules.begin_create_or_update(schedule)`
C) Cron job på compute instance
D) Azure Logic Apps

---

### Model Management

**Q31.** Du registrerer en model med `Model(name="my-model", path=..., type=AssetTypes.MLFLOW_MODEL)`. Hvad sker der, hvis du registrerer igen med samme navn?

A) Den overskriver den eksisterende model
B) Der oprettes automatisk en ny version (v2)
C) Du får en fejl — navnet er allerede i brug
D) Den eksisterende model arkiveres

---

**Q32.** Hvad er fordelen ved at registrere en model som `MLFLOW_MODEL` i stedet for `CUSTOM_MODEL`?

A) MLflow-modeller er mindre i størrelse
B) MLflow-modeller understøtter no-code deployment — Azure ML kan automatisk generere scoring-endpoint
C) MLflow-modeller er hurtigere at træne
D) Custom models kan ikke deployes til online endpoints

---

**Q33.** Du vil tagge en registreret model som "production-ready" uden at oprette en ny version. Er det muligt?

A) Nej, enhver ændring opretter en ny version
B) Ja, opdatér `model.tags` og kald `ml_client.models.create_or_update(model)` med samme version
C) Ja, men kun via Azure ML Studio UI
D) Nej, tags er immutable efter registrering

---

### Online Endpoints

**Q34.** Hvad er forskellen mellem et **endpoint** og et **deployment** i Azure ML?

A) De er det samme — begge termer refererer til en hosted model
B) Et endpoint er URL'en/API'et; et deployment er den konkrete model+compute bag endpointet
C) Et endpoint er til online inferens; et deployment er til batch
D) Et deployment indeholder flere endpoints

---

**Q35.** Hvad gør `init()` funktionen i et scoring script?

A) Initialiserer compute-ressourcer
B) Køres ved container-opstart for at indlæse modellen i hukommelsen
C) Validerer input-data før scoring
D) Opretter forbindelse til Azure ML workspace

---

**Q36.** Du har to deployments på et online endpoint: `blue` (80%) og `green` (20%). Du vil teste `green` direkte uden at ændre traffic. Hvad gør du?

A) Sæt midlertidigt traffic til `{"green": 100}`
B) Brug `ml_client.online_endpoints.invoke(endpoint_name=..., deployment_name="green")`
C) Opret et separat test-endpoint
D) Det er ikke muligt — traffic-fordelingen gælder altid

---

**Q37.** Hvilken environment-variabel bruges i `init()` til at finde den deployede model's sti?

A) `MODEL_PATH`
B) `AZUREML_MODEL_DIR`
C) `MLFLOW_MODEL_URI`
D) `SCORING_MODEL_PATH`

---

**Q38.** Et online endpoint med `auth_mode="key"` — hvad betyder det?

A) Endpoints er offentligt tilgængeligt uden autentificering
B) Klienter autentificerer med en statisk API-nøgle
C) Klienter autentificerer med Azure AD token
D) Klienter autentificerer med et X.509 certifikat

---

### Batch Endpoints

**Q39.** Hvad er hovedforskellen mellem et online endpoint og et batch endpoint?

A) Online endpoints bruger GPU, batch endpoints bruger CPU
B) Online endpoints er synkrone (real-time svar); batch endpoints er asynkrone (starter et job)
C) Batch endpoints kan kun bruges med MLflow-modeller
D) Online endpoints er gratis, batch endpoints koster ekstra

---

**Q40.** Hvilken compute-type kræver en batch deployment?

A) Compute instance
B) Managed online compute
C) AmlCompute cluster
D) Serverless compute

---

**Q41.** Hvad styrer `mini_batch_size` i en batch deployment?

A) Antal rækker per request til `run()`
B) Antal filer der sendes til `run()` i hvert batch
C) Maximum hukommelse per batch
D) Antal parallelle instanser

---

**Q42.** Hvad gør `output_action=BatchDeploymentOutputAction.APPEND_ROW`?

A) Hvert batch-resultat gemmes som en separat fil
B) Alle predictions samles i én output-fil med én linje per prediction
C) Output sendes til en Azure SQL-database
D) Output logges som MLflow metrics

---

### Facit: Domæne 3

| # | Svar | Forklaring |
|---|------|------------|
| Q26 | **B** | SDK v2 bruger `command()` funktionen. Option C (`PythonScriptStep`) er SDK v1. Option D (`RunConfiguration`) er også SDK v1. |
| Q27 | **B** | I SDK v2 pipelines refererer du til outputs med `step1.outputs.output_name` og sender dem som input til næste step. |
| Q28 | **B** | En component er en genanvendelig kode-enhed med definerede inputs, outputs og environment. Den kan bruges i flere pipelines. |
| Q29 | **B** | Intermediate data gemmes i workspace's default datastore (workspaceblobstore i Azure Blob Storage), ikke i containerens filsystem. |
| Q30 | **B** | Azure ML SDK v2 har native schedule-support: `ml_client.schedules.begin_create_or_update()` med cron eller recurrence. |
| Q31 | **B** | Registrering med samme navn men uden at angive version opretter automatisk en ny version (auto-increment). |
| Q32 | **B** | MLflow-modeller har standardiseret format med `MLmodel`-fil, signature og dependencies. Azure ML kan generere scoring-script automatisk (no-code deployment). |
| Q33 | **B** | Tags kan opdateres på en eksisterende model-version uden at oprette en ny version. Kald `create_or_update()` med ændrede tags. |
| Q34 | **B** | Endpoint = den stabile URL/API. Deployment = model + environment + compute bag endpointet. Ét endpoint kan have flere deployments (blue/green). |
| Q35 | **B** | `init()` køres én gang ved container-opstart. Typisk bruges den til at indlæse modellen fra `AZUREML_MODEL_DIR` ind i hukommelsen. |
| Q36 | **B** | `deployment_name` parameteren i `invoke()` sender request direkte til det angivne deployment, uanset traffic-fordeling. |
| Q37 | **B** | `AZUREML_MODEL_DIR` er den environment-variabel Azure ML sætter, der peger på model-mappen i containeren. |
| Q38 | **B** | `auth_mode="key"` betyder API-nøgle autentificering. Alternativet er `"aml_token"` (Azure AD token med expiry). |
| Q39 | **B** | Online endpoints giver real-time svar (synkron). Batch endpoints starter et job og returnerer resultater asynkront. |
| Q40 | **C** | Batch deployments kræver et AmlCompute cluster. Online deployments bruger managed compute (du angiver `instance_type`). |
| Q41 | **B** | `mini_batch_size` styrer antal filer (ikke rækker) der sendes til `run()` per batch. |
| Q42 | **B** | `APPEND_ROW` samler alle predictions i én CSV-fil med én linje per prediction. Alternativet `SUMMARY_ONLY` gemmer kun metadata. |

---

## Domæne 4: Optimize Language Models for AI Applications (25-30%)

### Azure AI Foundry

**Q43.** Hvad er forholdet mellem en Azure AI Foundry **Hub** og et **Project**?

A) Hub og Project er synonymer
B) Hub er det øverste administrationsniveau med delte ressourcer; Projects er isolerede arbejdsrum under en Hub
C) Project er overordnet og indeholder flere Hubs
D) Hub er til compute, Project er til storage

---

**Q44.** Du opretter et nyt AI Foundry Hub. Hvilken Azure-ressource oprettes automatisk?

A) En Azure Kubernetes Service cluster
B) En Azure ML workspace (kind=hub)
C) En Azure Databricks workspace
D) En Azure Cognitive Services ressource

---

**Q45.** Tre teams skal dele den samme Azure OpenAI API-nøgle. Hvor konfigurerer du connectionen?

A) I hvert teams Project individuelt
B) I Hub'en, så den arves af alle Projects
C) I Azure Key Vault manuelt
D) I en .env-fil i hvert teams repository

---

**Q46.** Du vil deploye Phi-4 med minimal opsætning og pay-per-token. Hvilken deployment-metode vælger du?

A) Managed Compute deployment
B) Azure Kubernetes Service deployment
C) Serverless API (Models as a Service)
D) Azure Container Instances

---

### Prompt Flow

**Q47.** Hvilken Prompt Flow-type har built-in support for `chat_history`?

A) Standard Flow
B) Chat Flow
C) Evaluation Flow
D) RAG Flow

---

**Q48.** Hvad er et **Evaluation Flow** i Prompt Flow?

A) Et flow der evaluerer compute-performance
B) Et flow der bedømmer kvaliteten af et andet flows output med metriks
C) Et flow der automatisk optimerer prompts
D) Et flow der evaluerer cost vs. quality trade-offs

---

**Q49.** Hvor gemmes API-nøgler for Prompt Flow connections?

A) I flow.dag.yaml i klar tekst
B) I Azure Key Vault tilknyttet Hub'en
C) I environment variables på compute
D) I en encrypted config-fil i flow-mappen

---

**Q50.** Du vil skrive Python-kode til at parse et LLM-output i Prompt Flow. Hvilket tool bruger du?

A) LLM Tool med custom output parsing
B) Prompt Tool med Jinja2
C) Python Tool med `@tool`-dekorator
D) Code Interpreter Tool

---

**Q51.** Et deployed Prompt Flow kører som hvilken type Azure ML ressource?

A) Compute instance
B) Azure Function
C) Online Endpoint (ManagedOnlineDeployment)
D) Batch Endpoint

---

### RAG & AI Search

**Q52.** Hvad er den korrekte rækkefølge i RAG-mønsteret?

A) Generate → Retrieve → Augment
B) Augment → Retrieve → Generate
C) Retrieve → Augment → Generate
D) Retrieve → Generate → Augment

---

**Q53.** Du forbereder dokumenter til RAG. Hvad er **chunking**?

A) Komprimering af dokumenter for at spare storage
B) Opdeling af store dokumenter i mindre segmenter, der kan embeddes og søges individuelt
C) Fjernelse af duplikerede afsnit
D) Konvertering af dokumenter til JSON-format

---

**Q54.** Hvad bruges **embeddings** til i en RAG-pipeline?

A) Kryptering af dokumenter for sikkerhed
B) Konvertering af tekst til numeriske vektorer, der muliggør semantisk søgning
C) Komprimering af tekst til kortere versioner
D) Oversættelse af tekst mellem sprog

---

**Q55.** Hvad er forskellen mellem **semantic search** og **vector search** i Azure AI Search?

A) Semantic search bruger embeddings; vector search bruger keyword matching
B) Semantic search bruger en language model til re-ranking af BM25-resultater; vector search bruger embeddings til similarity-søgning
C) De er det samme — begge bruger AI-baseret søgning
D) Vector search er hurtigere men mindre præcis

---

**Q56.** Hvad er **hybrid search** i Azure AI Search?

A) Søgning der kombinerer SQL og NoSQL
B) Søgning der kombinerer keyword (BM25) og vector search med Reciprocal Rank Fusion (RRF)
C) Søgning på tværs af flere indekser
D) Søgning der bruger både on-premises og cloud

---

### Responsible AI

**Q57.** Hvilken Responsible AI-metrik måler om en LLM's svar er baseret på den retrievede kontekst (anti-hallucination)?

A) Coherence
B) Fluency
C) Groundedness
D) Similarity

---

**Q58.** Hvad er **counterfactuals** i Responsible AI dashboardet?

A) Forudsigelser baseret på syntetisk data
B) De nærmeste datapunkter med en *anderledes* model-prediction — viser hvad der skulle ændres for et andet resultat
C) Antal forkerte predictions i test-data
D) Alternative modeller der sammenlignes

---

**Q59.** Hvilken RAI Dashboard-komponent identificerer subgrupper af data hvor modellen performer særligt dårligt?

A) Explanations
B) Error Analysis
C) Counterfactuals
D) Causal Analysis

---

**Q60.** Hvad er de 6 Microsoft Responsible AI-principper?

A) Accuracy, Speed, Cost, Scalability, Security, Compliance
B) Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, Accountability
C) Bias, Variance, Overfitting, Underfitting, Interpretability, Robustness
D) Precision, Recall, F1, AUC, Accuracy, Log Loss

---

### Facit: Domæne 4

| # | Svar | Forklaring |
|---|------|------------|
| Q43 | **B** | Hub = øverste niveau med delte ressourcer (connections, compute, storage). Projects arver fra Hub og giver isolation per team. |
| Q44 | **B** | Oprettelse af en AI Foundry Hub opretter automatisk en Azure ML workspace (kind=hub) i din subscription. |
| Q45 | **B** | Connections defineret på Hub-niveau arves automatisk af alle Projects under den Hub. |
| Q46 | **C** | Serverless API (Models as a Service) = pay-per-token, ingen compute-konfiguration. Managed Compute kræver VM-specifikation. |
| Q47 | **B** | Chat Flow har `chat_history` som reserveret input — den eneste strukturelle forskel fra Standard Flow. |
| Q48 | **B** | Evaluation Flow modtager output fra et andet flow + (optionelt) ground truth og returnerer kvalitetsmetriks (groundedness, relevance, etc.). |
| Q49 | **B** | Connections gemmer credentials i Azure Key Vault. Flows refererer til connection-navnet, aldrig til selve nøglen. |
| Q50 | **C** | Python Tool med `@tool`-dekorator bruges til vilkårlig Python-kode inkl. parsing, databehandling og API-kald. |
| Q51 | **C** | Et deployed Prompt Flow er et Online Endpoint (ManagedOnlineDeployment) — samme infrastruktur som model-deployments. |
| Q52 | **C** | RAG: **Retrieve** relevante dokumenter → **Augment** prompten med kontekst → **Generate** svar med LLM. |
| Q53 | **B** | Chunking opdeler store dokumenter i mindre segmenter (f.eks. 500 tokens), der individuelt embeddes og indexeres for søgning. |
| Q54 | **B** | Embeddings konverterer tekst til numeriske vektorer i et semantisk rum, hvor lignende tekster har lignende vektorer. |
| Q55 | **B** | Semantic search = BM25 keyword match + AI re-ranking. Vector search = embedding-baseret similarity. De er komplementære teknikker. |
| Q56 | **B** | Hybrid search kombinerer BM25 (keyword) og vector search og fusionerer resultaterne med RRF (Reciprocal Rank Fusion). |
| Q57 | **C** | Groundedness måler om svaret er baseret på den givne kontekst. Lav groundedness = hallucination. |
| Q58 | **B** | Counterfactuals viser de mindste ændringer i features der ville ændre modellens prediction — bruges til fairness og forståelse. |
| Q59 | **B** | Error Analysis identificerer subgrupper (f.eks. "kvinder over 50") hvor modellen har højere fejlrate end gennemsnittet. |
| Q60 | **B** | Microsofts 6 RAI-principper: Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, Accountability. |

---

## Hurtig opsummering: Nøgletal til eksamen

| Koncept | Huske-regel |
|---------|-------------|
| Compute instance vs. cluster | Instance = interaktiv udvikling (1 node). Cluster = jobs (0-N noder, auto-scale). |
| URI_FILE vs. URI_FOLDER vs. MLTABLE | FILE = enkelt fil. FOLDER = mappe. MLTABLE = tabeldata med schema. |
| Curated vs. custom environment | Curated = Microsoft-vedligeholdt. Custom = din conda/Docker spec. |
| AutoML primary_metric (ubalanceret) | Brug `AUC_weighted`, ALDRIG `accuracy` ved ubalancerede klasser. |
| `mlflow.autolog()` | Kalder du FØR træning. Logger params, metrics, artifacts automatisk. |
| log_model vs. save_model | `log_model` → MLflow tracking (kræver run). `save_model` → lokal sti (ingen run). |
| Grid vs. Random vs. Bayesian | Grid = alle kombinationer. Random = tilfældig sampling. Bayesian = sekventiel, INGEN early termination. |
| BanditPolicy slack_factor | Terminerer trials der er >slack_factor% dårligere end bedste trial. |
| Pipeline intermediate data | Gemmes i workspaceblobstore (Azure Blob), IKKE i Docker container. |
| Endpoint vs. deployment | Endpoint = stabil URL. Deployment = model+compute bag URL'en. |
| `init()` + `run()` | `init()` = container-opstart (load model). `run()` = per-request (parse JSON, predict, return JSON). |
| `AZUREML_MODEL_DIR` | Environment var der peger på model-mappen i containeren. |
| Online vs. batch | Online = synkron, managed compute. Batch = asynkron, AmlCompute cluster. |
| `mini_batch_size` | Antal FILER per batch til `run()` (ikke rækker). |
| Hub vs. Project | Hub = deling + governance. Project = isolation per team. Hub opretter AML workspace. |
| Serverless API vs. Managed Compute | Serverless = pay-per-token, nul infra. Managed = pay-per-hour, du styrer VM. |
| Chat Flow vs. Standard Flow | Chat Flow har `chat_history` input. Ellers strukturelt ens. |
| Connections + Key Vault | API-nøgler i Key Vault. Flow refererer til connection-navn. |
| RAG rækkefølge | Retrieve → Augment → Generate. |
| Semantic vs. Vector vs. Hybrid | Semantic = BM25 + AI re-ranking. Vector = embeddings. Hybrid = begge + RRF. |
| Groundedness | Anti-hallucination metrik. Holder svaret sig til konteksten? |
| Counterfactuals | Mindste feature-ændring for anderledes prediction. |
| Error Analysis | Finder subgrupper med høj fejlrate. |
| 6 RAI-principper | Fairness, Reliability, Privacy, Inclusiveness, Transparency, Accountability. |

---

*Genereret 2026-03-01. Kilder: [Microsoft DP-100 Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-100), [Microsoft Learn Exam Readiness Zone](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/preparing-for-dp-100-01-fy25), [ExamTopics DP-100](https://www.examtopics.com/exams/microsoft/dp-100/).*
