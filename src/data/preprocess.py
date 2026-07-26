"""
Data preprocessing functions for the
Customer Churn Prediction Platform.
"""

import pandas as pd

def load_data(filepath):
    """
    Load the Telco Customer Churn dataset.
    """

    df = pd.read_csv(filepath)

    return df

def clean_total_charges(df):
    """
    Convert TotalCharges into numeric values.
    """

    df = df.copy()

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    return df

def remove_duplicates(df):
    """
    Remove duplicate records.
    """

    df = df.drop_duplicates()

    return df


def preprocess_data(filepath):
    """
    Complete preprocessing pipeline.
    """

    df = load_data(filepath)

    df = clean_total_charges(df)

    df = remove_duplicates(df)

    return df

