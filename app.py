import streamlit as st
import pandas as pd
import numpy as np
import joblib
BestModel=joblib.load("./pklFiles/BestModel.pkl")
st.header("Apple Qulaity Prediction 🍎")

s1=st.number_input("Size Of Apple",0.0)
s2=st.number_input("Weight Of Apple",0.0)
s3=st.number_input("Sweet Of Apple",0.0)
s4=st.number_input("Crunchiness",0.0)
s5=st.number_input("Juiciness",0.0)
s6=st.number_input("Ripeness",0.0)
s7=st.number_input("Acidity")


btn=st.button("Predict Quality")
st.divider()
if btn:
    df={
        "Size":[s1],
        "Weight":[s2],
        "Sweetness":[s3],
        "Crunchiness":[s4],
        "Juiciness":[s5],
        "Ripeness":[s6],
        "Acidity":[s7],
    }
    df=pd.DataFrame(df)
    
    ans = BestModel.predict(df)[0]
    if ans==1:
        st.subheader("The Quality Of Your Apple Is :green[Good]")
    else:
        st.subheader("The Quality Of Your Apple Is :red[Bad]")
    




    
    




