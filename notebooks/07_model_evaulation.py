# =====================================================
# Import Libraries
# =====================================================

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import joblib
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (

    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
    balanced_accuracy_score,
    matthews_corrcoef,

    confusion_matrix,
    classification_report,

    roc_curve,
    precision_recall_curve

)

from sklearn.calibration import calibration_curve

# Optional SHAP

try:

    import shap

    SHAP_AVAILABLE = True

except ImportError:

    SHAP_AVAILABLE = False

# =====================================================
# Project Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"

MODEL_DIR = BASE_DIR / "models"

REPORT_DIR = BASE_DIR / "reports"

FIGURE_DIR = REPORT_DIR / "figures"

RESULT_DIR = REPORT_DIR / "model_results"

REPORT_DIR.mkdir(exist_ok=True)

FIGURE_DIR.mkdir(exist_ok=True)

RESULT_DIR.mkdir(exist_ok=True)

# =====================================================
# Load Model
# =====================================================

print("=" * 70)
print("Loading Best Model")
print("=" * 70)

model = joblib.load(

    MODEL_DIR / "best_model.pkl"

)

feature_names = joblib.load(

    MODEL_DIR / "feature_names.pkl"

)

print("✓ Best Model Loaded")

print("✓ Feature Names Loaded")

print()

# =====================================================
# Load Test Dataset
# =====================================================

print("=" * 70)
print("Loading Test Dataset")
print("=" * 70)

X_test = pd.read_csv(

    DATA_DIR / "X_test.csv"

)

y_test = pd.read_csv(

    DATA_DIR / "y_test.csv"

).squeeze()

print(f"Test Samples : {len(X_test)}")

print(f"Features     : {X_test.shape[1]}")

print()

# =====================================================
# Model Information
# =====================================================

print("=" * 70)
print("Model Information")
print("=" * 70)

print(model)

print()

# =====================================================
# Prediction
# =====================================================

print("=" * 70)
print("Generating Predictions")
print("=" * 70)

y_pred = model.predict(

    X_test

)

y_prob = model.predict_proba(

    X_test

)[:, 1]

print("✓ Predictions Generated")

print()


# =====================================================
# Evaluate Model
# =====================================================

print("=" * 70)
print("Evaluating Model")
print("=" * 70)

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred
)

recall = recall_score(
    y_test,
    y_pred
)

f1 = f1_score(
    y_test,
    y_pred
)

roc_auc = roc_auc_score(
    y_test,
    y_prob
)

pr_auc = average_precision_score(
    y_test,
    y_prob
)

balanced_acc = balanced_accuracy_score(
    y_test,
    y_pred
)

mcc = matthews_corrcoef(
    y_test,
    y_pred
)

print(f"Accuracy              : {accuracy:.4f}")
print(f"Precision             : {precision:.4f}")
print(f"Recall                : {recall:.4f}")
print(f"F1 Score              : {f1:.4f}")
print(f"ROC AUC               : {roc_auc:.4f}")
print(f"PR AUC                : {pr_auc:.4f}")
print(f"Balanced Accuracy     : {balanced_acc:.4f}")
print(f"Matthews Correlation  : {mcc:.4f}")

print()

# =====================================================
# Save Evaluation Metrics
# =====================================================

print("=" * 70)
print("Saving Evaluation Metrics")
print("=" * 70)

metrics_df = pd.DataFrame({

    "Metric":[

        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC",
        "PR AUC",
        "Balanced Accuracy",
        "Matthews Correlation"

    ],

    "Value":[

        round(accuracy,4),
        round(precision,4),
        round(recall,4),
        round(f1,4),
        round(roc_auc,4),
        round(pr_auc,4),
        round(balanced_acc,4),
        round(mcc,4)

    ]

})

metrics_df.to_csv(

    RESULT_DIR / "evaluation_metrics.csv",

    index=False

)

print("✓ evaluation_metrics.csv saved")

print()

# =====================================================
# Classification Report
# =====================================================

print("=" * 70)
print("Generating Classification Report")
print("=" * 70)

report = classification_report(

    y_test,

    y_pred,

    output_dict=True

)

report_df = pd.DataFrame(report).transpose()

report_df.to_csv(

    RESULT_DIR / "classification_report.csv"

)

print(report_df)

print()

print("✓ classification_report.csv saved")

print()

# =====================================================
# Confusion Matrix
# =====================================================

cm = confusion_matrix(

    y_test,

    y_pred

)

cm_df = pd.DataFrame(

    cm,

    index=[

        "Actual No",

        "Actual Yes"

    ],

    columns=[

        "Predicted No",

        "Predicted Yes"

    ]

)

cm_df.to_csv(

    RESULT_DIR / "confusion_matrix.csv"

)

print("✓ confusion_matrix.csv saved")

print()

# =====================================================
# Evaluation Summary
# =====================================================

print("=" * 70)
print("Evaluation Summary")
print("=" * 70)

print(metrics_df)

print()


# =====================================================
# Generate Evaluation Visualizations
# =====================================================

print("=" * 70)
print("Generating Evaluation Visualizations")
print("=" * 70)

# =====================================================
# Confusion Matrix Plot
# =====================================================

plt.figure(figsize=(6, 5))

sns.heatmap(

    cm,

    annot=True,

    fmt="d",

    cmap="Blues",

    cbar=False,

    xticklabels=["No Churn", "Churn"],

    yticklabels=["No Churn", "Churn"]

)

plt.title("Confusion Matrix")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.tight_layout()

plt.savefig(

    FIGURE_DIR / "confusion_matrix.png",

    dpi=300,

    bbox_inches="tight"

)

plt.close()

