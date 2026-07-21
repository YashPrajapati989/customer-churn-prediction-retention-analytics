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
pd.set_option("display.max_rows", 100)
pd.set_option("display.width", 1000)

# =========================================================
# Define Project Paths
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "telco.csv"
PROCESSED_DATA_PATH = (
    BASE_DIR / "data" / "processed" / "customer_churn_loaded.csv"
)

# =========================================================
# Load Dataset
# =========================================================

print("=" * 60)
print("Loading Customer Churn Dataset...")
print("=" * 60)

try:
    df = pd.read_csv(RAW_DATA_PATH)
    print("Dataset loaded successfully.\n")

except FileNotFoundError:
    print("ERROR: Dataset not found.")
    print(f"Expected location:\n{RAW_DATA_PATH}")
    exit()

# =========================================================
# Dataset Preview
# =========================================================

print("=" * 60)
print("First 5 Records")
print("=" * 60)

print(df.head())

print("\n")

print("=" * 60)
print("Last 5 Records")
print("=" * 60)

print(df.tail())

print("\n")

# =========================================================
# Dataset Shape
# =========================================================

rows, columns = df.shape

print("=" * 60)
print("Dataset Shape")
print("=" * 60)

print(f"Rows    : {rows}")
print(f"Columns : {columns}")

print("\n")

# =========================================================
# Column Names
# =========================================================

print("=" * 60)
print("Column Names")
print("=" * 60)

for column in df.columns:
    print(column)

print("\n")

# =========================================================
# Dataset Information
# =========================================================

print("=" * 60)
print("Dataset Information")
print("=" * 60)

df.info()

print("\n")

# =========================================================
# Data Types
# =========================================================

print("=" * 60)
print("Data Types")
print("=" * 60)

print(df.dtypes)

print("\n")

# =========================================================
# Numerical Summary
# =========================================================

print("=" * 60)
print("Numerical Summary")
print("=" * 60)

print(df.describe())

print("\n")

# =========================================================
# Categorical Summary
# =========================================================

print("=" * 60)
print("Categorical Summary")
print("=" * 60)

print(df.describe(include="object"))

print("\n")

# =========================================================
# Missing Values
# =========================================================

print("=" * 60)
print("Missing Values")
print("=" * 60)

missing_values = pd.DataFrame({

    "Missing Values": df.isnull().sum(),
    "Percentage": round(df.isnull().mean() * 100, 2)

})

print(
    missing_values.sort_values(
        by="Missing Values",
        ascending=False
    )
)

print("\n")

# =========================================================
# Duplicate Records
# =========================================================

duplicates = df.duplicated().sum()

print("=" * 60)
print("Duplicate Records")
print("=" * 60)

print(f"Duplicate Rows : {duplicates}")

print("\n")

# =========================================================
# Unique Values
# =========================================================

print("=" * 60)
print("Unique Values")
print("=" * 60)

unique_values = pd.DataFrame({

    "Unique Values": df.nunique()

})

print(unique_values.sort_values(by="Unique Values"))

print("\n")

# =========================================================
# Target Variable Distribution
# =========================================================

print("=" * 60)
print("Target Variable Distribution")
print("=" * 60)

print(df["Churn Label"].value_counts())

print("\n")

print("=" * 60)
print("Target Variable Percentage")
print("=" * 60)

print(round(df["Churn Label"].value_counts(normalize=True) * 100, 2))

print("\n")

# =========================================================
# Memory Usage
# =========================================================

memory = df.memory_usage(deep=True).sum() / 1024**2

print("=" * 60)
print("Memory Usage")
print("=" * 60)

print(f"Dataset Memory Usage : {memory:.2f} MB")

print("\n")

# =========================================================
# Dataset Summary
# =========================================================

summary = pd.DataFrame({

    "Metric": [

        "Rows",
        "Columns",
        "Duplicate Records",
        "Missing Values",
        "Memory Usage (MB)"

    ],

    "Value": [

        df.shape[0],
        df.shape[1],
        duplicates,
        df.isnull().sum().sum(),
        round(memory, 2)

    ]

})

print("=" * 60)
print("Dataset Summary")
print("=" * 60)

print(summary)

print("\n")

# =========================================================
# Save Loaded Dataset
# =========================================================

PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(PROCESSED_DATA_PATH, index=False)

print("=" * 60)
print("Dataset Saved Successfully")
print("=" * 60)

print(f"Location:\n{PROCESSED_DATA_PATH}")

print("\n")

# =========================================================
# Completion Message
# =========================================================

print("=" * 60)
print("Data Loading Completed Successfully")
print("=" * 60)
