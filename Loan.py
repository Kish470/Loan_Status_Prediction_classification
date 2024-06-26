import pandas as pd
import streamlit as st
import pickle as pk

model = pk.load(open('Loan_Prediction_Model.Pickle','rb'))

st.header("Loan Prediction Status")

st.slider('Choose No of Dependents', 0,5)
st.selectbox('Choose Education',['Graduate', 'Not Graduate'])
Pred_data = pd.DataFrame([[2,1,0,12,778,16.077274,17.213369,17.635418]], columns=['no_of_dependents','education','self_employed','loan_term','cibil_score','income_annum_log','loan_amount_log','Assets_log'])