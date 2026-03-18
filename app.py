
# ================================
# IMPORT LIBRARIES
# ================================

import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# ================================
# PAGE CONFIG
# ================================

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)


# ================================
# LOAD DATA & MODEL
# ================================

df = pd.read_csv("cleaned_data.csv")

with open("Log_model.joblib", "rb") as file:
    model = joblib.load(file)


# ================================
# SIDEBAR
# ================================

st.sidebar.title("❤️ Heart Disease Prediction")
st.sidebar.image("logo image.png")


st.sidebar.markdown("---")
st.sidebar.subheader("Model Performance")
st.sidebar.write("Model : Logistic Regression")
st.sidebar.write("Accuracy : ~86%")
st.sidebar.write("Dataset Size :", len(df))

tab1, tab2, tab3, tab4 = st.tabs(["Prediction", "Dataset Insights", "Model Info", "About"])
# ================================
# PAGE 1 : PREDICTION
# ================================

with tab1:

    st.title("❤️ Heart Disease Prediction System")

    st.markdown("""
    This **Machine Learning application** predicts the **risk of heart disease**
    based on medical parameters such as age, cholesterol, blood pressure and ECG.

    🔹 Built with **Machine Learning + Streamlit**  
    🔹 Helps in **early risk detection**
    """)

    st.markdown("---")

    # ================================
    # INPUT FIELDS
    # ================================

    with st.container(border=True):

        col1, col2 = st.columns(2)

        with col1:

            age = st.number_input("Age", min_value=1, max_value=100, step=1)

            gender = st.radio(
                "Gender",
                options=["Male", "Female"],
                horizontal=True
            )

            gender = 1 if gender == "Male" else 0

            cp_dict = {
                "Typical angina": 0,
                "Atypical angina": 1,
                "Non-anginal pain": 2,
                "Asymptomatic": 3
            }

            chest_pain_type = st.selectbox(
                "Chest Pain Type",
                options=list(cp_dict.keys())
            )

            chest_pain_type = cp_dict[chest_pain_type]

            resting_bp = st.number_input(
                "Resting Blood Pressure",
                min_value=50,
                max_value=250,
                step=5
            )

            cholesterol = st.number_input(
                "Cholesterol",
                min_value=50,
                max_value=600,
                step=10
            )

            fbs = st.radio(
                "Fasting Blood Sugar > 120",
                options=["Yes", "No"],
                horizontal=True
            )

            fbs = 1 if fbs == "Yes" else 0

        with col2:

            ecg_dict = {
                "Normal": 0,
                "ST-T Wave Abnormality": 1,
                "Left Ventricular Hypertrophy": 2
            }

            restecg = st.selectbox(
                "Resting ECG",
                options=list(ecg_dict.keys())
            )

            restecg = ecg_dict[restecg]

            max_heart = st.number_input(
                "Maximum Heart Rate",
                min_value=50,
                max_value=250,
                step=1
            )

            exang = st.radio(
                "Exercise Induced Angina",
                options=["Yes", "No"],
                horizontal=True
            )

            exang = 1 if exang == "Yes" else 0

            oldpeak = st.number_input(
                "Oldpeak (ST Depression)",
                min_value=0.0,
                max_value=10.0,
                step=0.1
            )

            slope_dict = {
                "Upsloping": 0,
                "Flat": 1,
                "Downsloping": 2
            }

            slope = st.selectbox(
                "Slope",
                options=list(slope_dict.keys())
            )

            slope = slope_dict[slope]

            num_vessels = st.selectbox(
                "Number of Major Vessels",
                options=[0, 1, 2, 3]
            )

            thal_dict = {
                "Normal": 1,
                "Fixed Defect": 2,
                "Reversible Defect": 3
            }

            thal = st.selectbox(
                "Thal",
                options=list(thal_dict.keys())
            )

            thal = thal_dict[thal]


    # ================================
    # PREDICTION
    # ================================

    if st.button("Predict Heart Disease Risk"):

        data = [[
            age, gender, chest_pain_type, resting_bp,
            cholesterol, fbs, restecg, max_heart,
            exang, oldpeak, slope, num_vessels, thal
        ]]

        pred = model.predict(data)[0]
        prob = model.predict_proba(data)[0][1]

        st.markdown("---")

        st.subheader("Patient Summary")

        with st.container(border=True):

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Age", age)
                st.metric("Cholesterol", cholesterol)

            with col2:
                st.metric("Gender", "Male" if gender==1 else "Female")
                st.metric("Resting BP", resting_bp)

        # Risk Probability
        st.metric(
            "Heart Disease Risk Probability",
            f"{round(prob * 100, 2)} %"
        )

        st.markdown("---")

        # Prediction Result
        if pred == 0:

            st.success("✅ LOW RISK OF HEART DISEASE")
            st.image("image1.png", width=200)
            st.balloons()

        else:

            st.error("⚠️ HIGH RISK OF HEART DISEASE")
            st.image("heart1.jpeg", width=200)

            st.warning("""
            **Health Recommendations**

            • Consult a cardiologist  
            • Maintain healthy diet  
            • Exercise regularly  
            • Reduce cholesterol intake  
            • Avoid smoking and alcohol
            """)

        # Download Report
        report = f"""
        HEART DISEASE REPORT

        Age : {age}
        Gender : {gender}
        Cholesterol : {cholesterol}
        Resting BP : {resting_bp}

        Risk Probability : {round(prob*100,2)} %

        Prediction : {"High Risk" if pred==1 else "Low Risk"}
        """

        st.download_button(
            "Download Report",
            report,
            file_name="heart_disease_report.txt"
        )


# ================================
# PAGE 2 : DATASET INSIGHTS
# ================================

with tab2:

    st.title("📊 Dataset Insights")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.markdown("---")

    st.subheader("Age Distribution")

    fig, ax = plt.subplots()
    ax.hist(df["age"], bins=20)
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")

    st.pyplot(fig)

    st.subheader("Cholesterol Distribution")

    fig, ax = plt.subplots()
    ax.hist(df["cholestrol"], bins=20)
    ax.set_xlabel("Cholesterol")
    ax.set_ylabel("Count")

    st.pyplot(fig)


# ================================
# PAGE 3 : MODEL INFO
# ================================

with tab3:

    st.title("🧠 Model Information")

    st.write("""
    **Algorithm Used : Logistic Regression**

    Logistic Regression is a supervised machine learning algorithm used
    for binary classification problems.

    In this project it predicts whether a patient has **heart disease risk**
    based on medical parameters.
    """)

    st.subheader("Feature Importance")

    try:

        importance = model.coef_[0]
        features = df.drop("target", axis=1).columns

        fig, ax = plt.subplots()

        ax.barh(features, importance)

        st.pyplot(fig)

    except:
        st.info("Feature importance not available for this model.")


# ================================
# PAGE 4 : ABOUT
# ================================

with tab4:

    st.title("ℹ️ About Project")

    st.write("""
    **Heart Disease Prediction System**

    This project uses **Machine Learning** to predict the risk of heart disease.

    Technologies Used:

    • Python  
    • Scikit-learn  
    • Pandas  
    • Streamlit  
    • Matplotlib

    The goal is to assist in **early detection of heart disease risk**
    using patient medical data.
    """)
