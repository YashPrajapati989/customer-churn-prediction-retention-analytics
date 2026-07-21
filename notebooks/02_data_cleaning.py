# =========================================================
# Import Libraries
# =========================================================

import pandas as pd
import numpy as np
from pathlib import Path

# =========================================================
# Pandas Display Settings
# =========================================================

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

# =========================================================
# Project Paths
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "data" / "processed" / "customer_churn_loaded.csv"
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "customer_churn_cleaned.csv"

# =========================================================
# Load Dataset
# =========================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(INPUT_PATH)

print("Dataset Loaded Successfully.\n")

# =========================================================
# Dataset Information
# =========================================================

print("=" * 60)
print("Dataset Shape")
print("=" * 60)

print(df.shape)

print("\n")

# =========================================================
# Check Missing Values
# =========================================================

print("=" * 60)
print("Missing Values")
print("=" * 60)

missing = pd.DataFrame({
    "Missing Values": df.isnull().sum(),
    "Percentage": round(df.isnull().mean() * 100, 2)
})

print(missing[missing["Missing Values"] > 0])

print("\n")

# =========================================================
# Handle Missing Values
# =========================================================

print("=" * 60)
print("Handling Missing Values")
print("=" * 60)

# Numerical Columns
numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in numerical_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].median())

# Categorical Columns
categorical_cols = df.select_dtypes(include=["object"]).columns

for col in categorical_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])

print("Missing Values Handled Successfully.\n")

# =========================================================
# Check Duplicate Records
# =========================================================

print("=" * 60)
print("Duplicate Records")
print("=" * 60)

duplicates = df.duplicated().sum()

print(f"Duplicate Rows Before Cleaning : {duplicates}")

df = df.drop_duplicates()

duplicates_after = df.duplicated().sum()

print(f"Duplicate Rows After Cleaning : {duplicates_after}")

print("\n")

# =========================================================
# Remove Extra Spaces
# =========================================================

print("=" * 60)
print("Removing Leading & Trailing Spaces")
print("=" * 60)

for col in categorical_cols:
    df[col] = df[col].astype(str).str.strip()

print("Completed.\n")

# =========================================================
# Convert Yes / No Columns
# =========================================================

print("=" * 60)
print("Standardizing Yes/No Columns")
print("=" * 60)

yes_no_columns = [
    "under_30",
    "senior_citizen",
    "married",
    "dependents",
    "referred_a_friend",
    "phone_service",
    "internet_service",
    "paperless_billing",
    "online_security",
    "online_backup",
    "device_protection_plan",
    "premium_tech_support",
    "streaming_tv",
    "streaming_movies",
    "streaming_music",
    "unlimited_data",
    "multiple_lines",
]

for col in yes_no_columns:
    if col in df.columns:
        df[col] = df[col].replace({
            "Yes": "Yes",
            "No": "No",
            "yes": "Yes",
            "no": "No"
        })

print("Completed.\n")

# =========================================================
# Validate Data Types
# =========================================================

print("=" * 60)
print("Data Types")
print("=" * 60)

print(df.dtypes)

print("\n")

# =========================================================
# Negative Value Check
# =========================================================

print("=" * 60)
print("Checking Negative Values")
print("=" * 60)

numeric_columns = [
    "age",
    "monthly_charge",
    "total_charges",
    "total_refunds",
    "total_extra_data_charges",
    "total_long_distance_charges",
    "total_revenue",
    "cltv"
]

for col in numeric_columns:

    if col in df.columns:

        count = (df[col] < 0).sum()

        print(f"{col:<35} : {count}")

print("\n")

# =========================================================
# Dataset Summary
# =========================================================

print("=" * 60)
print("Cleaned Dataset Summary")
print("=" * 60)

summary = pd.DataFrame({

    "Metric": [

        "Rows",
        "Columns",
        "Duplicate Rows",
        "Missing Values"

    ],

    "Value": [

        df.shape[0],
        df.shape[1],
        df.duplicated().sum(),
        df.isnull().sum().sum()

    ]

})

print(summary)

print("\n")

# =========================================================
# Save Clean Dataset
# =========================================================

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print("=" * 60)
print("Clean Dataset Saved Successfully")
print("=" * 60)

print(f"Location:\n{OUTPUT_PATH}")

print("\n")

# =========================================================
# Completion Message
# =========================================================

print("=" * 60)
print("Data Cleaning Completed Successfully")
print("=" * 60)