print("✓ confusion_matrix.png saved")

# =====================================================
# ROC Curve
# =====================================================

fpr, tpr, _ = roc_curve(

    y_test,

    y_prob

)

plt.figure(figsize=(7,6))

plt.plot(

    fpr,

    tpr,

    linewidth=2,

    label=f"AUC = {roc_auc:.3f}"

)

plt.plot(

    [0,1],

    [0,1],

    linestyle="--"

)

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve")

plt.legend()

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(

    FIGURE_DIR / "roc_curve.png",

    dpi=300,

    bbox_inches="tight"

)

plt.close()

print("✓ roc_curve.png saved")

# =====================================================
# Precision Recall Curve
# =====================================================

precision_curve, recall_curve, _ = precision_recall_curve(

    y_test,

    y_prob

)

plt.figure(figsize=(7,6))

plt.plot(

    recall_curve,

    precision_curve,

    linewidth=2

)

plt.xlabel("Recall")

plt.ylabel("Precision")

plt.title("Precision-Recall Curve")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(

    FIGURE_DIR / "precision_recall_curve.png",

    dpi=300,

    bbox_inches="tight"

)

plt.close()

print("✓ precision_recall_curve.png saved")

# =====================================================
# Calibration Curve
# =====================================================

prob_true, prob_pred = calibration_curve(

    y_test,

    y_prob,

    n_bins=10

)

plt.figure(figsize=(7,6))

plt.plot(

    prob_pred,

    prob_true,

    marker="o",

    linewidth=2,

    label="Model"

)

plt.plot(

    [0,1],

    [0,1],

    linestyle="--",

    label="Perfect Calibration"

)

plt.xlabel("Mean Predicted Probability")

plt.ylabel("Observed Probability")

plt.title("Calibration Curve")

plt.legend()

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(

    FIGURE_DIR / "calibration_curve.png",

    dpi=300,

    bbox_inches="tight"

)

plt.close()

print("✓ calibration_curve.png saved")

print()

print("=" * 70)
print("Evaluation Plots Generated Successfully")
print("=" * 70)

print()

# =====================================================
# Feature Importance
# =====================================================

print("=" * 70)
print("Generating Feature Importance")
print("=" * 70)

importance = None

# Tree Models
if hasattr(model, "feature_importances_"):

    importance = pd.DataFrame({

        "Feature": feature_names,
        "Importance": model.feature_importances_

    })

# Logistic Regression
elif hasattr(model, "coef_"):

    importance = pd.DataFrame({

        "Feature": feature_names,
        "Importance": abs(model.coef_[0])

    })

if importance is not None:

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    importance.to_csv(
        RESULT_DIR / "feature_importance.csv",
        index=False
    )

    plt.figure(figsize=(10,8))

    sns.barplot(

        data=importance.head(20),

        x="Importance",

        y="Feature"

    )

    plt.title("Top 20 Feature Importance")

    plt.tight_layout()

    plt.savefig(

        FIGURE_DIR / "feature_importance.png",

        dpi=300,

        bbox_inches="tight"

    )

    plt.close()

    print("✓ feature_importance.csv saved")

    print("✓ feature_importance.png saved")

else:

    print("Feature Importance not available.")


# =====================================================
# SHAP Explainability (Optional)
# =====================================================

print()
print("=" * 70)
print("SHAP Explainability")
print("=" * 70)

try:

    import shap

    print("Generating SHAP Values...")

    # Sample for speed
    X_sample = X_test.sample(
        min(500, len(X_test)),
        random_state=42
    )

    if hasattr(model, "feature_importances_"):

        explainer = shap.TreeExplainer(model)

        shap_values = explainer.shap_values(X_sample)

        plt.figure(figsize=(12,8))

        shap.summary_plot(
            shap_values,
            X_sample,
            show=False
        )

        plt.tight_layout()

        plt.savefig(
            FIGURE_DIR / "shap_summary.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print("✓ SHAP Summary Saved")

    elif hasattr(model, "coef_"):

        explainer = shap.LinearExplainer(
            model,
            X_sample
        )

        shap_values = explainer.shap_values(X_sample)

        plt.figure(figsize=(12,8))

        shap.summary_plot(
            shap_values,
            X_sample,
            show=False
        )

        plt.tight_layout()

        plt.savefig(
            FIGURE_DIR / "shap_summary.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print("✓ SHAP Summary Saved")

    else:

        print("SHAP not supported for this model.")

except Exception:

    print("SHAP library not installed. Skipping...")

print()

# =====================================================
# Save Evaluation Summary
# =====================================================

summary = pd.DataFrame({

    "Metric":[

        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC"

    ],

    "Value":[

        round(accuracy,4),
        round(precision,4),
        round(recall,4),
        round(f1,4),
        round(roc_auc,4)

    ]

})

summary.to_csv(

    RESULT_DIR / "evaluation_summary.csv",

    index=False

)


# =====================================================
# Generated Files
# =====================================================

print("=" * 70)
print("Generated Files")
print("=" * 70)

generated = [

    "evaluation_metrics.csv",
    "classification_report.csv",
    "confusion_matrix.csv",
    "evaluation_summary.csv",
    "feature_importance.csv",

    "confusion_matrix.png",
    "roc_curve.png",
    "precision_recall_curve.png",
    "calibration_curve.png",
    "feature_importance.png"

]

if importance is not None:

    generated.append("feature_importance.png")

try:
    import shap
    generated.append("shap_summary.png")
except:
    pass

for file in generated:

    print(f"✓ {file}")

print()

print("=" * 70)
print("Model Evaluation Completed Successfully")
print("=" * 70)
