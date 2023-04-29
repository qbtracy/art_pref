import pandas as pd
#from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.compose import ColumnTransformer
#from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
#from sklearn.preprocessing import StandardScaler
import joblib

#Load in our cleaned data:
df = pd.read_csv('art_pref_cleaned.csv')

#For the current time, let's drop the 'major's with low N (<10)
df = df.groupby('major').filter(lambda x: len(x) >= 10)

#So what predictors might be contenders? For now, let's try age, family size, and most of the small_demo variables (+ major)
demo_final = ['age','familysize','education','urban','gender','engnat','hand','religion',
              'orientation','race','voted','married']#,'major']
demo_final_cat = ['education','urban','gender','engnat','hand','religion',
              'orientation','race','voted','married']#,'major']

allcol_final = ['age','familysize','education','urban','gender','engnat','hand','religion',
              'orientation','race','voted','married','MF_Cat']#'LP_Cat']#'RA_Cat']#'major','LP_Cat','MF_Cat']

#For the web app, let's start with 'major' and 'age', and consider other predictors later. These two form models with mid-50s to low-60s accuracy for our models
df_finalRA = df.dropna(subset=['major','age','RA_Cat'])
df_finalLP = df.dropna(subset=['major','age','LP_Cat'])
df_finalMF = df.dropna(subset=['major','age','MF_Cat'])

model_cats = ['major']

#Build a model for each
def rf_model_fit (features, label):

    ohe_cat = ColumnTransformer([ 
      ('one_hot', OneHotEncoder(), model_cats) #Note that this relies on a global variable, unless I probably separate out the function arguments by categorical and continuous features
        ], 
        remainder='passthrough')

    #Set up a pipeline that does the one hot encoding and then performs the random forest classification
    rf_pipe = Pipeline([('ohe', ohe_cat),
                    ('rf', RandomForestClassifier(n_estimators=50))])

    #Do a grid search to find optimal depth for the random forest model
    rf_gs = GridSearchCV(rf_pipe, 
                     cv=5, 
                     param_grid={'rf__max_depth': range(3, 10)}
                    )

    rf_est = rf_gs.fit(features, label)
                       
    return rf_est #With the model fit, we are ready to accept input to produce a prediction

#Create and save our fit models
RAmodel = rf_model_fit(df_finalRA[['major','age']],df_finalRA['RA_Cat'])
LPmodel = rf_model_fit(df_finalLP[['major','age']],df_finalLP['LP_Cat'])
MFmodel = rf_model_fit(df_finalMF[['major','age']],df_finalMF['MF_Cat'])

#And export our model fits for use elsewhere:
joblib.dump(RAmodel, "RAmodel.joblib")
joblib.dump(LPmodel, "LPmodel.joblib")
joblib.dump(MFmodel, "MFmodel.joblib")