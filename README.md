# ⚡ ENERGY_APP  
## Monthly Electricity Consumption & Bill Predictor

🔗 **Live Demo:** https://hasssssankhalid0001-eng-energy-app-app-d2wcy6.streamlit.app/

---

## 📌 Project Overview

This project predicts the **monthly electricity consumption of a household** and estimates the **electricity bill** based on appliance usage.

The main objective is to help users understand:

- How much electricity they consume monthly
- How appliance usage impacts billing
- How they can optimize usage to reduce cost

---

## 🎯 Problem Statement

Most households do not clearly know:

- Electricity consumption of individual appliances  
- How daily usage affects monthly bills  
- How changes in appliance usage impact total cost  

This project solves this problem using **Machine Learning**.

---

## 🧠 Methodology

### 🔢 Inputs Taken

The model takes the following inputs:

- Number of Fans  
- Number of Air Conditioners (ACs)  
- Number of Laptops  
- Number of Washing Machines  
- Daily usage hours of each appliance  

### 📈 What the System Does

1. Calculates estimated usage patterns  
2. Predicts monthly electricity consumption (kWh)  
3. Estimates the electricity bill  

---

## 🤖 Machine Learning Model

**Model Used:** Random Forest Regressor  

### Why Random Forest?

- Handles nonlinear relationships effectively  
- Works well with structured/tabular data  
- Reduces overfitting compared to single decision trees  
- Provides strong prediction accuracy  

The model was trained on generated household energy consumption data.

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- Scikit-learn  
- Pandas  
- NumPy  

---

