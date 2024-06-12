function updateAgeInput() {
  const ageSlider = document.getElementById("ageSlider");
  const ageInput = document.getElementById("ageInput");
  ageInput.value = ageSlider.value;
}

function updateAgeSlider() {
  const ageSlider = document.getElementById("ageSlider");
  const ageInput = document.getElementById("ageInput");
  ageSlider.value = ageInput.value;
}

function onClickedPredictRisk() {
  console.log("Predict Risk button clicked");

  var age = parseFloat(document.getElementById("ageInput").value);
  var sex = parseInt(document.getElementById("sex").value);
  var height = parseFloat(document.getElementById("height").value);
  var weight = parseFloat(document.getElementById("weight").value);
  var alcohol = parseFloat(document.getElementById("alcohol").value);
  var smoking = parseInt(document.getElementById("smoking").value);
  var geneticRisk = parseInt(document.getElementById("geneticRisk").value);
  var physicalActivity = parseFloat(
    document.getElementById("physicalActivity").value
  );
  var diabetes = parseInt(document.getElementById("diabetes").value);
  var hypertension = parseInt(document.getElementById("hypertension").value);

  var url = "/api/predict_risk";

  jQuery.post(url, {
    age: age,
    sex: sex,
    height: height,
    weight: weight,
    alcohol: alcohol,
    smoking: smoking,
    geneticRisk: geneticRisk,
    physicalActivity: physicalActivity,
    diabetes: diabetes,
    hypertension: hypertension,
  }),
    function (data, status) {
      console.log(data.risk_percentage);
      document.getElementById(
        "result"
      ).innerHTML = `<h2>${data.risk_percentage}</h2>`;
      console.log(status);
    };
}
