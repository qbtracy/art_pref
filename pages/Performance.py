import streamlit as st

#st.markdown('**Quinn Tracy**')
st.markdown('**How do the predictions work?**')
st.markdown('A set of 3 binary classifier models (random forest) provide the predictions. Using the four features shown on the prediction page, each classifier predicts what a person with those characteristics would prefer between two mutually-exclusive categories.')


st.markdown('**How do the predictions perform?**')
st.markdown('The current models have the following accuracies:')
st.markdown('_Realistic vs. Surreal_: ~60%')
st.markdown('_Linear vs. Painterly_: ~60%')
st.markdown('_Masculine vs. Feminine_: ~62%')

#st.markdown("This app was created as a capstone project for The Data Incubator's Data Science Bootcamp. If you want to reach out, see my contact information above!")