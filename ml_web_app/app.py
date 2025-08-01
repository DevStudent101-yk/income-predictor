import streamlit as st

import requests

st.set_page_config(page_title="Income Prediction App", page_icon="🤖")

st.title("🧠 Income Prediction App")

st.write("Enter the details below and click Predict to see the model output.")

# Input fields
age = st.number_input("Age", 18, 100, 30)
workclass = st.text_input("Workclass", "Private")
fnlwgt = st.number_input("Fnlwgt", 10000, 500000, 200000)
education = st.text_input("Education", "Bachelors")
education_num = st.number_input("Education Number", 1, 20, 13)
marital_status = st.text_input("Marital Status", "Never-married")
occupation = st.text_input("Occupation", "Adm-clerical")
relationship = st.text_input("Relationship", "Not-in-family")
race = st.text_input("Race", "White")
sex = st.text_input("Sex", "Male")
capital_gain = st.number_input("Capital Gain", 0, 100000, 0)
capital_loss = st.number_input("Capital Loss", 0, 10000, 0)
hours_per_week = st.number_input("Hours per week", 1, 100, 40)
native_country = st.text_input("Native Country", "United-States")
income = st.text_input("Income", "<=50K")

if st.button("Predict"):
    url = env["API_URL"]   
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {env['API_TOKEN']}"
    }
    
    data = {
        "Inputs": {
            "WebServiceInput0": [
                {
                    "age": age,
                    "workclass": workclass,
                    "fnlwgt": fnlwgt,
                    "education": education,
                    "education-num": education_num,
                    "marital-status": marital_status,
                    "occupation": occupation,
                    "relationship": relationship,
                    "race": race,
                    "sex": sex,
                    "capital-gain": capital_gain,
                    "capital-loss": capital_loss,
                    "hours-per-week": hours_per_week,
                    "native-country": native_country,
                    "income": income
                }
            ]
        },
        "GlobalParameters": {}
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            scored_label = result['Results']['WebServiceOutput0'][0]['Scored Labels']
            scored_prob = result['Results']['WebServiceOutput0'][0]['Scored Probabilities']
            st.success(f"✅ Prediction: {scored_label}")
            st.info(f"📊 Probability: {scored_prob:.2f}")
        else:
            st.error(f"❌ Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Exception occurred: {e}")



