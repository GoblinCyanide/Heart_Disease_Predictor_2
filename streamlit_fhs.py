import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
     page_title="Heart Disease Predictor",
     page_icon=":heart:",
     layout="wide",
     initial_sidebar_state="expanded",
)

st.write("# 10 Year Heart Disease Predictor")

col1, col2, col3 = st.columns(3)

# getting input by user

gender = col1.radio("Select your gender",("Male", "Female"))

age = col2.number_input("Enter your age", min_value = 0, max_value = 150, value = 0, step = 1)

education = col3.selectbox("Highest academic qualification",["High school diploma", "Undergraduate degree", "Postgraduate degree", "PhD"])

isSmoker = col1.radio("Are you currently a smoker?",("Yes","No"))

yearsSmoking = col2.number_input("Number of daily cigarettes", min_value = 0, max_value = 150, value = 0, step = 1)

BPMeds = col3.radio("Are you currently on BP medication?",("Yes","No"))

stroke = col1.radio("Have you ever experienced a stroke?",("Yes","No"))

hyp = col2.radio("Do you have hypertension?",("Yes","No"))

diabetes = col3.radio("Do you have diabetes?",("Yes","No"))

chol = col1.number_input("Enter your cholesterol level (mg/dL)", min_value = 0, max_value = 1000, value = 0, step = 1)

sys_bp = col2.number_input("Enter your systolic blood pressure (mm Hg)", step = 0.5)

dia_bp = col3.number_input("Enter your diastolic blood pressure (mm Hg)", step = 0.5)

bmi = col1.number_input("Enter your Body mass index (BMI)")

heart_rate = col2.number_input("Enter your resting heart rate (bpm)", min_value = 0, max_value = 200, value = 0, step = 1)

glucose = col3.number_input("Enter your glucose level (mg/dL)", min_value = 0, max_value = 500, value = 0, step = 1)


# Tranforming the user input data

df_pred = pd.DataFrame([[gender,age,education,isSmoker,yearsSmoking,BPMeds,stroke,hyp,diabetes,chol,sys_bp,dia_bp,bmi,heart_rate,glucose]],

columns= ['gender','age','education','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','prevalentHyp','diabetes','totChol','sysBP','diaBP','BMI','heartRate','glucose'])

df_pred['gender'] = df_pred['gender'].apply(lambda x: 1 if x == 'Male' else 0)

df_pred['prevalentHyp'] = df_pred['prevalentHyp'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['prevalentStroke'] = df_pred['prevalentStroke'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['diabetes'] = df_pred['diabetes'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['BPMeds'] = df_pred['BPMeds'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['currentSmoker'] = df_pred['currentSmoker'].apply(lambda x: 1 if x == 'Yes' else 0)
def transform(data):
    result = 3
    if(data=='High school diploma'):
        result = 0
    elif(data=='Undergraduate degree'):
        result = 1
    elif(data=='Postgraduate degree'):
        result = 2
    return(result)
df_pred['education'] = df_pred['education'].apply(transform)


# Loading the ML model and predicting using it


model = joblib.load('fhs_rf_model2.pkl')
prediction = model.predict(df_pred)

# Displaying the prediction on button click

if st.button('Predict'):

    if(prediction[0]==0):
        st.write('<p class="big-font">You are <b>NOT</b> likely to develop heart disease in 10 years.</p>',unsafe_allow_html=True)

    else:
        st.write('<p class="big-font">You are likely to develop heart disease in 10 years.</p>',unsafe_allow_html=True)
