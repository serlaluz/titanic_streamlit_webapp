# titanic_streamlit_webapp
This is an app to predict whether or not someone could or not survive on the Titanic. 

## Machine Model Used

In order to do this I first used a notebook via Google Colab to import the data, clean the data, split the data, fit the data, train and test the data, evaluate performance and deploy and save as a pikl file. I used the `Scikitlearn RandomForestClassifier`to train and test. Then, with the Streamlit package, I've made a simple UI and then deployed it unto Heroku. 

Project URL - https://titanic-streamlit-webapp.herokuapp.com/

## UI tool
* Streamlit, https://www.streamlit.io/

## Deployed
* Heroku, https://www.heroku.com

## Required Files
1. setup.sh
2. Procfile
3. requirements.txt

## Future Fixes
1. Set default value for Siblings, Parents as 0. 
2. Remove the numbers that are visible after clicking on `Predict Survivability`

### References
1. JCharis Tech's video on How to deploy Streamlit to Heroku, https://www.youtube.com/watch?v=skpiLtEN3yk&list=PLJ39kWiJXSixyRMcn3lrbv8xI8ZZoYNZU&index=3
