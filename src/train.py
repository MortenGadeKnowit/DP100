import argparse
import joblib
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import mlflow
import mlflow.sklearn

def make_dummies(df: pd.DataFrame, categorical_columns: list[str]):
    for col in categorical_columns:
        temp = df[col]
        dummies = pd.get_dummies(temp, prefix=col)
        df = pd.concat([df, dummies], axis=1)

    df.drop(columns=categorical_columns, inplace=True)

    return df

def get_data(path):
    df = pd.read_csv(path)

    # Count the rows and print the result
    row_count = (len(df))
    print('Analyzing {} rows of data'.format(row_count))

    return df

def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--input_data", dest='input_data', type=str)
    parser.add_argument("--reg", dest='reg', type=float, default=0.01, help="Regularization rate (inverse used for C)")
    parser.add_argument("--model_dir", type=str, required=True, help="Directory to save model (AML output)")

    # parse args
    args = parser.parse_args()

    # return args
    return args

def main(args):
    mlflow.start_run()

    df = get_data(args.input_data)

    keep_cols = ['Attrition', 'Age','Gender','Department','WorkLifeBalance','YearsSinceLastPromotion','JobInvolvement','YearsAtCompany','MonthlyIncome']
    df_reduced = df[keep_cols]
    categorical_cols = ['Gender', 'Department']
    df_reduced = make_dummies(df_reduced, categorical_columns=categorical_cols)
    X, y = df_reduced.drop(columns=['Attrition']).values, df_reduced['Attrition'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

    # set regularization hyperparameter
    C = 1.0 / float(args.reg)

    # train a logistic regression model
    print('Training a logistic regression model with regularization rate of', args.reg)
    model = LogisticRegression(C=C, solver="liblinear").fit(X_train, y_train)

    # calculate accuracy
    y_hat = model.predict(X_test)
    acc = np.average(y_hat == y_test)
    print('Accuracy:', acc)
    mlflow.log_metric("val_accuracy", acc)

    # Log hyperparams explicitly
    mlflow.log_param("reg", args.reg)
    mlflow.log_param("C", C)


    # AUC (if binary)
    if len(np.unique(y_test)) == 2:
        y_scores = model.predict_proba(X_test)[:, 1]
        auc = float(roc_auc_score(y_test, y_scores))
        print('AUC:', auc)
        mlflow.log_metric("val_auc", auc)
    else:
        auc = None

    # Save model artifact to model_dir (AML output)
    out_dir = Path(args.model_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    model_path = out_dir / "model.joblib"
    joblib.dump(model, model_path)
    print(f"Saved model to {model_path}")

    # Also log model with MLflow (so it's visible in MLflow artifacts)
    mlflow.log_artifact(str(model_path), artifact_path="model_artifacts")

    mlflow.end_run()

if __name__ == "__main__":
    args = parse_args()
    main(args)
