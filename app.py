import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import tempfile
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# ==================================================
# Page Configuration
# ==================================================
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="wide"
)

# ==================================================
# Custom CSS
# ==================================================
st.markdown("""
<style>
.main { background-color: #f8f9fa; }
.stMetric {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# Load Model & Scaler
# ==================================================
@st.cache_resource
def load_model():
    model = joblib.load("model/diabetes_model.pkl")
    scaler = joblib.load("model/scaler.pkl")
    return model, scaler

model, scaler = load_model()
# ==================================================
# Title
# ==================================================
st.title("🩺 Diabetes Prediction System")
st.write(
    "A **machine learning–based healthcare application** for "
    "**early diabetes prediction using Gradient Boosting.**"
)

st.divider()

# =================================================
# INPUT FORM
# ==================================================
with st.form("diabetes_form"):

    st.subheader("🧾 Patient Information")

    patient_name = st.text_input("Patient Name")

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        age = st.number_input("Age (years)", min_value=1, max_value=120)

    with col2:
        hypertension = st.selectbox("Hypertension", ["No", "Yes"])
        heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])

    with col3:
        smoking_history = st.selectbox(
            "Smoking History",
            ["No Info", "never", "former", "current"]
        )

    st.subheader("🧪 Clinical Measurements")

    col4, col5, col6 = st.columns(3)

    with col4:
        bmi = st.number_input("BMI", min_value=10.0, max_value=60.0)

    with col5:
        hba1c = st.number_input("HbA1c Level (%)", min_value=3.0, max_value=15.0)

    with col6:
        glucose = st.number_input(
            "Blood Glucose Level (mg/dL)", min_value=50, max_value=400
        )

    submit = st.form_submit_button("🔍 Predict Diabetes")

# ==================================================
# PDF GENERATOR
# ==================================================
def generate_pdf(data, prediction, probability):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(tmp.name, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "Diabetes Prediction Report")

    c.setFont("Helvetica", 12)
    y = 760
    for k, v in data.items():
        c.drawString(50, y, f"{k}: {v}")
        y -= 20

    c.drawString(50, y - 10,
                 f"Prediction: {'Diabetic' if prediction == 1 else 'Non-Diabetic'}")
    c.drawString(50, y - 40,
                 f"Probability: {probability * 100:.2f}%")

    c.drawString(50, y - 80,
                 "⚠ This report is for educational purposes only.")

    c.save()
    return tmp.name

# ==================================================
# PREDICTION
# ==================================================
if submit:
    try:
        input_dict = {
            'gender': [gender],
            'age': [age],
            'hypertension': [1 if hypertension == "Yes" else 0],
            'heart_disease': [1 if heart_disease == "Yes" else 0],
            'smoking_history': [smoking_history],
            'bmi': [bmi],
            'HbA1c_level': [hba1c],
            'blood_glucose_level': [glucose]
        }

        input_df = pd.DataFrame(input_dict)

        # Encoding
        input_df = pd.get_dummies(input_df)

        # Match training columns
        input_df = input_df.reindex(columns=scaler.feature_names_in_, fill_value=0)

        # Scaling
        scaled_input = scaler.transform(input_df)

        # Prediction
        prediction = model.predict(scaled_input)[0]
        probability = model.predict_proba(scaled_input)[0][1]

        st.divider()
        st.subheader(f"📌 Results for {patient_name}")

        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Results",
            "📈 Analysis",
            "🧾 Health Advice",
            "📄 Report"
        ])

        # ================= RESULTS =================
        with tab1:
            if prediction == 1:
                st.error("🔴 **Prediction: Diabetic**")
            else:
                st.success("🟢 **Prediction: Non-Diabetic**")

            st.metric("Diabetes Probability", f"{probability * 100:.2f}%")
            st.progress(probability)

        # ================= ANALYSIS =================
        with tab2:
            def status(val, normal):
                return "🟢 Normal" if val <= normal else "🔴 High"

            st.write(f"BMI: {bmi} → {status(bmi, 24.9)}")
            st.write(f"HbA1c: {hba1c}% → {status(hba1c, 5.7)}")
            st.write(f"Glucose: {glucose} → {status(glucose, 140)}")

            fig, ax = plt.subplots()
            ax.bar(["Non-Diabetic", "Diabetic"], [1 - probability, probability])
            ax.set_ylim(0, 1)
            st.pyplot(fig)

        # ================= HEALTH ADVICE (FIXED) =================
        with tab3:
            st.subheader("🧾 Personalized Health Advice")

            if probability < 0.30:
                st.success("🟢 LOW RISK")
                st.write("✔ Maintain a healthy lifestyle")
                st.write("✔ Continue regular exercise")
                st.write("✔ Eat a balanced diet rich in fruits and vegetables")
                st.write("✔ Regular health check-ups are recommended")

            elif probability < 0.60:
                st.warning("🟠 MODERATE RISK")
                st.write("⚠ Monitor your blood sugar levels regularly")
                st.write("⚠ Reduce sugar and processed food intake")
                st.write("⚠ Increase physical activity (at least 30 mins/day)")
                st.write("⚠ Maintain a healthy weight")

            else:
                st.error("🔴 HIGH RISK")
                st.write("🚨 Consult a doctor immediately")
                st.write("🚨 Follow a strict diabetic diet plan")
                st.write("🚨 Monitor glucose levels frequently")
                st.write("🚨 Avoid sugary foods and sedentary lifestyle")

        # ================= REPORT =================
        with tab4:
            patient_data = {
                "Patient Name": patient_name,
                "Gender": gender,
                "Age": age,
                "BMI": bmi,
                "HbA1c": hba1c,
                "Glucose": glucose
            }

            pdf_path = generate_pdf(patient_data, prediction, probability)

            with open(pdf_path, "rb") as f:
                st.download_button(
                    "📄 Download Report",
                    f,
                    file_name=f"{patient_name}_Report.pdf"
                )

    except Exception as e:
        st.error(f"Error: {e}")

# ==================================================
# Footer
# ==================================================
st.divider()
st.caption("Diabetes Prediction using Machine Learning")