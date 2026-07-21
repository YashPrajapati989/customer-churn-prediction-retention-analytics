# ==========================================================
# Import Libraries
# ==========================================================

import joblib
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = (
    BASE_DIR /
    "data" /
    "processed" /
    "customer_churn_cleaned.csv"
)

OUTPUT_DIR = (
    BASE_DIR /
    "data" /
    "processed"
)

MODEL_DIR = (
    BASE_DIR /
    "models"
)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MODEL_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Load Dataset
# ==========================================================

print("=" * 70)
print("Loading Clean Dataset")
print("=" * 70)

df = pd.read_csv(INPUT_PATH)

print(f"Dataset Shape : {df.shape}")
print()

# ==========================================================
# Dataset Information
# ==========================================================

print("=" * 70)
print("Dataset Information")
print("=" * 70)

df.info()
print()

# ==========================================================
# Remove Unnecessary Columns
# ==========================================================

print("=" * 70)
print("Removing Identifier, Leakage & High Cardinality Columns")
print("=" * 70)

drop_columns = [

    # Identifier
    "Customer ID",

    # Data Leakage
    "Customer Status",
    "Churn Score",
    "Churn Category",
    "Churn Reason",
    "Satisfaction Score",

    # High Cardinality
    "City",
    "Zip Code",
    "Latitude",
    "Longitude",
    "Country"

]

existing_columns = [

    col for col in drop_columns

    if col in df.columns

]

df.drop(
    columns=existing_columns,
    inplace=True
)

print("Dropped Columns")

for col in existing_columns:
    print(f"✓ {col}")

print()

# ==========================================================
# Remaining Columns
# ==========================================================

print("=" * 70)
print("Remaining Columns")
print("=" * 70)

print(df.columns.tolist())

print()

# ==========================================================
# Encode Target Variable
# ==========================================================

print("=" * 70)
print("Encoding Target Variable")
print("=" * 70)

df["Churn Label"] = df["Churn Label"].map({

    "No":0,

    "Yes":1

})

print(df["Churn Label"].value_counts())

print()

# ==========================================================
# Binary Encoding
# ==========================================================

print("=" * 70)
print("Encoding Binary Columns")
print("=" * 70)

binary_columns = []

label_encoders = {}

for column in df.select_dtypes(include="object").columns:

    if column == "Churn Label":
        continue

    if df[column].nunique() == 2:

        binary_columns.append(column)

for column in binary_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(df[column])

    label_encoders[column] = encoder

print(f"Binary Columns Encoded : {len(binary_columns)}")

print(binary_columns)

print()


# ==========================================================
# Save Label Encoders
# ==========================================================

print("=" * 70)
print("Saving Label Encoders")
print("=" * 70)

joblib.dump(

    label_encoders,

    MODEL_DIR / "label_encoders.pkl"

)

print("✅ label_encoders.pkl saved successfully")

print()


# ==========================================================
# One Hot Encoding
# ==========================================================

print("=" * 70)
print("One-Hot Encoding Remaining Categorical Variables")
print("=" * 70)

categorical_columns = df.select_dtypes(
    include="object"
).columns.tolist()

if "Churn Label" in categorical_columns:
    categorical_columns.remove("Churn Label")

joblib.dump(

    categorical_columns,

    MODEL_DIR / "categorical_columns.pkl"

)

print("✅ categorical_columns.pkl saved successfully")

print()

df = pd.get_dummies(

    df,

    columns=categorical_columns,

    drop_first=True,

    dtype=int

)

print("One-Hot Encoding Completed")

print(f"Dataset Shape After Encoding : {df.shape}")

print()

# ==========================================================
# Create Features & Target
# ==========================================================

print("=" * 70)
print("Creating Features & Target")
print("=" * 70)

X = df.drop(columns="Churn Label")

y = df["Churn Label"]

print(f"Feature Matrix Shape : {X.shape}")

print(f"Target Shape         : {y.shape}")

print()

# ==========================================================
# Feature Summary
# ==========================================================

print("=" * 70)
print("Feature Information")
print("=" * 70)

print(f"Total Features : {X.shape[1]}")

print()

# ==========================================================
# Leakage Check
# ==========================================================

print("=" * 70)
print("Checking Data Leakage")
print("=" * 70)

leakage_keywords = [

    "Customer Status",

    "Churn Score",

    "Churn Category",

    "Churn Reason"

]

leakage_found = False

for column in X.columns:

    for keyword in leakage_keywords:

        if keyword.lower() in column.lower():

            print(f"❌ Leakage Found : {column}")

            leakage_found = True

if not leakage_found:

    print("✅ No Leakage Columns Found")

print()

# ==========================================================
# Train Test Split
# ==========================================================

print("=" * 70)
print("Splitting Dataset")
print("=" * 70)

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

print(f"Training Samples : {len(X_train)}")

print(f"Testing Samples  : {len(X_test)}")

