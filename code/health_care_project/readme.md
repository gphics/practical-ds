## Health care project

### Click [here](https://www.kaggle.com/datasets/prasad22/healthcare-dataset) to view the dataset

### Objectives
#### Exploratory Data Analysis:

    * Demographic Profiling: Does a specific age group or gender correlate with higher rates of certain conditions (e.g., are older patients more frequently admitted for "Diabetes" or "Hypertension")?

    * Operational Efficiency: Which Hospitals or Doctors have the longest average admission durations, and is there a correlation with the Medical Condition being treated?

    * Financial Analysis: What is the distribution of Billing Amounts? Are certain Insurance Providers (e.g., Cigna vs. Medicare) associated with more expensive treatments or longer stays?

    * Blood Type Availability: Is there a mismatch between the most common patient Blood Types and the severity of the medical conditions treated?

    * Medication Patterns: For a specific condition like "Asthma," what is the most frequently prescribed Medication, and does it impact the length of the stay?

#### Modelling:
    * Length of Stay (LoS) Prediction (Regression):
    Goal: Predict the number of days a patient will be hospitalized based on their condition, age, and medication.
    Algorithms: XGBoost Regressor, Random Forest, or LGBM.

    * Medical Condition Classification (Multi-class Classification):
    Goal: Predict the Medical Condition based on laboratory results (if available in your feature set), age, and symptoms.
    Algorithms: Support Vector Machines (SVM) or Neural Networks.

    * Billing Amount Estimation (Regression):
    Goal: Forecast the total cost of a hospital visit to help insurance companies or patients estimate expenses.
    Algorithms: Linear Regression or CatBoost.

    * Anomalous Billing Detection (Unsupervised Learning):
    Goal: Identify "outlier" bills that are significantly higher than the average for a specific condition/medication pair—useful for fraud detection.
    Algorithms: Isolation Forest or Local Outlier Factor (LOF).