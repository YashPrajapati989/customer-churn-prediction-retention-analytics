# =====================================================
# Import Libraries
# =====================================================

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import joblib
import pandas as pd

# =====================================================
# Project Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "models"

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PREDICTION_FILE = DATA_DIR / "prediction_input.csv"

RAW_FILE = RAW_DATA_DIR / "telco.csv"

OUTPUT_FILE = DATA_DIR / "prediction_output.csv"

# =====================================================
# Select Input File
# =====================================================

if PREDICTION_FILE.exists():

    INPUT_FILE = PREDICTION_FILE

else:

    INPUT_FILE = RAW_FILE

# =====================================================
# Load Saved Artifacts
# =====================================================

print("=" * 70)
print("Loading Saved Model & Preprocessing Objects")
print("=" * 70)

model = joblib.load(
    MODEL_DIR / "best_model.pkl"
)

scaler = joblib.load(
    MODEL_DIR / "scaler.pkl"
)

feature_names = joblib.load(
    MODEL_DIR / "feature_names.pkl"
)

label_encoders = joblib.load(
    MODEL_DIR / "label_encoders.pkl"
)

categorical_columns = joblib.load(
    MODEL_DIR / "categorical_columns.pkl"
)

numeric_columns = joblib.load(
    MODEL_DIR / "numeric_columns.pkl"
)

print("✓ Best Model Loaded")
print("✓ StandardScaler Loaded")
print("✓ Feature Names Loaded")
print("✓ Label Encoders Loaded")
print("✓ Categorical Columns Loaded")
print("✓ Numeric Columns Loaded")

print()

# =====================================================
# Load Dataset
# =====================================================

print("=" * 70)
print("Loading Prediction Dataset")
print("=" * 70)

if not INPUT_FILE.exists():

    raise FileNotFoundError(

        f"\nInput file not found:\n{INPUT_FILE}"

    )

df = pd.read_csv(INPUT_FILE)

print(f"Loaded File : {INPUT_FILE.name}")

print(f"Dataset Shape : {df.shape}")

print()

# =====================================================
# Store Original Dataset
# =====================================================

original_df = df.copy()

# =====================================================
# Remove Target Column (if present)
# =====================================================

if "Churn Label" in df.columns:

    df.drop(
        columns="Churn Label",
        inplace=True
    )

# =====================================================
# Remove Leakage & Unused Columns
# =====================================================

print("=" * 70)
print("Removing Unnecessary Columns")
print("=" * 70)

drop_columns = [

    "Customer ID",

    "Customer Status",

    "Churn Score",

    "Churn Category",

    "Churn Reason",

    "Satisfaction Score",

    "City",

    "Zip Code",

    "Latitude",

    "Longitude",

    "Country"

]

existing_columns = [

    col

    for col in drop_columns

    if col in df.columns

]

df.drop(

    columns=existing_columns,

    inplace=True

)

print(f"Columns Removed : {len(existing_columns)}")

for col in existing_columns:

    print(f"✓ {col}")

print()

# =====================================================
# Dataset Information
# =====================================================

print("=" * 70)
print("Dataset Ready for Encoding")
print("=" * 70)

print(df.shape)

print(df.columns.tolist())

print()


# =====================================================
# Remove Unnecessary Columns
# =====================================================

drop_columns = [

    "Customer ID",
    "Customer Status",
    "Churn Score",
    "Churn Category",
    "Churn Reason",
    "Satisfaction Score",
    "City",
    "Zip Code",
    "Latitude",
    "Longitude",
    "Country",
    "Churn Label"

]

existing_columns = [

    col for col in drop_columns

    if col in df.columns

]

df.drop(
    columns=existing_columns,
    inplace=True
)

# =====================================================
# Binary Encoding
# =====================================================

print("=" * 70)
print("Encoding Binary Columns")
print("=" * 70)

for column, encoder in label_encoders.items():

    if column in df.columns:

        df[column] = encoder.transform(df[column])

print("✓ Binary Encoding Completed")

print()

# =====================================================
# One-Hot Encoding
# =====================================================

print("=" * 70)
print("One-Hot Encoding Remaining Categorical Variables")
print("=" * 70)

df = pd.get_dummies(

    df,

    columns=categorical_columns,

    drop_first=True,

    dtype=int

)

print("✓ One-Hot Encoding Completed")

print()

# =====================================================
# Align Features with Training Data
# =====================================================

print("=" * 70)
print("Aligning Features")
print("=" * 70)

for column in feature_names:

    if column not in df.columns:

        df[column] = 0

# Remove unexpected columns
extra_columns = [

    col for col in df.columns

    if col not in feature_names

]

if len(extra_columns) > 0:

    df.drop(columns=extra_columns, inplace=True)

# Keep same feature order
df = df[feature_names]

print(f"Final Dataset Shape : {df.shape}")

print()

# =====================================================
# Scale Numerical Features
# =====================================================

print("=" * 70)
print("Scaling Numerical Features")
print("=" * 70)

df[numeric_columns] = scaler.transform(
    df[numeric_columns]
)

print("✓ Scaling Completed")

print()


# =====================================================
# Predict Customer Churn
# =====================================================

print("=" * 70)
print("Predicting Customer Churn")
print("=" * 70)

predictions = model.predict(df)

probabilities = model.predict_proba(df)[:, 1]

print("✓ Prediction Completed")

print()

# =====================================================
# Prepare Output
# =====================================================

results = original_df.copy()

results["Prediction"] = predictions

results["Prediction"] = results["Prediction"].map({

    0: "No",

    1: "Yes"

})

results["Churn Probability"] = probabilities.round(4)

results["Risk Level"] = pd.cut(

    results["Churn Probability"],

    bins=[0.0, 0.30, 0.70, 1.0],

    labels=[

        "Low",

        "Medium",

        "High"

    ],

    include_lowest=True

)

# =====================================================
# Save Prediction Results
# =====================================================

results.to_csv(

    OUTPUT_FILE,

    index=False

)

# =====================================================
# Prediction Summary
# =====================================================

print("=" * 70)
print("Prediction Summary")
print("=" * 70)

print()

print(results[

    [

        "Prediction",

        "Churn Probability",

        "Risk Level"

    ]

].head())

print()

print(f"Total Customers      : {len(results)}")

print(f"Predicted Churn      : {(results['Prediction'] == 'Yes').sum()}")

print(f"Predicted Retained   : {(results['Prediction'] == 'No').sum()}")

print()

print("Risk Distribution")

print(results["Risk Level"].value_counts())

print()

print("=" * 70)
print("Prediction File Saved Successfully")
print("=" * 70)

print(OUTPUT_FILE)

print()

print("=" * 70)
print("Prediction Module Completed Successfully")
print("=" * 70)
