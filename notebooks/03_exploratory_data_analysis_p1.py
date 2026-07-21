# =========================================================
# Import Libraries
# =========================================================

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# =========================================================
# Pandas Display Settings
# =========================================================

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

# =========================================================
# Project Paths
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "data" / "processed" / "customer_churn_cleaned.csv"

FIGURE_PATH = BASE_DIR / "reports" / "figures"

FIGURE_PATH.mkdir(parents=True, exist_ok=True)

# =========================================================
# Load Dataset
# =========================================================

print("="*60)
print("Loading Dataset...")
print("="*60)

df = pd.read_csv(INPUT_PATH)

print("Dataset Loaded Successfully")

print()

# =========================================================
# Dataset Overview
# =========================================================

print("="*60)
print("Dataset Shape")
print("="*60)

print(df.shape)

print()

print("="*60)
print("Dataset Information")
print("="*60)

print(df.info())

print()

# =========================================================
# Helper Function
# =========================================================

def save_plot(file_name):

    plt.tight_layout()

    plt.savefig(
        FIGURE_PATH / file_name,
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

# =========================================================
# 1. Churn Distribution
# =========================================================

print("Generating Churn Distribution...")

plt.figure(figsize=(6,5))

sns.countplot(
    data=df,
    x="Churn Label"
)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

save_plot("01_churn_distribution.png")

print(df["Churn Label"].value_counts())

print()

# =========================================================
# 2. Gender Distribution
# =========================================================

print("Generating Gender Distribution...")

plt.figure(figsize=(6,5))

sns.countplot(
    data=df,
    x="Gender"
)

plt.title("Gender Distribution")

save_plot("02_gender_distribution.png")

print(df["Gender"].value_counts())

print()

# =========================================================
# 3. Contract Type Distribution
# =========================================================

print("Generating Contract Distribution...")

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="Contract",
    order=df["Contract"].value_counts().index
)

plt.xticks(rotation=20)

plt.title("Contract Type Distribution")

save_plot("03_contract_distribution.png")

print(df["Contract"].value_counts())

print()

# =========================================================
# 4. Payment Method Distribution
# =========================================================

print("Generating Payment Method Distribution...")

plt.figure(figsize=(10,5))

sns.countplot(
    data=df,
    x="Payment Method",
    order=df["Payment Method"].value_counts().index
)

plt.xticks(rotation=35)

plt.title("Payment Method")

save_plot("04_payment_method_distribution.png")

print()

# =========================================================
# 5. Internet Type Distribution
# =========================================================

print("Generating Internet Type Distribution...")

plt.figure(figsize=(7,5))

sns.countplot(
    data=df,
    x="Internet Type",
    order=df["Internet Type"].value_counts().index
)

plt.xticks(rotation=20)

plt.title("Internet Type")

save_plot("05_internet_type_distribution.png")

print()

# =========================================================
# 6. Customer Status Distribution
# =========================================================

print("Generating Customer Status Distribution...")

plt.figure(figsize=(7,5))

sns.countplot(
    data=df,
    x="Customer Status",
    order=df["Customer Status"].value_counts().index
)

plt.xticks(rotation=20)

plt.title("Customer Status")

save_plot("06_customer_status_distribution.png")

print()

# =========================================================
# 7. Age Distribution
# =========================================================

print("Generating Age Distribution...")

plt.figure(figsize=(8,5))

sns.histplot(
    data=df,
    x="Age",
    bins=20,
    kde=True
)

plt.title("Age Distribution")

save_plot("07_age_distribution.png")

print()

# =========================================================
# 8. Monthly Charge Distribution
# =========================================================

print("Generating Monthly Charge Distribution...")

plt.figure(figsize=(8,5))

sns.histplot(
    data=df,
    x="Monthly Charge",
    bins=30,
    kde=True
)

plt.title("Monthly Charges")

save_plot("08_monthly_charge_distribution.png")

print()

# =========================================================
# 9. Total Revenue Distribution
# =========================================================

print("Generating Revenue Distribution...")

plt.figure(figsize=(8,5))

sns.histplot(
    data=df,
    x="Total Revenue",
    bins=30,
    kde=True
)

plt.title("Total Revenue")

save_plot("09_total_revenue_distribution.png")

print()

# =========================================================
# 10. CLTV Distribution
# =========================================================

print("Generating CLTV Distribution...")

plt.figure(figsize=(8,5))

sns.histplot(
    data=df,
    x="CLTV",
    bins=30,
    kde=True
)

plt.title("Customer Lifetime Value")

save_plot("10_cltv_distribution.png")

print()

# =========================================================
# Numerical Summary
# =========================================================

print("="*60)
print("Numerical Summary")
print("="*60)

print(df.describe())

print()

# =========================================================
# Categorical Summary
# =========================================================

print("="*60)
print("Categorical Summary")
print("="*60)

print(df.describe(include="object"))

print()

print("="*60)
print("Part 1 Completed Successfully")
print("="*60)


# =========================================================
# PART 2 : Bivariate Analysis
# =========================================================

print("=" * 60)
print("PART 2 : Bivariate Analysis")
print("=" * 60)

