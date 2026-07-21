# =====================================================
# Import Libraries
# =====================================================

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import (
    GridSearchCV,
    StratifiedKFold,
    cross_val_score
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

# =====================================================
# Optional XGBoost
# =====================================================

try:
    from xgboost import XGBClassifier
    XGBOOST_AVAILABLE = True
except ImportError:
    XGBOOST_AVAILABLE = False

# =====================================================
# Project Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"

MODEL_DIR = BASE_DIR / "models"

REPORT_DIR = BASE_DIR / "reports"

FIGURE_DIR = REPORT_DIR / "figures"

RESULT_DIR = REPORT_DIR / "model_results"

MODEL_DIR.mkdir(exist_ok=True)

REPORT_DIR.mkdir(exist_ok=True)

FIGURE_DIR.mkdir(exist_ok=True)

RESULT_DIR.mkdir(exist_ok=True)

# =====================================================
# Load Data
# =====================================================

print("="*70)
print("Loading Training Dataset")
print("="*70)

X_train = pd.read_csv(DATA_DIR / "X_train.csv")
X_test = pd.read_csv(DATA_DIR / "X_test.csv")

y_train = pd.read_csv(DATA_DIR / "y_train.csv").squeeze()
y_test = pd.read_csv(DATA_DIR / "y_test.csv").squeeze()

print("Training Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

print()

# =====================================================
# Cross Validation
# =====================================================

cv = StratifiedKFold(

    n_splits=3,

    shuffle=True,

    random_state=42

)

# =====================================================
# Model Definitions
# =====================================================

models = {

    "Logistic Regression": (

        LogisticRegression(),

        {

            "C":[0.01,0.1,1,10],

            "solver":["liblinear"]

        }

    ),

    "Decision Tree": (

        DecisionTreeClassifier(random_state=42),

        {

            "max_depth":[3,5,8,12],

            "min_samples_split":[2,5,10]

        }

    ),

    "Random Forest": (

        RandomForestClassifier(random_state=42),

        {

            "n_estimators":[100,200],

            "max_depth":[5,10,None]

        }

    ),

    "Gradient Boosting": (

        GradientBoostingClassifier(random_state=42, subsample=0.8),

        {

            "learning_rate":[0.05,0.1],

            "n_estimators":[50,100],

            "max_depth" : [3]

        }

    )

}

# =====================================================
# Optional XGBoost
# =====================================================

if XGBOOST_AVAILABLE:

    models["XGBoost"]=(

        XGBClassifier(

            eval_metric="logloss",

            random_state=42

        ),

        {

            "learning_rate":[0.01,0.1],

            "max_depth":[3,5],

            "n_estimators":[100,200]

        }

    )

print("="*70)
print("Models Ready")
print("="*70)

for model in models:

    print(model)

print()

# =====================================================
# Containers
# =====================================================

results=[]

best_model=None

best_model_name=""

best_auc=0

feature_importance=None

print("="*70)
print("Starting Model Training")
print("="*70)


# =====================================================
# Train Models
# =====================================================

for model_name, (model, params) in models.items():

    print("=" * 70)
    print(f"Training {model_name}")
    print("=" * 70)

    grid = GridSearchCV(
        estimator=model,
        param_grid=params,
        cv=cv,
        scoring="roc_auc",
        n_jobs=1,
        verbose=1
    )

    grid.fit(X_train, y_train)

    best_estimator = grid.best_estimator_

    print("Best Parameters:")
    print(grid.best_params_)

    # ==========================================
    # Predictions
    # ==========================================

    y_pred = best_estimator.predict(X_test)

    y_prob = best_estimator.predict_proba(X_test)[:, 1]

    # ==========================================
    # Metrics
    # ==========================================

    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(y_test, y_pred)

    recall = recall_score(y_test, y_pred)

    f1 = f1_score(y_test, y_pred)

    roc_auc = roc_auc_score(y_test, y_prob)

    cv_score = cross_val_score(
        best_estimator,
        X_train,
        y_train,
        cv=cv,
        n_jobs=1,
        scoring="roc_auc"
    ).mean()

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")
    print(f"ROC AUC  : {roc_auc:.4f}")
    print(f"CV Score : {cv_score:.4f}")

    # ==========================================
    # Store Results
    # ==========================================

    results.append({

        "Model": model_name,

        "Accuracy": round(accuracy, 4),

        "Precision": round(precision, 4),

        "Recall": round(recall, 4),

        "F1 Score": round(f1, 4),

        "ROC AUC": round(roc_auc, 4),

        "Cross Validation": round(cv_score, 4)

    })

    # ==========================================
    # Save Best Model
    # ==========================================

    if grid.best_score_ > best_auc:

        best_auc = grid.best_score_

        best_model = best_estimator

        best_model_name = model_name

print(f"Best CV ROC-AUC : {best_auc:.4f}")
print(f"Test ROC-AUC    : {roc_auc:.4f}")

# =====================================================
# Model Comparison
# =====================================================

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="ROC AUC",
    ascending=False
)

print()
print("=" * 70)
print("Model Comparison")
print("=" * 70)

print(results_df)

results_df.to_csv(
    RESULT_DIR / "model_comparison.csv",
    index=False
)

# =====================================================
# Save Best Model
# =====================================================

print()
print("=" * 70)
print("Saving Best Model")
print("=" * 70)

joblib.dump(
    best_model,
    MODEL_DIR / "best_model.pkl"
)

print(f"Best Model : {best_model_name}")

print(f"ROC AUC    : {best_auc:.4f}")

# =====================================================
# Save Feature Importance
# =====================================================

importance = None

# Tree Models
if hasattr(best_model, "feature_importances_"):

    importance = pd.DataFrame({

        "Feature": X_train.columns,

        "Importance": best_model.feature_importances_

    })

# Logistic Regression
elif hasattr(best_model, "coef_"):

    importance = pd.DataFrame({

        "Feature": X_train.columns,

        "Importance": abs(best_model.coef_[0])

    })

# =====================================================
# Save Importance CSV
# =====================================================

if importance is not None:

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    importance.to_csv(
        RESULT_DIR / "feature_importance.csv",
        index=False
    )

    print()
    print("=" * 70)
    print("Top 20 Important Features")
    print("=" * 70)

    print(importance.head(20))

print()

print("=" * 70)
print("Part 2 Completed Successfully")
print("=" * 70)