print()

# ==========================================================
# Scale Numerical Features
# ==========================================================

print("=" * 70)
print("Scaling Numerical Features")
print("=" * 70)

numeric_columns = [

    "Age",
    "Number of Dependents",
    "Population",
    "Number of Referrals",
    "Tenure in Months",
    "Avg Monthly Long Distance Charges",
    "Avg Monthly GB Download",
    "Monthly Charge",
    "Total Charges",
    "Total Refunds",
    "Total Extra Data Charges",
    "Total Long Distance Charges",
    "Total Revenue",
    "CLTV"

]

numeric_columns = [
    col for col in numeric_columns
    if col in X_train.columns
]

print(f"Numeric Features : {len(numeric_columns)}")

print()

# ==========================================================
# Save Numeric Columns
# ==========================================================

print("=" * 70)
print("Saving Numeric Columns")
print("=" * 70)

joblib.dump(

    numeric_columns,

    MODEL_DIR / "numeric_columns.pkl"

)

print("✅ numeric_columns.pkl saved successfully")

print()

scaler = StandardScaler()

X_train[numeric_columns] = scaler.fit_transform(

    X_train[numeric_columns]

).astype("float64")


X_test[numeric_columns] = scaler.transform(

    X_test[numeric_columns]

).astype("float64")

print("Scaling Completed Successfully")

print()

# ==========================================================
# Save Standard Scaler
# ==========================================================

print("=" * 70)
print("Saving StandardScaler")
print("=" * 70)

joblib.dump(

    scaler,

    MODEL_DIR / "scaler.pkl"

)

print("✅ scaler.pkl saved successfully")

print()

# ==========================================================
# Save Feature Names
# ==========================================================

print("=" * 70)
print("Saving Feature Names")
print("=" * 70)

joblib.dump(

    list(X_train.columns),

    MODEL_DIR / "feature_names.pkl"

)

print("✅ feature_names.pkl saved successfully")

print()


# ==========================================================
# Save Processed Files
# ==========================================================

print("=" * 70)
print("Saving Processed Datasets")
print("=" * 70)

X_train.to_csv(
    OUTPUT_DIR / "X_train.csv",
    index=False
)

X_test.to_csv(
    OUTPUT_DIR / "X_test.csv",
    index=False
)

y_train.to_csv(
    OUTPUT_DIR / "y_train.csv",
    index=False
)

y_test.to_csv(
    OUTPUT_DIR / "y_test.csv",
    index=False
)

print("✓ X_train.csv Saved")
print("✓ X_test.csv Saved")
print("✓ y_train.csv Saved")
print("✓ y_test.csv Saved")

print()

# ==========================================================
# Feature Engineering Summary
# ==========================================================

summary = pd.DataFrame({

    "Metric": [

        "Original Rows",
        "Original Columns",
        "Total Features",
        "Training Samples",
        "Testing Samples",
        "Numeric Features",
        "Binary Features",
        "Target Classes"

    ],

    "Value": [

        len(df),
        len(df.columns),
        X.shape[1],
        len(X_train),
        len(X_test),
        len(numeric_columns),
        len(binary_columns),
        y.nunique()

    ]

})

summary.to_csv(

    OUTPUT_DIR / "feature_engineering_summary.csv",

    index=False

)

print("=" * 70)
print("Feature Engineering Summary")
print("=" * 70)

print(summary)

print()

# ==========================================================
# Final Validation
# ==========================================================

print("=" * 70)
print("Final Validation")
print("=" * 70)

print(f"Missing Values (X_train): {X_train.isnull().sum().sum()}")

print(f"Missing Values (X_test) : {X_test.isnull().sum().sum()}")

print(f"Missing Values (y_train): {y_train.isnull().sum()}")

print(f"Missing Values (y_test) : {y_test.isnull().sum()}")

print()

print(f"Duplicate Rows (X_train): {X_train.duplicated().sum()}")

print(f"Duplicate Rows (X_test) : {X_test.duplicated().sum()}")

print()

print("Target Distribution")

print(y.value_counts())

print()

print("Target Percentage")

print(round(y.value_counts(normalize=True) * 100, 2))

print()

# ==========================================================
# Files Generated
# ==========================================================

print("=" * 70)
print("Generated Files")
print("=" * 70)

generated_files = [

    "X_train.csv",
    "X_test.csv",
    "y_train.csv",
    "y_test.csv",
    "feature_engineering_summary.csv",
    "scaler.pkl",
    "feature_names.pkl",
    "label_encoders.pkl",
    "categorical_columns.pkl",
    "numeric_columns.pkl"

]

for file in generated_files:

    print(f"✓ {file}")

print()

# ==========================================================
# Completion
# ==========================================================

print("=" * 70)
print("Feature Engineering Completed Successfully")
print("=" * 70)

print()

print("Dataset is Ready for Model Training.")

print()

