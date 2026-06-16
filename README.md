# 🩺 Diabetes Risk Prediction ML

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://diabetes-risk-prediction-ml-ss3hafbqzoifhdyskqlqyz.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A production-ready **machine learning application** that predicts diabetes risk using Gradient Boosting with SMOTE. Leveraging medical data and clinical measurements, this tool provides accurate predictions along with personalized health insights and downloadable reports.

**[🚀 Try the Live App →](https://diabetes-risk-prediction-ml-ss3hafbqzoifhdyskqlqyz.streamlit.app/)**

---

## 📋 Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Input Features](#input-features)
- [Model Details](#model-details)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Data & Training](#data--training)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Contact](#contact)

---

## ✨ Features

- 🎯 **Accurate Predictions** - Gradient Boosting model trained with SMOTE for handling imbalanced data
- 📊 **Visual Analytics** - Interactive charts and health metric analysis
- 💡 **Personalized Recommendations** - Risk-based health advice tailored to your profile
- 📄 **PDF Reports** - Generate and download comprehensive medical reports
- 🌐 **Web Interface** - User-friendly Streamlit application with responsive design
- ⚡ **Real-time Processing** - Get instant predictions with confidence scores
- 🔐 **Data Privacy** - No data is stored; all predictions are processed locally

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.9+**
- **pip** package manager
- **Git** (for cloning the repository)

### Installation

```bash
# Clone the repository
git clone https://github.com/Nithin026/Diabetes-Risk-Prediction-ML.git
cd Diabetes-Risk-Prediction-ML

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
# Start the Streamlit app
streamlit run app.py
```

Open your browser and navigate to: `http://localhost:8501`

---

## 📂 Project Structure

```
Diabetes-Risk-Prediction-ML/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── runtime.txt                     # Python runtime version
├── README.md                       # This file
│
├── model/
│   ├── diabetes_model.pkl          # Pre-trained Gradient Boosting model
│   └── scaler.pkl                  # Feature scaling transformer
│
├── notebooks/
│   └── diabetes_analysis.ipynb     # Data exploration & model training
│
└── data/
    └── [Original training dataset]  # (See Data & Training section)
```

---

## 📝 How It Works

### 1. **Enter Your Information**
   - Personal details: Name, age, gender
   - Medical history: Hypertension, heart disease, smoking status
   - Clinical measurements: BMI, HbA1c level, blood glucose level

### 2. **Get Your Results**
   - Instant prediction: **Diabetic** or **Non-Diabetic**
   - Risk probability percentage (0-100%)
   - Visual analysis with confidence bars

### 3. **Review Analysis**
   - Health metrics breakdown (BMI, HbA1c, Glucose)
   - Visual comparison charts
   - Status indicators for each metric

### 4. **Get Personalized Advice**
   - **Low Risk (<30%)**: Lifestyle maintenance recommendations
   - **Moderate Risk (30-60%)**: Preventive measures and monitoring tips
   - **High Risk (>60%)**: Urgent medical consultation advice

### 5. **Download Report**
   - Generate professional PDF reports
   - Include all predictions and personal data
   - Suitable for sharing with healthcare providers

---

## 📊 Input Features

| Feature | Type | Range | Description |
|---------|------|-------|-------------|
| **Age** | Integer | 1-120 | Patient age in years |
| **Gender** | Categorical | Male/Female | Biological gender |
| **BMI** | Float | 10-60 | Body Mass Index (kg/m²) |
| **Hypertension** | Binary | Yes/No | History of high blood pressure |
| **Heart Disease** | Binary | Yes/No | Presence of heart disease |
| **Smoking History** | Categorical | No Info/Never/Former/Current | Smoking status |
| **HbA1c Level** | Float | 3-15 | Glycated hemoglobin (3-month glucose average) |
| **Blood Glucose Level** | Float | 50-400 | Fasting blood glucose (mg/dL) |

---

## 🧠 Model Details

### Algorithm
- **Type**: Gradient Boosting Classifier
- **Library**: Scikit-learn
- **Imbalance Handling**: SMOTE (Synthetic Minority Oversampling Technique)

### Training Approach
- **Cross-validation**: K-fold validation for robust evaluation
- **Feature Scaling**: StandardScaler for normalization
- **Data Encoding**: One-hot encoding for categorical variables
- **Class Balancing**: SMOTE to handle class imbalance in diabetes dataset

### Key Characteristics
- Handles non-linear relationships between features
- Robust to outliers through ensemble boosting
- Calibrated probability estimates for confidence scores

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.9+** | Core programming language |
| **Streamlit** | Web application framework & UI |
| **Scikit-learn** | Machine learning algorithms & model evaluation |
| **Imbalanced-learn** | SMOTE for handling class imbalance |
| **Pandas** | Data manipulation & analysis |
| **NumPy** | Numerical computations |
| **Matplotlib** | Data visualization |
| **ReportLab** | PDF report generation |
| **Joblib** | Model persistence |

---

## 📈 Model Performance

The model achieves strong performance metrics on the test dataset:

```
Accuracy:    ~95%
Precision:   ~92%
Recall:      ~89%
F1-Score:    ~90%
AUC-ROC:     ~96%
```

*Note: Metrics are based on internal validation. For production use, consult healthcare professionals.*

---

## 📚 Data & Training

### Dataset Source
- **Original Data**: Publicly available diabetes prediction dataset
- **Records**: 100,000+ patient records
- **Features**: 8 clinical and demographic variables
- **Class Distribution**: Imbalanced (majority non-diabetic)

### Data Preprocessing
1. **Missing Values**: Handled appropriately
2. **Outliers**: Detected and treated
3. **Scaling**: StandardScaler normalization
4. **Encoding**: Categorical variables converted to numeric
5. **Balancing**: SMOTE applied to training data

### Training Details
- **Train-Test Split**: 80-20
- **Validation**: 5-fold cross-validation
- **Hyperparameters**: Tuned for optimal performance
- **See**: `notebooks/diabetes_analysis.ipynb` for full training pipeline

---

## 🔍 Using the Application

### Step-by-Step Guide

1. **Launch the App**
   ```bash
   streamlit run app.py
   ```

2. **Fill in Your Information**
   - Complete all required fields
   - Use accurate measurements for best results

3. **Click "Predict Diabetes"**
   - Processing happens instantly
   - Results displayed in real-time

4. **Review Tabs**
   - **Results**: Prediction & probability
   - **Analysis**: Health metrics breakdown
   - **Health Advice**: Personalized recommendations
   - **Report**: Generate PDF for records

5. **Download Report** (Optional)
   - PDF includes all your data and prediction
   - Share with healthcare provider

---

## ⚠️ Important Disclaimer

**This application is for educational and informational purposes only.**

- ❌ **NOT** a substitute for professional medical advice
- ❌ **NOT** a diagnostic tool
- ❌ Should **NOT** be used for treatment decisions
- ⚠️ Always consult with qualified healthcare professionals for medical decisions
- 📋 This tool is meant to raise awareness, not provide medical diagnosis

**Use at your own risk. The developers and creators assume no liability.**

---

## 🤝 Contributing

We welcome contributions! If you'd like to improve this project:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Ideas
- 🐛 Bug fixes and improvements
- 📊 Better model architectures
- 🎨 UI/UX enhancements
- 📚 Documentation improvements
- 🧪 Additional test cases
- 📈 Model performance optimization

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 📧 Contact & Support

- **GitHub Issues**: [Open an issue](https://github.com/Nithin026/Diabetes-Risk-Prediction-ML/issues)
- **Questions**: Feel free to reach out through GitHub discussions
- **Bug Reports**: Please provide detailed reproduction steps

---

## 📚 Resources & References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Gradient Boosting Explained](https://en.wikipedia.org/wiki/Gradient_boosting)
- [SMOTE Technique](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html)
- [Diabetes Information](https://www.cdc.gov/diabetes/)

---

## 🙏 Acknowledgments

- Dataset providers and open-source community
- Scikit-learn and Streamlit teams
- All contributors and users

---

**Made with ❤️ for healthcare awareness and education.**

Last Updated: 2026 | Version: 1.0
