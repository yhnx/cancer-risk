from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__, template_folder='client')

@app.route('/predict_risk', methods=['POST'])
def predict_risk():
    try:
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        alcohol_consumption = float(request.form['alcohol_consumption'])
        smoking = int(request.form['smoking'])
        genetic_risk = int(request.form['genetic_risk'])
        physical_activity = float(request.form['physical_activity'])
        diabetes = int(request.form['diabetes'])
        hypertension = int(request.form['hypertension'])
    except:
        return util.apology("Invalid input values", 400)

    risk_percentage = util.predict_risk(age, sex, weight, height, alcohol_consumption, smoking, genetic_risk, physical_activity, diabetes, hypertension)
    

    return render_template('risk.html', risk_percentage=risk_percentage)

@app.route('/', methods=['POST', "GET"])
def home():
    return render_template('app.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return util.apology("Page not found", 404)
