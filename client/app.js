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

function calculateRisk() {
  const age = parseFloat(document.getElementById("ageInput").value);
  const sex = parseInt(document.getElementById("sex").value);
  const height = parseFloat(document.getElementById("height").value);
  const weight = parseFloat(document.getElementById("weight").value);
  const alcohol = parseFloat(document.getElementById("alcohol").value);
  const smoking = parseInt(document.getElementById("smoking").value);
  const geneticRisk = parseInt(document.getElementById("geneticRisk").value);
  const physicalActivity = parseFloat(
    document.getElementById("physicalActivity").value
  );
  const diabetes = parseInt(document.getElementById("diabetes").value);
  const hypertension = parseInt(document.getElementById("hypertension").value);

  // Hypothetical risk factor calculation
  let riskFactor = 0;
  riskFactor += age * 0.1;
  riskFactor += sex * 1.5;
  riskFactor += (weight / height) * 0.2;
  riskFactor += alcohol * 0.3;
  riskFactor += smoking * 2;
  riskFactor += geneticRisk * 1.7;
  riskFactor -= physicalActivity * 0.5;
  riskFactor += diabetes * 1.8;
  riskFactor += hypertension * 1.4;

  // Display result
  document.getElementById(
    "result"
  ).innerHTML = `<h3>Your Liver Cancer Risk Factor is: ${riskFactor.toFixed(
    2
  )}</h3>`;
}
