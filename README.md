# 🎓 Student Placement Prediction Using Machine Learning

## 📌 Project Overview

This project predicts whether a student is likely to get placed based on academic performance, internships, projects, aptitude scores, soft skills, and other factors.

The project uses Machine Learning techniques to analyze student data and predict placement status as Placed or Not Placed.

---

## 🎯 Problem Statement

Students often want to know their placement chances based on their academic and skill profiles.

This project aims to build a Machine Learning model that can predict a student's placement status using historical student data.

---

## 📊 Dataset Features

The dataset contains the following features:

- CGPA
- Internships
- Projects
- Workshops/Certifications
- Aptitude Test Score
- Soft Skills Rating
- Extracurricular Activities
- Placement Training
- SSC Marks
- HSC Marks

### Target Variable

- Placement Status
  - Placed
  - Not Placed

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Streamlit

---

## 🤖 Machine Learning Algorithm

### Logistic Regression

The Logistic Regression algorithm was used to classify students into:

- Placed
- Not Placed

---

## 🔄 Project Workflow

1. Data Collection
2. Data Preprocessing
3. Data Cleaning
4. Feature Selection
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Placement Prediction
9. Streamlit Web Application

---

## 📈 Model Performance

### Logistic Regression Accuracy

**79.45%**

---

## 💻 Streamlit Application

The trained model is integrated with Streamlit to provide an interactive user interface where users can enter student details and get placement predictions instantly.

---

## 📂 Project Structure

```text
Student-Placement-Prediction/

│
├── app.py
├── placement_model.pkl
├── placement_data.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Sample Prediction

Input:

- CGPA = 8.5
- Internships = 2
- Projects = 3
- Aptitude Score = 88
- Soft Skills = 4.7

Output:

```text
Placed
```

---

## 🚀 Future Improvements

- Random Forest Implementation
- Feature Importance Analysis
- Deployment on Streamlit Cloud
- More Advanced Machine Learning Models
- Improved User Interface

---

## 👨‍💻 Author

Mithra
B.Tech AIML Student

Machine Learning Beginner Project
