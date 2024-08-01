import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("/content/model_poly.pkl", "rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_bankruptcy(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk):
    prediction = classifier.predict([[industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk]])
    print(prediction)
    return prediction

def main():
    #st.title("Bankruptcy Detector")
    html_temp = """
    <div style="background-color:#cdb4db;padding:10px">
    <h2 style="color:white;text-align:center;">Bankruptcy Detector</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    industrial_risk = st.text_input("Industrial Risk", value="")
    management_risk = st.text_input("Management Risk", value="")
    financial_flexibility = st.text_input("Financial Flexibility", value="")
    credibility = st.text_input("Credibility", value="")
    competitiveness = st.text_input("Competitiveness", value="")
    operating_risk = st.text_input("Operating Risk", value="")
    result = ""
    if st.button("Predict"):
        industrial_risk = float(industrial_risk)
        management_risk = float(management_risk)
        financial_flexibility = float(financial_flexibility)
        credibility = float(credibility)
        competitiveness = float(competitiveness)
        operating_risk = float(operating_risk)
        
        prediction = predict_bankruptcy(
            industrial_risk, management_risk, financial_flexibility,
            credibility, competitiveness, operating_risk
        )
        if prediction == 0:
            result = "The company is bankrupted"
        else:
            result = "The company is not bankrupted"

    st.success('Prediction: {}'.format(result))
    #if st.button("About"):
      #  st.text("Let's Learn")
       # st.text("Built with Streamlit")

if __name__ == '__main__':
    main()
