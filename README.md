# 🩺 Diabetes Risk Prediction Using Machine Learning

A comprehensive machine learning application that predicts diabetes risk using patient medical data. Built with Streamlit for an interactive user interface and powered by advanced machine learning algorithms.

**Live Demo:** [Streamlit App](https://diabetes-risk-prediction-ml-ss3hafbqzoifhdyskqlqyz.streamlit.app/)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Dataset](#dataset)
- [Results & Performance](#results--performance)
- [How to Use the App](#how-to-use-the-app)
- [Health Advice Categories](#health-advice-categories)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project implements a machine learning-based healthcare application for early diabetes prediction. The application uses advanced algorithms including **Gradient Boosting** and **SMOTE** (Synthetic Minority Over-sampling Technique) to handle class imbalance and improve prediction accuracy.

The system takes patient medical parameters as input and provides:
- ✅ Diabetes risk prediction (Diabetic/Non-Diabetic)
- ✅ Probability score of having diabetes
- ✅ Personalized health recommendations
- ✅ PDF report generation for patient records
- ✅ Visual analysis and statistics

---

## ✨ Features

### Core Prediction Features
- **Risk Classification**: Predicts whether a patient is at risk of diabetes
- **Probability Scoring**: Provides a probability percentage (0-100%) for diabetes risk
- **Real-time Prediction**: Instant predictions based on patient input

### User Interface
- **Interactive Streamlit Dashboard**: User-friendly interface with multiple sections
- **Tabbed Results View**: Organized results with four tabs:
  - 📊 Results: Prediction outcome and risk probability
  - 📈 Analysis: Health metrics analysis and visualization
  - 🧾 Health Advice: Personalized recommendations based on risk level
  - 📄 Report: PDF report generation and download

### Additional Features
- **Patient Information Collection**: Name, gender, age, and medical history
- **Clinical Measurements**: BMI, HbA1c level, blood glucose level
- **Health Status Indicators**: Visual indicators (🟢 Normal, 🔴 High)
- **PDF Report Generation**: Download detailed prediction reports
- **Visualization**: Bar charts showing prediction probability distribution

---

## 💻 Technologies

### Languages & Frameworks
- **Python 3.x**: Core programming language
- **Streamlit**: Web application framework for interactive UI
- **Scikit-learn**: Machine learning algorithms and model evaluation
- **Pandas**: Data manipulation and preprocessing
- **NumPy**: Numerical computations
- **Imbalanced-learn**: SMOTE for handling class imbalance

### Additional Libraries
- **Joblib**: Model and scaler serialization
- **Matplotlib**: Data visualization
- **ReportLab**: PDF report generation

### Deployment
- **Streamlit Cloud**: Live application hosting

---

## 📁 Project Structure
