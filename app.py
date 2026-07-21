import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import shap
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models"

REPORT_DIR = BASE_DIR / "reports" / "model_results"


# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="Customer Churn AI Analytics",
    page_icon="🤖",
    layout="wide"
)


# =====================================================
# Load Assets
# =====================================================

@st.cache_resource
def load_assets():
    try:
        model = joblib.load(MODEL_DIR / "best_model.pkl")
        feature_names = joblib.load(MODEL_DIR / "feature_names.pkl")
        label_encoders = joblib.load(MODEL_DIR / "label_encoders.pkl")
        categorical_columns = joblib.load(MODEL_DIR / "categorical_columns.pkl")
        numeric_columns = joblib.load(MODEL_DIR / "numeric_columns.pkl")
        scaler = joblib.load(MODEL_DIR / "scaler.pkl")

        explainer = shap.TreeExplainer(model)

        return (
            model,
            feature_names,
            label_encoders,
            categorical_columns,
            numeric_columns,
            scaler,
            explainer
        )

    except Exception as e:
        st.error(f"Unable to load model files: {e}")
        st.stop()



(
model,
feature_names,
label_encoders,
categorical_columns,
numeric_columns,
scaler,
explainer

)=load_assets()



# =====================================================
# Validation
# =====================================================

required_columns=[

    "Customer ID",
    "Gender",
    "Age",
    "Contract",
    "Internet Type",
    "Payment Method",
    "Tenure in Months",
    "Monthly Charge",
    "Total Charges"

]


def validate_dataset(df):

    errors=[]


    missing=set(required_columns)-set(df.columns)


    if missing:

        errors.append(
            f"Missing columns: {list(missing)}"
        )


    if len(df)==0:

        errors.append(
            "Dataset is empty"
        )


    return errors



# =====================================================
# Preprocessing
# =====================================================

