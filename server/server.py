from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/predict_risk', methods=['POST'])
def predict_risk():
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

    response = jsonify({
        'predict_risk': util.predict_risk(age, sex, weight, height, alcohol_consumption, smoking, genetic_risk, physical_activity, diabetes, hypertension)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("Starting Flask Server...")
    app.run()