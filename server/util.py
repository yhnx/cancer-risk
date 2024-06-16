# Description: This file contains the utility functions that are used to load the saved artifacts and make predictions.
import pickle
import numpy as np
from flask import render_template
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import onnxruntime as rt

__data_columns = None
__model = None

def predict_risk(age, sex, weight, height, alcohol_consumption, smoking, genetic_risk, physical_activity, diabetes, hypertension):
    load_saved_artifacts()
    
    # Calculate BMI
    bmi = weight / (height**2)
    # Assign the values to the data list
    data = [age, sex, bmi, alcohol_consumption, smoking, genetic_risk, physical_activity, diabetes, hypertension]

    # Prepare the input data
    sess = rt.InferenceSession(__model.SerializeToString())
    input_name = sess.get_inputs()[0].name
    data = np.array([data], dtype=np.float32)

    # Make a prediction
    probabilities = sess.run(None, {input_name: data})

    # The returned probabilities are in the range [0, 1]. 
    # In the case of binary classification, `probabilities[0, 1]` will give you the probability of the positive class.
    print(probabilities)
    risk_percentage = probabilities[1][0][1] * 100
    risk_percentage_string = f"{risk_percentage:.2f}%"
        
    return risk_percentage_string

def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __model

    with open('artifacts/log_model.pkl', 'rb') as f:
        __skimodel = pickle.load(f)
    initial_type = [('float_input', FloatTensorType([None, 9]))]  # assuming your input is a 1D array with 9 features
    __model = convert_sklearn(__skimodel, initial_types=initial_type)

    with open('artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

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

