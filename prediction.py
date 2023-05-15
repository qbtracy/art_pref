import streamlit as st
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

#Load in our fitted models:
RAmodel = joblib.load("RAmodel.joblib")
LPmodel = joblib.load("LPmodel.joblib")
MFmodel = joblib.load("MFmodel.joblib")

#Now take the user's input and produce a prediction:
def app():
    
    st.title("Art Preference Prediction")
    
    st.markdown('Choose values from the fields below. This app will provide a prediction for what type of artwork a person with those characteristics would like.')
    
#    age = st.number_input('Age:',min_value=1,max_value=122)
    race = st.selectbox('Race:',options=['Asian','Arab','Black','Indigenous Australian','Native American','White','Other'])
    gender = st.selectbox('Gender:',options=['Male','Female','Other'])
    religion = st.selectbox('Religion:',options=['Agnostic','Atheist','Buddhist','Christian (Catholic)',
                                                     'Christian (Mormon)','Christian (Protestant)', 'Christian (Other)',
                                                    'Hindu','Jewish','Muslim','Sikh','Other'])

    major = st.selectbox('College Major:',options=['psychology','art','english','computer science','biology','business',
                                           'engineering','history','medical','economics','law','education','math',
                                           'physics','political science','nursing','architecture','philosophy',
                                           'communication','graphic design'])

    text_input = pd.DataFrame({'race':[race],'gender':[gender],'religion':[religion],'major':[major]})
    
    RAcat = RAmodel.predict(text_input)[0]
    LPcat = LPmodel.predict(text_input)[0]
    MFcat = MFmodel.predict(text_input)[0]
    
    if RAcat == 'Realistic':
        if LPcat == 'Linear':
            if MFcat == 'Masculine':
                example = 'ReLnMc.jpg'
            else:
                example = 'ReLnFe.jpg'
        else:
            if MFcat == 'Masculine':
                example = 'RePaMc.jpg'
            else:
                example = 'RePaFe.jpg'            
    else:
        if LPcat == 'Linear':
            if MFcat == 'Masculine':
                example = 'AbLnMc.jpg'
            else:
                example = 'AbLnFe.jpg'
        else:
            if MFcat == 'Masculine':
                example = 'AbPaMc.jpg'
            else:
                example = 'AbPaFe.jpg'  
    
    st.markdown('__We recommend artwork that is:__')
    st.write(RAcat)  
    st.write(LPcat)      
    st.write(MFcat)  

    st.markdown('__An example matching these categories:__')

    st.image(example)#, caption='Example of the above categories.')    
    
    st.markdown('\n\n\n\n\n\n\n')
    
    st.markdown('__What do these categories mean?__')

    st.markdown('**Realistic**: artwork which tries to render realistic scenes.')    
    st.markdown('**Abstract**: artwork which does not try to look realistic.')
    st.markdown('\n\n\n\n\n\n\n')
    st.markdown('**Linear**: artwork with clean lines, striving towards photorealism.')
    st.markdown('**Painterly**: artwork with visible brush strokes.')
    st.markdown('\n\n\n\n\n\n\n')    
    st.markdown('**Masculine**: artwork with content that is stereotypically of interest to males (such as fighting, machines, architecture, etc.).')
    st.markdown('**Feminine**: artwork with content that stereotypically appeals to females (such as women in dresses).')
    
#if __name__ == '__main__':
#    app()