def preprocess_data(df):

    df=df.copy()


    drop_columns=[

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


    df.drop(

        columns=[
            c for c in drop_columns
            if c in df.columns
        ],

        inplace=True

    )


    for col,encoder in label_encoders.items():

        if col in df.columns:

            df[col]=encoder.transform(
                df[col]
            )


    df=pd.get_dummies(

        df,

        columns=[
            c for c in categorical_columns
            if c in df.columns
        ],

        drop_first=True,

        dtype=int

    )



    for col in feature_names:

        if col not in df.columns:

            df[col]=0



    df=df[feature_names]


    df[numeric_columns]=scaler.transform(
        df[numeric_columns]
    )


    return df



# =====================================================
# Header
# =====================================================

st.title(
    "🤖 Customer Churn AI Analytics Dashboard"
)


st.markdown(
"""
### Explainable AI Customer Retention Platform

Features:

- Churn Prediction
- Customer Risk Segmentation
- SHAP Explainability
- Retention Recommendations

Model:
**Gradient Boosting Classifier**
"""
)



# =====================================================
# Upload Dataset
# =====================================================

uploaded_file=st.file_uploader(

    "Upload Telco Customer Churn CSV",

    type="csv"

)



if uploaded_file:


    raw_df=pd.read_csv(
        uploaded_file
    )

    st.subheader(
        "Dataset Preview"
    )

    st.dataframe(
        raw_df.head()
    )

    errors=validate_dataset(
        raw_df
    )

    if errors:
        st.error(
            "Dataset validation failed"
        )

        for error in errors:
            st.warning(error)
        st.stop()

    st.success(
        "Dataset validation successful"
    )

    # -----------------------------
    # Prediction
    # -----------------------------


    X=preprocess_data(
        raw_df
    )


    predictions=model.predict(
        X
    )


    probabilities=model.predict_proba(
        X
    )



    result=raw_df.copy()


    result["Prediction"]=predictions


    result["Churn Probability"]=(
        probabilities[:,1]*100
    ).round(2)



    result["Risk Level"]=pd.cut(

        result["Churn Probability"],

        bins=[0,30,70,100],

        labels=[
            "Low Risk",
            "Medium Risk",
            "High Risk"
        ]

    )



    # =====================================================
    # Tabs
    # =====================================================

    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(

    [

    "📊 Executive Overview",

    "🔮 Prediction Results",

    "⚠ Risk Analysis",

    "🧠 Model Insights",

    "🔍 Customer Explanation",

    "💡 Retention Strategy"

    ]

    )



    # =====================================================
    # Executive Overview
    # =====================================================

    with tab1:


        total=len(result)

        churn=int(
            result["Prediction"].sum()
        )

        retained=total-churn


        churn_rate=(
            churn/total
        )*100



        c1,c2,c3,c4=st.columns(4)



        c1.metric(
            "👥 Customers",
            f"{total:,}"
        )


        c2.metric(
            "⚠ Churn",
            f"{churn:,}"
        )


        c3.metric(
            "✅ Retained",
            f"{retained:,}"
        )


        c4.metric(
            "📉 Churn Rate",
            f"{churn_rate:.2f}%"
        )



    # =====================================================
    # Prediction Results
    # =====================================================

    with tab2:


        st.dataframe(
            result.head(100)
        )


        csv=result.to_csv(
            index=False
        )


        st.download_button(

            "Download Report",

            csv,

            "churn_predictions.csv"

        )



    # =====================================================
    # Risk Analysis
    # =====================================================

    with tab3:


        st.subheader(
            "Customer Risk Distribution"
        )


        st.bar_chart(

            result["Risk Level"]
            .value_counts()

        )



        st.subheader(
            "High Risk Customers"
        )


        high=result[

            result["Risk Level"]
            ==
            "High Risk"

        ]



        st.dataframe(

            high[
            [
            "Customer ID",
            "Churn Probability",
            "Risk Level"
            ]
            ]

        )



    # =====================================================
    # Model Insights + SHAP Global
    # =====================================================

    with tab4:
        st.subheader(
            "Feature Importance"
        )
        importance=pd.read_csv(
        REPORT_DIR / "feature_importance.csv"
        )
        st.bar_chart(
            importance.head(10)
            .set_index("Feature")
        )


        st.subheader(
            "SHAP Global Explanation"
        )
        sample=X.sample(
            min(500,len(X)),
            random_state=42
        )

        shap_values=explainer.shap_values(
            sample
        )

        shap_importance=pd.DataFrame({
            "Feature":
            sample.columns,
            "Impact":
            np.abs(
                shap_values
            ).mean(axis=0)
        })

        shap_importance=shap_importance.sort_values(
            "Impact",
            ascending=False
        )

        st.bar_chart(
            shap_importance.head(15)
            .set_index("Feature")
        )


    # =====================================================
    # Individual Explanation
    # =====================================================

    with tab5:


        st.header(
            "Why Will This Customer Churn?"
        )


        customer_index=st.selectbox(

            "Select Customer",

            result.index

        )



        customer_X=X.iloc[
            [customer_index]
        ]



        customer_probability=result.iloc[
            customer_index
        ]["Churn Probability"]



        st.metric(

            "Churn Probability",

            f"{customer_probability}%"

        )



        shap_value=explainer.shap_values(
            customer_X
        )



        explanation=pd.DataFrame({

            "Feature":
            customer_X.columns,

            "Impact":
            shap_value[0]

        })


        explanation["Magnitude"]=(
            explanation["Impact"]
            .abs()
        )


        explanation=explanation.sort_values(

            "Magnitude",

            ascending=False

        ).head(10)



        st.subheader(
            "Main Prediction Drivers"
        )


        st.bar_chart(

            explanation.set_index(
                "Feature"
            )["Impact"]

        )



    # =====================================================
    # Retention Strategy
    # =====================================================

    with tab6:


        st.markdown(
"""
## Retention Recommendations

### High Risk Customers

✅ Offer loyalty discounts

✅ Promote annual contracts

✅ Provide proactive support

✅ Review pricing concerns


### Medium Risk Customers

• Personalized campaigns

• Engagement offers

• Monitor behaviour


### Low Risk Customers

• Maintain relationship

• Encourage referrals

"""
        )



else:


    st.info(
        "Upload Telco Customer Churn CSV to start."
    )