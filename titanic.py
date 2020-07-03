import streamlit as st
import joblib
import numpy as np
from PIL import Image

#this is our machine learning model
titanic = open("titanic_random_forest.pkl", "rb")
titanic_model = joblib.load(titanic)

#this is the predict function
@st.cache
def predict_survive(data):
  predictions = np.array([data])
  final_result = titanic_model.predict(predictions)
  return final_result

#this is the main app function
def main():
  """Titanic Classifier App with Streamlit"""
  st.title("Can you Survive on the Titanic?")
  img = Image.open("titanic.jpg")
  st.image(img, width=700, caption="Tragedy on the Titanic")
  st.markdown("```#In order to begin please click on the arrow in the top left corner```")
  st.subheader("Scikitlearn's RandomForestClassifier")
  st.text("You have selected")
  

  models = ['RandomForestClassifier']
  choice = st.sidebar.selectbox("Choose a Machine Learning Model", models)

  if choice == 'RandomForestClassifier':
    st.info("Predict Survivabiity with RandomForestClassifier")
  
#The following allows inputs to be inserted in order to make our predictions
  Age = st.slider("How old are you", 1, 100)

  SibSp = st.slider("How many Siblings or Spouse are onboard?", 1, 10)

  Parch = st.slider("How many Parents or Children are onboard?", 1, 10)

  Fare = st.number_input("Enter Fare value 1-512 with Decimals (ex 100.00) ")

  Gender = 0
  Gender_input = st.radio("Your Gender", ('Male', 'Female'))
  if Gender_input == "Male" :
    Gender += 1 
  else:
    Gender += 0

  PClass1 = 0
  PClass2 = 0
  PClass_input = st.selectbox("Your Cabin Class", ["First", "Second", "Third"])
  if PClass_input == "Second":
    PClass1 += 1
    PClass2 += 0
  elif PClass_input == "Third":
    PClass1 += 0
    PClass2 += 1
  else:
    PClass1 = 0
    PClass2 = 0


  Place1 = 0
  Place2 = 0
  Place_input = st.selectbox("Place of Embarkment", ["Queenstown", "Southampton", "Other"])
  if Place_input.casefold() == "queenstown":
    Place1 += 1
    Place2 += 0
  elif Place_input.casefold() == "southampton":
    Place1 += 0
    Place2 += 1
  else:
    Place1 += 0
    Place2 += 0

  p = []
  p += [Age, SibSp, Parch, Fare, Gender, PClass1, PClass2, Place1, Place2]

#This calls the predict function
  if st.button("Predict Survivability"):
    result = predict_survive(p)
    st.text(p)
    st.text([result])
    if result == [1]:
      prediction = "Survived"
      return st.success(f"You have {prediction}")
    else:
      prediction = "Deceased"
      return st.error(f"You have {prediction}")
  



if __name__ == '__main__':
  main()