# =========================================================
# 11. Churn by Gender
# =========================================================

print("Generating Churn by Gender...")

plt.figure(figsize=(7,5))

sns.countplot(
    data=df,
    x="Gender",
    hue="Churn Label"
)

plt.title("Churn by Gender")
plt.xlabel("Gender")
plt.ylabel("Customers")

save_plot("11_churn_by_gender.png")

print(
    pd.crosstab(
        df["Gender"],
        df["Churn Label"]
    )
)

print()


# =========================================================
# 12. Churn by Contract Type
# =========================================================

print("Generating Churn by Contract...")

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="Contract",
    hue="Churn Label"
)

plt.xticks(rotation=20)

plt.title("Churn by Contract")

save_plot("12_churn_by_contract.png")

print(
    pd.crosstab(
        df["Contract"],
        df["Churn Label"]
    )
)

print()


# =========================================================
# 13. Churn by Payment Method
# =========================================================

print("Generating Churn by Payment Method...")

plt.figure(figsize=(10,5))

sns.countplot(
    data=df,
    x="Payment Method",
    hue="Churn Label"
)

plt.xticks(rotation=35)

plt.title("Churn by Payment Method")

save_plot("13_churn_by_payment_method.png")

print()


# =========================================================
# 14. Churn by Internet Type
# =========================================================

print("Generating Churn by Internet Type...")

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="Internet Type",
    hue="Churn Label"
)

plt.xticks(rotation=20)

plt.title("Churn by Internet Type")

save_plot("14_churn_by_internet_type.png")

print()


# =========================================================
# 15. Satisfaction Score vs Churn
# =========================================================

print("Generating Satisfaction Score Analysis...")

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="Churn Label",
    y="Satisfaction Score"
)

plt.title("Satisfaction Score vs Churn")

save_plot("15_satisfaction_vs_churn.png")

print()


# =========================================================
# 16. Monthly Charge vs Churn
# =========================================================

print("Generating Monthly Charge Analysis...")

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="Churn Label",
    y="Monthly Charge"
)

plt.title("Monthly Charge vs Churn")

save_plot("16_monthly_charge_vs_churn.png")

print()


# =========================================================
# 17. Total Revenue vs Churn
# =========================================================

print("Generating Revenue Analysis...")

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="Churn Label",
    y="Total Revenue"
)

plt.title("Revenue vs Churn")

save_plot("17_revenue_vs_churn.png")

print()


# =========================================================
# 18. CLTV vs Churn
# =========================================================

print("Generating CLTV Analysis...")

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="Churn Label",
    y="CLTV"
)

plt.title("CLTV vs Churn")

save_plot("18_cltv_vs_churn.png")

print()


# =========================================================
# 19. Revenue by Contract
# =========================================================

print("Generating Revenue by Contract...")

plt.figure(figsize=(8,5))

sns.barplot(
    data=df,
    x="Contract",
    y="Total Revenue",
    estimator=np.mean
)

plt.title("Average Revenue by Contract")

save_plot("19_revenue_by_contract.png")

print()


# =========================================================
# 20. CLTV by Contract
# =========================================================

print("Generating CLTV by Contract...")

plt.figure(figsize=(8,5))

sns.barplot(
    data=df,
    x="Contract",
    y="CLTV",
    estimator=np.mean
)

plt.title("Average CLTV by Contract")

save_plot("20_cltv_by_contract.png")

print()


# =========================================================
# 21. Correlation Heatmap
# =========================================================

print("Generating Correlation Heatmap...")

numeric_df = df.select_dtypes(include=["int64", "float64"])

plt.figure(figsize=(16,10))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

save_plot("21_correlation_heatmap.png")

print()


# =========================================================
# 22. Outlier Detection
# =========================================================

print("Generating Outlier Analysis...")

numerical_columns = [

    "Age",
    "Monthly Charge",
    "Total Charges",
    "Total Revenue",
    "CLTV"

]

for column in numerical_columns:

    plt.figure(figsize=(8,4))

    sns.boxplot(
        x=df[column]
    )

    plt.title(f"Outlier Detection - {column}")

    save_plot(f"22_boxplot_{column}.png")

print()


# =========================================================
# 23. Churn Percentage
# =========================================================

print("=" * 60)
print("Churn Percentage")
print("=" * 60)

churn_percentage = round(
    df["Churn Label"].value_counts(normalize=True) * 100,
    2
)

print(churn_percentage)

print()


# =========================================================
# 24. Business Insights
# =========================================================

print("=" * 60)
print("Key Business Insights")
print("=" * 60)

print(f"Total Customers : {len(df):,}")

print(
    f"Churn Rate : "
    f"{round((df['Churn Label']=='Yes').mean()*100,2)}%"
)

print(
    f"Average Monthly Charge : "
    f"${df['Monthly Charge'].mean():.2f}"
)

print(
    f"Average Revenue : "
    f"${df['Total Revenue'].mean():.2f}"
)

print(
    f"Average CLTV : "
    f"${df['CLTV'].mean():.2f}"
)

print()


# =========================================================
# Completion
# =========================================================

print("=" * 60)
print("Part 2 Completed Successfully")
print("=" * 60)
