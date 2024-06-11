# Description: This file contains the utility functions that are used to load the saved artifacts and make predictions.
import json 
import pickle
import numpy as np

__data_columns = None
__model = None

def predict_risk(age, sex, weight, height, alcohol_consumption, smoking, genetic_risk, physical_activity, diabetes, hypertension):
    data= np.zeros( len(__data_columns) )
    bmi = weight / (height**2)
    # Assign the values to the data array
    data[0] = age
    data[1] = sex
    data[2] = bmi
    data[3] = alcohol_consumption
    data[4] = smoking
    data[5] = genetic_risk
    data[6] = physical_activity
    data[7] = diabetes
    data[8] = hypertension

    # Make a prediction
    probabilities = __model.predict_proba([data])

    # The returned probabilities are in the range [0, 1]. 
    # In the case of binary classification, `probabilities[0, 1]` will give you the probability of the positive class.
    risk_percentage = probabilities[0, 1] * 100
    risk_percentage_string = f"{risk_percentage:.2f}%"
        
    return risk_percentage_string

def load_saved_artifiacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __model

    with open('server/artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

    with open('server/artifacts/log_model.pkl', 'rb') as f:
        __model = pickle.load(f)

    print("Loading saved artifacts...done")


if __name__ == '__main__':
    load_saved_artifiacts()