import argparse
from pathlib import Path
import pandas as pd
import mlflow


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_data", dest="input_data", required=True, type=str)
    parser.add_argument("--output_data", dest="output_data", required=True, type=str)
    return parser.parse_args()

def main(args: argparse.Namespace) -> None:

    def _make_dummies(df: pd.DataFrame, categorical_columns: list) -> pd.DataFrame:
        for col in categorical_columns:
            dummies = pd.get_dummies(df[col], prefix=col)
            df = pd.concat([df, dummies], axis=1)
        df.drop(columns=categorical_columns, inplace=True)
        return df

    df = pd.read_csv(args.input_data)

    keep_cols = [
        "Attrition", "Age", "Gender", "Department", 
        "WorkLifeBalance", "YearsSinceLastPromotion", 
        "JobInvolvement", "YearsAtCompany", "MonthlyIncome"
    ]
    df = df[keep_cols]
    df = _make_dummies(df, ["Gender", "Department"])

    mlflow.log_metric("n_rows", df.shape[0])
    mlflow.log_metric("n_cols", df.shape[1])

    out_dir = Path(args.output_data)
    out_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_dir / "prepped.csv")

if __name__ == "__main__":
    args = parse_args()
    main(args)
