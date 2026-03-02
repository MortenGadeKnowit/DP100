import os
import json
import pandas as pd
import mlflow.pyfunc

model = None


def init():
    global model
    model_dir = os.environ["AZUREML_MODEL_DIR"]
    # Find den faktiske MLmodel-mappe
    for root, dirs, files in os.walk(model_dir):
        if "MLmodel" in files:
            model_dir = root
            break

    model = mlflow.pyfunc.load_model(model_dir)

def run(raw_data: str) -> str:
    """Køres per inference-request.

    Args:
        raw_data: JSON-streng med input-data.
            Eksempel: '{"data": [[35, 3, 2, 3, 5, 5000, 1, 0, 0]]}'

    Returns:
        JSON-streng med predictions.
    """
    # TODO: Parse raw_data med json.loads()
    data = json.loads(raw_data)

    import numpy as np
    df = pd.DataFrame(data['data'], columns=['Age', 'WorkLifeBalance', 'YearsSinceLastPromotion', 'JobInvolvement', 'YearsAtCompany', 'MonthlyIncome', 'Gender_Male', 'Department_Research & Development', 'Department_Sales'])
    df = df.astype(np.int32)

    # TODO: Kald model.predict() og konverter resultatet til en Python-liste
    predictions = list(model.predict(df))

    # TODO: Returner resultatet som JSON-streng
    return json.dumps(predictions)
