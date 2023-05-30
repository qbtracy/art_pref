import streamlit as st

#st.markdown('**Quinn Tracy**')
st.markdown('**How do the predictions work?**')
st.markdown('A set of 3 binary classifier models (random forest) provide the predictions. Using the four features shown on the prediction page, each classifier predicts what a person with those characteristics would prefer between two mutually-exclusive categories.')

#st.markdown('**TESTING**')
st.image('./pages/capstone_bar_chart.png')
st.markdown('The bar chart above shows the accuracy of each of the classifiers when the four features are each entered as the only feature. The three classifiers, from left to right: Realistic vs. Surreal, Linear vs. Painterly, Masculine vs. Feminine.')

st.markdown('**How do the four features perform together?**')
st.markdown('The current models have the following accuracies:')
st.markdown('_Realistic vs. Surreal_: ~60%')
st.markdown('_Linear vs. Painterly_: ~60%')
st.markdown('_Masculine vs. Feminine_: ~62%')

st.markdown('**Miscellaneous:**')
st.image('./pages/capstone_scatter_plot.png')
st.markdown('The scatterplot above shows the art preferences (as continuous scores) among the five most common majors in the dataset. Negative scores indicate preference towards one end of the scale (Linear/Realistic/Masculine), while positive scores indicate preference towards the other (Painterly/Surreal/Feminine). A score of zero suggested no preference towards either end of the scale.')
st.markdown('There is no large, obvious separation in art preferences here, but there is considerable variability within each major. While major was one of the better predictors in the dataset, it should not be relied on in isolation.')
#st.markdown("This app was created as a capstone project for The Data Incubator's Data Science Bootcamp. If you want to reach out, see my contact information above!")