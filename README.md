# 🩺 Diabetes Risk Prediction

A machine learning app that predicts your diabetes risk based on medical data. Get instant predictions, health insights, and downloadable reports.

**[Try the Live App →](https://diabetes-risk-prediction-ml-ss3hafbqzoifhdyskqlqyz.streamlit.app/)**

---

## ✨ What This Does

- 🎯 **Predicts diabetes risk** - Get a yes/no prediction with confidence score
- 📊 **Analyzes your health** - Visual breakdown of your health metrics  
- 💡 **Gives health advice** - Personalized recommendations based on your risk level
- 📄 **Generates reports** - Download PDF reports for your records

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/Nithin026/Diabetes-Risk-Prediction-ML.git
cd Diabetes-Risk-Prediction-ML

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

---

## 📝 How to Use

1. **Enter Your Information**
   - Name, age, and gender
   - Medical measurements (weight, height, blood sugar levels)

2. **Get Your Results**
   - Instant prediction (Diabetic/Non-Diabetic)
   - Risk probability percentage
   - Visual analysis charts

3. **Get Recommendations**
   - Personalized health advice
   - Lifestyle suggestions

4. **Download Report**
   - Save PDF report for doctor visits

---

## 🧠 The Model

**Algorithm**: Gradient Boosting with SMOTE (handles imbalanced data)

**Trained on**: Medical patient data with multiple health indicators

**Accuracy**: High-performance predictions on test data

---

## 📂 Project Files

```
├── app.py                 # Main Streamlit application
├── model.pkl             # Pre-trained ML model
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

---

## 🛠️ Technologies Used

- **Python** - Programming language
- **Streamlit** - Web framework for UI
- **Scikit-learn** - Machine learning
- **Pandas** - Data processing
- **ReportLab** - PDF generation

---

## 📊 Input Features

| Feature | Description | Example |
|---------|-------------|---------|
| Age | Patient age in years | 45 |
| Gender | Male/Female | Male |
| BMI | Body Mass Index | 28.5 |
| HbA1c | Blood sugar average (3 months) | 5.8 |
| Blood Glucose | Current blood sugar level | 120 |

---

## ⚠️ Disclaimer

This tool is for **educational and informational purposes only**. It is **not a substitute for professional medical advice**. Always consult with a healthcare provider for medical decisions.

---

## 📜 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

---

## 📧 Questions?

Feel free to open an issue on GitHub or reach out!

