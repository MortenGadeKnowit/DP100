from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

def init_ml_client() -> MLClient:
    import os
    from dotenv import load_dotenv
    load_dotenv("../.env")
        
    ml_client = MLClient(
        credential=DefaultAzureCredential(),
        subscription_id=os.environ['subscription_id'],
        resource_group_name=os.environ['resource_group_name'],
        workspace_name=os.environ['workspace_name']
    )

    return ml_client

def search_for_runs():
    pass

