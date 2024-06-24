# Dynamic Pricing App on Ride Sharing Case

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](deploymentlink) 

## 🔍 About the project

This Streamlit application empowers users to estimate ride costs using a dynamic pricing model. By analyzing historical data with data-driven techniques, the model can adjust prices in real-time based on various factors. Built using a CatBoost Regression model, it considers features like vehicle type, number of riders and drivers, and expected ride duration to predict adjusted fares.

This project involved several key steps:

1. Data Wrangling: Data [was obtained from](https://statso.io/dynamic-pricing-case-study/) and meticulously prepared for analysis.
2. Exploratory Data Analysis: The data was thoroughly examined to understand its characteristics and identify potential patterns.
3. Feature Engineering: New features namely 'Dynamic_Price_M1' that is calculated using demand and supply multipliers, were created to generate adjusted fares.
4. Model Building and Evaluation: The CatBoost Regression model was trained and rigorously evaluated to ensure its accuracy. Hyperparameters were also optimized for peak performance.
5. Model Deployment: Finally, the model was deployed within the Streamlit app, making it accessible to users.

## Setup environment
```
conda create --name dynamic-pricing-app python=3.9
conda activate dynamic-pricing-app
pip install streamlit pickle-mixin pandas
```

## Run streamlit app
```
streamlit run app.py
```