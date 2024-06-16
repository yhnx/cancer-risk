# Description: This file contains the utility functions that are used to load the saved artifacts and make predictions.
import json 
import pickle
from flask import render_template

__data_columns = None
__model = None

def predict_risk(age, sex, weight, height, alcohol_consumption, smoking, genetic_risk, physical_activity, diabetes, hypertension):
    load_saved_artifiacts()
    
    # Calculate BMI
    bmi = weight / (height**2)
    # Assign the values to the data list
    data = [age, sex, bmi, alcohol_consumption, smoking, genetic_risk, physical_activity, diabetes, hypertension]

    # Define the feature names used during model training
    feature_names = ['Age', 'Sex', 'BMI', 'AlcoholConsumption', 'Smoking', 'GeneticRisk', 'PhysicalActivity', 'Diabetes', 'Hypertension']

    # Convert data to a dictionary
    data_dict = dict(zip(feature_names, data))

    # Make a prediction
    probabilities = __model.predict_proba([list(data_dict.values())])


    # The returned probabilities are in the range [0, 1]. 
    # In the case of binary classification, `probabilities[0, 1]` will give you the probability of the positive class.
    risk_percentage = probabilities[0, 1] * 100
    risk_percentage_string = f"{risk_percentage:.2f}%"
        
    return risk_percentage_string

def load_saved_artifiacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __model

    with open('artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

    with open('artifacts/log_model.pkl', 'rb') as f:
        __model = pickle.load(f)

    print("Loading saved artifacts...done")

def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code

