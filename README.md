# Obesity Category Prediction App

This is a **Machine Learning**-powered web application built using **Streamlit** that predicts a person's **Obesity Category** based on key physical attributes and lifestyle metrics.

> **Categories Predicted:**
> - 0: Normal weight
> - 1: Obese
> - 2: Overweight
> - 3: Underweight

---

## Live App Deployment

 **Try the app here**: [Obesity Prediction App](https://obesity-prediction-app-b3rssec5aax3cnlrhaia9r.streamlit.app/)

Deployed using **Streamlit Cloud**, with **CI/CD** enabled via Git integration — every time you push to the `main` branch, the app redeploys automatically ✅

---

##  Features

-  User inputs: Age, Gender, Height, Weight, BMI, Physical Activity Level
-  Trained ML Model: Random Forest Classifier (with GridSearchCV tuning)
-  Feature importance & data visualization using Seaborn & Matplotlib
-  High accuracy with optimized metrics (precision, recall, F1-score)
-  Deployed via Streamlit Cloud with automated CI/CD

---

##  Tech Stack

| Tool              | Purpose                                 |
|-------------------|-----------------------------------------|
| **Python**        | Programming language                    |
| **Pandas**        | Data manipulation                       |
| **Scikit-learn**  | Machine learning modeling               |
| **Matplotlib / Seaborn** | Data visualization              |
| **Streamlit**     | Web app development and deployment      |
| **GitHub**        | Version control                         |
| **CI/CD**         | Triggered via Streamlit GitHub sync     |

---

##  Project Structure

─ obesity.py # Streamlit app

─ final_obesity_model.pkl # Trained ML model

─ requirements.txt # Project dependencies

─ README.md # Project documentation

 How to Run Locally

1. Clone the repo:
   git clone https://github.com/SuyashBurile/obesity-prediction-app.git
   cd obesity-prediction-app
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app:
   streamlit run app.py

