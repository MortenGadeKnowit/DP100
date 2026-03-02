import matplotlib.pyplot as plt
import argparse
from pathlib import Path
import pandas as pd
import mlflow
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import mlflow
import mlflow.sklearn
from mlflow.types.schema import Schema, ColSpec
from mlflow.models.signature import ModelSignature

input_schema = Schema([
    ColSpec("integer", "Age"),
    ColSpec("integer", "WorkLifeBalance"),
    ColSpec("integer", "YearsSinceLastPromotion"),
    ColSpec("integer", "JobInvolvement"),
    ColSpec("integer", "YearsAtCompany"),
    ColSpec("integer", "MonthlyIncome"),
    ColSpec("integer", "Gender_Female"),
    ColSpec("integer", "Department_Human Resources"),
    ColSpec("integer", "Department_Research & Development"),
    ColSpec("integer", "Department_Sales"),
])

output_schema = Schema([ColSpec("boolean")])
signature = ModelSignature(inputs=input_schema, outputs=output_schema)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_data", dest="input_data", required=True, type=str)
    parser.add_argument("--model_dir", dest="model_dir", required=True, type=str)
    parser.add_argument("--reg", dest="reg", required=True, type=float, default=0.01)
    parser.add_argument("--solver", dest="solver", required=True, type=str, default="liblinear")
    return parser.parse_args()

def log_coef_plot(model: LogisticRegression, feature_names: list, output_dir: Path) -> None:
    """Lav et coefficients-plot og log det som MLflow-artefakt."""
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(feature_names, model.coef_[0])
    ax.set_title("Logistic Regression Coefficients")
    ax.set_xlabel("Feature")
    ax.set_ylabel("Coefficient")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plot_path = output_dir / "coef_plot.png"
    plt.savefig(str(plot_path))
    plt.close(fig)
    mlflow.log_artifact(str(plot_path))
    print(f"Coefficient plot logget: {plot_path}")

def main(args: argparse.Namespace) -> None:
    df = pd.read_csv(args.input_data)
    X = df.drop(columns=["Attrition"]).values
    y = df["Attrition"].values
    feature_names = df.drop(columns=["Attrition"]).columns.tolist()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
    C = 1.0 / float(args.reg)
    print(f"Training LogisticRegression with reg={args.reg}, C={C}")
    model = LogisticRegression(C=C, solver=args.solver).fit(X_train, y_train)
    y_hat = model.predict(X_test)
    acc = float(np.average(y_hat == y_test))
    print(f"Accuracy: {acc}")
    mlflow.log_param("reg", args.reg)
    mlflow.log_param("solver", args.solver)
    mlflow.log_metric("val_accuracy", acc)

    if len(np.unique(y_test)) == 2:
        y_scores = model.predict_proba(X_test)[:, 1]
        auc = float(roc_auc_score(y_test, y_scores))
        print(f"AUC: {auc}")
        mlflow.log_metric("val_auc", auc)

    out_dir = Path(args.model_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    mlflow.sklearn.log_model(model, artifact_path="model", signature=signature)
    log_coef_plot(model, feature_names, out_dir)

if __name__ == "__main__":
    args = parse_args()
    main(args)
