# House Price Prediction using Machine Learning

## Overview

This project implements an end-to-end Machine Learning pipeline for predicting California housing prices using Linear Regression. The workflow includes exploratory data analysis, model training, evaluation, model serialization, and deployment through a Streamlit web application.

## Dataset

The project uses the California Housing Dataset provided by Scikit-Learn.

### Features

* Median Income (MedInc)
* House Age (HouseAge)
* Average Rooms (AveRooms)
* Average Bedrooms (AveBedrms)
* Population
* Average Occupancy (AveOccup)
* Latitude
* Longitude

### Target Variable

* Median House Value (MedHouseVal)

---

## Workflow

1. Data Loading and Exploration
2. Exploratory Data Analysis (EDA)
3. Correlation Analysis
4. Train-Test Split (80:20)
5. Linear Regression Model Training
6. Model Evaluation
7. Model Serialization using Pickle
8. Streamlit Deployment

---

## Results

| Metric   | Score |
| -------- | ----- |
| MAE      | 0.533 |
| MSE      | 0.556 |
| RMSE     | 0.746 |
| R² Score | 0.576 |

### Key Findings

* The model explains approximately **57.6%** of the variance in housing prices.
* No missing values were found in the dataset.
* Outliers were identified in AveRooms, AveBedrms, AveOccup, and Population.
* The model serves as a strong baseline for further experimentation with advanced regression techniques.

---

## Visualizations

The project includes:

* Correlation Heatmap
* Actual vs Predicted Scatter Plot
* Residual Error Analysis

These visualizations help evaluate feature relationships and model performance.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit

---

## Future Improvements

* Feature Engineering
* Feature Scaling
* Ridge Regression
* Cross Validation
* Random Forest Regression
* XGBoost Regression
* Hyperparameter Tuning

---

## Conclusion

This project demonstrates the complete machine learning workflow from data analysis and model development to deployment through an interactive Streamlit application. The implementation establishes a baseline regression model and provides a foundation for exploring more advanced predictive techniques.
