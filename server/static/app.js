function updateAgeInput() {
  const ageSlider = document.getElementById("ageSlider");
  const ageInput = document.getElementById("ageInput");
  ageInput.value = ageSlider.value;
}

/*function updateAgeSlider() {
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

  console.log(
    age,
    sex,
    height,
    weight,
    alcohol,
    smoking,
    geneticRisk,
    physicalActivity,
    diabetes,
    hypertension
  );
}*/
