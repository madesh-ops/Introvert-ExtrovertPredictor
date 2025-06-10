# Introvert/Extrovert Predictor

This project is a machine learning web application that predicts whether a person is an introvert or extrovert based on their responses to a set of features. The project consists of a Jupyter notebook for model training and a Flask web app for user interaction and prediction.

![image](https://github.com/user-attachments/assets/811ac2f8-29c6-48d9-9523-c50061d34b02)



## Project Structure

- `classification.ipynb`: Jupyter notebook for data preprocessing, model training, and saving the trained model and preprocessors.
- `personality_dataset.csv`: The dataset used for training the model, containing features and personality labels.
- `model.pkl`: The trained logistic regression model.
- `scaler.pkl`, `le1.pkl`, `le2.pkl`, `le3.pkl`: Saved StandardScaler and LabelEncoders used for preprocessing.
- `app.py`: Flask web application for serving predictions.
- `templates/index.html`: HTML template for the web interface.
- `requirements.txt`: List of required Python packages.

## How It Works

1. **Data Preprocessing and Model Training (Jupyter Notebook):**
    - The dataset is loaded and checked for missing values.
    - Categorical features are encoded using `LabelEncoder`.
    - Missing values are imputed using `SimpleImputer`.
    - Features are scaled using `StandardScaler`.
    - The data is split into training and test sets.
    - A logistic regression model is trained to classify introvert/extrovert.
    - The trained model, scaler, and encoders are saved as `.pkl` files for later use.

2. **Web Application (Flask):**
    - Users interact with a web form to input feature values.
    - The Flask app loads the trained model, scaler, and encoders.
    - User input is preprocessed (label encoding and scaling) to match the training pipeline.
    - The model predicts whether the user is an introvert or extrovert.
    - The result is displayed on the web page.

## How to Run

1. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Train the Model (if needed):**
   - Run `classification.ipynb` to preprocess data and train the model. This will generate the required `.pkl` files.
3. **Start the Web App:**
   ```bash
   python app.py
   ```
4. **Open the Web Interface:**
   - Go to `http://localhost:5000` in your browser.
   - Enter the required features and click Predict to see the result.

## Notes
- Ensure the order and type of features in the web form match the model's expectations.
- The model and preprocessors must be present in the project directory for the app to work.

## License
This project is licensed under the MIT License.
