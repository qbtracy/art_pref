import streamlit as st
#import pandas as pd
#import joblib

#Load in our fitted models:
#RAmodel = joblib.load(RAmodel, "RAmodel.joblib")
#LPmodel = joblib.load(LPmodel, "LPmodel.joblib")
#MFmodel = joblib.load(MFmodel, "MFmodel.joblib")

#Now take the user's input and produce a prediction:
def app():
    
    st.title('Art Preference Prediction')
    
    st.markdown('Enter in values into the two fields below. This app will provide a prediction for what type of artwork a person with those characteristics would like.')
    
#    st.number_input('Age:',0,123)
#    st.text_input
    
if __name__ == '__main__':
    app()