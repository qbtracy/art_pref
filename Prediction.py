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
    
    st.markdown('Choose values from the fields below. This app will provide a prediction for what type of artwork a person with those characteristics would like, as well as some paintings that exemplify those recommendations.')
    
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
    
    
    #Set up what we show the user after generating their prediction:
    if RAcat == 'Realistic':
        RAtext = '**Realistic**: artwork which tries to render realistic scenes.'
    else:
        RAtext = '**Surreal**: artwork which portrays bizarre scenes.'
        
    if LPcat == 'Linear':
        LPtext = '**Linear**: artwork with clean lines, striving towards photorealism.'
    else:
        LPtext = '**Painterly**: artwork with visible brush strokes.'
        
    if MFcat == 'Masculine':
        MFtext = '**Masculine**: artwork with content that is stereotypically of interest to males (such as fighting, machines, architecture, etc.).'
    else:
        MFtext = '**Feminine**: artwork with content that stereotypically appeals to females (such as women in dresses).'
        
    #Set up which example paintings to show. Unless otherwise noted, they are taken from the survey's dataset,
    #which in turn provides sources for the images (mostly Wikipedia I think):
    if RAcat == 'Realistic':
        if LPcat == 'Linear':
            if MFcat == 'Masculine':
                example = 'ReLnMc.jpg'
                #Source: CNN war art
                example2 = 'ReLnMc2.jpg'
                #Source: https://www.nga.gov/
                example3 = 'ReLnMc3.jpg'
            else:
                example = 'ReLnFe.jpg'
                example2 = 'ReLnFe2.jpg'
                example3 = 'ReLnFe3.jpg'
        else:
            if MFcat == 'Masculine':
                example = 'RePaMc.jpg'                
                #Source: civil-war-picket.blogspot.com
                example2 = 'RePaMc2.jpg'
                #Source: http://www.nobullart.com/
                example3 = 'RePaMc3.jpg'
            else:
                example = 'RePaFe.jpg'   
                #Source: https://mymodernmet.com/famous-female-painters-art-history/
                example2 = 'RePaFe2.jpg' 
                #Source: https://www.1stdibs.com/
                example3 = 'RePaFe3.jpg'
    else:
        if LPcat == 'Linear':
            if MFcat == 'Masculine':
                example = 'AbLnMc.jpg'
                #Source: https://juliennedickey.wordpress.com/
                example2 = 'AbLnMc2.jpg'
                #Source: https://www.designstack.co/
                example3 = 'AbLnMc3.jpg'
            else:
                example = 'AbLnFe.jpg'
                #Source: http://www.redbubble.com/people/frankmoth
                example2 = 'AbLnFe2.jpg'
                #Source: https://www.redbubble.com/i/poster/Discohead-Disco-ball-by-MsGonzalez/
                example3 = 'AbLnFe3.jpg'
        else:
            if MFcat == 'Masculine':
                example = 'AbPaMc.jpg'
                #Source: https://fineartamerica.com/
                example2 = 'AbPaMc2.jpg'
                #Source: https://www.artnews.com/
                example3 = 'AbPaMc3.jpg'
            else:
                example = 'AbPaFe.jpg'
                #Source for both 2 and 3: https://beautifulbizarre.net/2022/02/25/christina-ridgeway-interview/
                example2 = 'AbPaFe2.jpg'
                example3 = 'AbPaFe3.jpg'
    
#    st.markdown('__We recommend artwork that is:__')
#    st.write(RAtext)  
#    st.write(LPtext)      
#    st.write(MFtext)  

#    st.markdown('__An example matching these categories:__')

#    st.image(example)#, caption='Example of the above categories.')    
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('__We recommend artwork that is:__')
        st.write(RAtext)  
        st.write(LPtext)      
        st.write(MFtext)    
    with col2:
        st.image(example)
        
    col3, col4 = st.columns(2)
    
    with col3:
#        3cont = st.container()
        st.image(example2)
#        st.image(example3)
    with col4:
        st.image(example3)
#    st.sidebar.image(example)
    
#    st.markdown('\n\n\n\n\n\n\n')
    
#    st.markdown('__What do these categories mean?__')

#    st.markdown('**Realistic**: artwork which tries to render realistic scenes.')    
#    st.markdown('**Abstract**: artwork which does not try to look realistic.')
#    st.markdown('\n\n\n\n\n\n\n')
#    st.markdown('**Linear**: artwork with clean lines, striving towards photorealism.')
#    st.markdown('**Painterly**: artwork with visible brush strokes.')
#    st.markdown('\n\n\n\n\n\n\n')    
#    st.markdown('**Masculine**: artwork with content that is stereotypically of interest to males (such as fighting, machines, architecture, etc.).')
#    st.markdown('**Feminine**: artwork with content that stereotypically appeals to females (such as women in dresses).')
    
if __name__ == '__main__':
    app()