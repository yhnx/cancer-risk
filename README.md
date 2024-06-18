# Project Rysk

#### Video Demo: <(https://youtu.be/qOienrfvjIs)>

#### Description:

# Liver Cancer Risk Detector

This project is a web-based application designed to predict the risk of liver cancer based on several user-provided parameters. The application is hosted on Render.com and is accessible [https://cancer-risk.onrender.com](https://cancer-risk.onrender.com/). The app employs a logistic regression model trained on a dataset from Kaggle to output a percentage risk score for liver cancer.

## Overview

### Parameters Required

- **Age**: The age of the user.
- **Gender**: The gender of the user.
- **Height**: Height in centimeters.
- **Weight**: Weight in kilograms (used to calculate BMI).
- **Alcohol Consumption**: Weekly alcohol consumption in standardized units.
- **Smoking Status**: Whether the user smokes or not.
- **Genetic Risk**: Categorized as low, medium, or high.
  - **Low**: No family history of liver cancer.
  - **Medium**: Distant relatives with liver cancer.
  - **High**: Close family members with liver cancer.
- **Physical Activity**: Hours of physical activity per week.
- **Diabetes**: Whether the user has diabetes.
- **Hypertension**: Whether the user has hypertension.

### Model Training

The model is trained using the `liver_disease_data` dataset from Kaggle. The training process involves using pandas, numpy, and matplotlib for data analysis and cleaning. A logistic regression model is chosen for its ability to provide probabilistic outputs, suitable for risk prediction.

## Project Files

### Data Files

- **liver_disease_data.csv**: The dataset used for training the model.

### Jupyter Notebooks

- **Training Notebook**: This notebook includes the code for data cleaning, exploratory data analysis, and training of both linear regression and logistic regression models. The logistic regression model was chosen due to its better performance in this context.

### Model Files

- **model.pkl**: The trained logistic regression model serialized as a pickle file.
- **columns.json**: A JSON file containing the relevant columns used for the model training.

### Web Application Files

#### Backend

- **app.py**: The main Flask application file.

  - Takes user input from the form.
  - Validates the input and redirects to the error page if necessary.
  - Uses the trained model to predict the risk percentage.
  - Renders the results on the risk.html page.

- **util.py**: Utility functions used in the app.
  - Handles the prediction logic.
  - Converts the sklearn model to an ONNX model to optimize for web hosting constraints.

#### Frontend

- **templates/**: Contains HTML files.

  - **index.html**: The home page with the input form.
  - **risk.html**: Displays the predicted risk percentage.
  - **apology.html**: Error handling page.

- **static/**: Contains static files like CSS and JS.
  - **slide.js**: JavaScript file for form interactions.
  - **styles.css**: CSS file for styling the pages (if needed).

### Dependencies

- **pandas**: Data manipulation and analysis.
- **numpy**: Numerical computations.
- **matplotlib**: Data visualization.
- **scikit-learn**: Model training and evaluation.
- **onnxruntime**: Running the ONNX model.
- **flask**: Web framework for Python.

## Design Choices

1. **Logistic Regression Model**: Chosen for its probabilistic output, making it suitable for risk prediction.
2. **ONNX Model**: Converted the scikit-learn model to ONNX format for efficient deployment on web servers with limited resources.
3. **Flask Framework**: Simple and lightweight framework, suitable for this project’s needs.
4. **Bootstrap for UI**: Used Bootstrap for a clean and responsive design, without spending excessive time on the front-end development.

## How to Run the Project

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/cancer-risk.git
   cd cancer-risk
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Application**:

   ```bash
   cd server
   flask run
   ```

4. **Access the Application**:
   Open your browser and go to `http://127.0.0.1:5000`.

## Conclusion

This project demonstrates a practical application of machine learning for health risk assessment. It combines data analysis, model training, and web development to provide a user-friendly tool for predicting liver cancer risk. Future improvements could include enhancing the UI/UX and incorporating more sophisticated models.

---

Feel free to explore the code, or provide feedback. For any queries, please contact [yehenasuramuni@hotmail.com].
