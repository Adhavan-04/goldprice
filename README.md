# Gold Price Prediction System (Modernized 2026)

## 📌 Project Overview
The **Gold Price Prediction System** is an advanced machine learning-based web application modernized to forecast gold prices in the 2026 financial landscape. By analyzing seven critical economic indicators, including global stock indices, commodity prices, and local currency rates (USD/INR), the system provides precise predictions to assist in strategic financial planning and investment.

---

## 🚀 Modernization & Problem Statement
Gold prices are notoriously volatile, influenced by a complex web of global and local factors. This project addresses the challenge of **predictive uncertainty** in a post-2024 economic environment. We have enhanced the system by incorporating real-time currency conversion (INR) and expanding the feature set to include macroeconomic indicators like Interest Rates and CPI, ensuring the model remains accurate under shifting market dynamics.

---

## 🧠 Model and Algorithm
- **Algorithm:** **Random Forest Regressor** (Ensemble Learning).
- **Why Random Forest?** It excels at capturing non-linear relationships and interactions between diverse economic factors. It is robust against outliers and provides high predictive stability by aggregating results from 100 decision trees.
- **Model Type:** Supervised Machine Learning (Regression).

---

## 📊 Dataset Details
- **Source:** Modernized historical dataset (2018–2026).
- **Dataset File:** `static/gld_price_data.csv`.
- **Records:** Approximately **2,770 data points**.
- **Features (Input Parameters):**
  1. **SPX:** S&P 500 Stock Market Index.
  2. **USO:** United States Oil Fund (Crude Oil Prices).
  3. **SLV:** Silver Trust Price (Silver correlation).
  4. **EUR/USD:** Euro to US Dollar exchange rate.
  5. **USD/INR:** US Dollar to Indian Rupee exchange rate (Critical for local pricing).
  6. **INTEREST:** Global/Central Bank Interest Rates.
  7. **CPI:** Consumer Price Index (Inflation indicator).
- **Target Variable:** **GLD** (Gold ETF Price tracked at ~1/10th of an ounce).

---

## 📊 Model Performance & Parameters

### 1. Model Parameters
- **Number of Input Features:** 7 Features (Comprehensive Economic Indicators).
- **Algorithm:** RandomForestRegressor.
- **Hyperparameters:**
  - `n_estimators`: 100 (Number of trees in the forest).
  - `criterion`: 'squared_error' (Default MSE).
  - `random_state`: 2 (Ensures reproducibility).

### 2. Evaluation Metrics
The model has been rigorously tested using an 80-20 train-test split:
- **Model Accuracy (R2 Score):** **~0.989 (98.9%)**
- **Mean Absolute Error (MAE):** **~1.31**
- **Mean Squared Error (MSE):** **~5.60**
- **Root Mean Squared Error (RMSE):** **~2.37**

---

## 🏗️ Machine Learning Pipeline

This project follows a structured **Machine Learning Pipeline** to ensure consistent and reliable predictions. 

### Pipeline Stages:
1.  **Data Acquisition:** Loading the modernized historical gold dataset from CSV.
2.  **Preprocessing:** Feature selection (dropping irrelevant columns like `Date`) and handling target variables.
3.  **Model Training:** Fitting the `RandomForestRegressor` ensemble model.
4.  **Inference:** Using the trained model to predict and store results.

**Note on implementation:** While the project follows this logical pipeline, it currently uses a **manual implementation** (direct script execution) rather than an automated `sklearn.pipeline.Pipeline` object. This allows for easier debugging and transparency during the development phase.

---

## 🛠️ Technology Stack
| Component | Technology |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, Modern UI, Jinja2 Templates |
| **Backend** | Python, Flask (Robust Web Framework) |
| **Machine Learning** | Scikit-Learn (Random Forest), Pandas, NumPy |
| **Database** | SQLite3 (Local persistent history tracking) |
| **Environment** | Python 3.13+, venv |

---

## 📚 Key Libraries Used
- `pandas`: Data processing and feature engineering.
- `numpy`: Numerical optimizations.
- `scikit-learn`: Implementation of the Random Forest Regressor and model evaluation.
- `flask`: Web application routing and server-side logic.
- `sqlite3`: Management of the prediction history database.

---

## ⚙️ How the Project Works (INR logic)
1. **Dynamic Training:** The system trains the **Random Forest Regressor** on 7 features including USD/INR and CPI.
2. **User Input:** Users provide current market indices (SPX, USO, etc.) and the current **USD/INR** rate.
3. **Dual-Currency Prediction:**
   - The model predicts the **GLD ETF price** (USD).
   - The system then calculates the **Gram Gold Price in INR** for a 10g unit:
     - `Price per Ounce = Prediction * 10`
     - `Price per Gram (INR) = (Price per Ounce * USD_INR) / 31.1035`
     - `10g Price = Price per Gram * 10`
4. **Persistence:** Features and final predictions are stored in a **SQLite database**.
5. **Timeline View:** Users can track prediction trends in the history dashboard.

---

## 📝 Viva Questions & Answers

### 1. What is the main objective of this project?
**Ans:** To build a modernized forecasting system that predicts gold prices in INR/USD by analyzing complex economic factors like inflation (CPI), interest rates, and currency exchange volatility.

### 2. Why are USD/INR and CPI included in the modernized model?
**Ans:** **USD/INR** directly affects the landing cost of gold in India. **CPI (Inflation)** is a primary driver for gold as it is often used as a hedge against inflation. Including these makes the model much more accurate for 2026 market conditions.

### 3. How do you convert the GLD prediction to Indian Market prices (24K Gold)?
**Ans:** The GLD ETF roughly tracks 1/10th of an ounce. We multiply the prediction by 10 to get the ounce price, convert it to INR using the current rate, and then divide by 31.1035 to get the price per gram (since 1 troy ounce ≈ 31.1g). Finally, we multiply by 10 for the standard 10g Indian market unit.

### 4. Why use Random Forest instead of a simple Linear Regression?
**Ans:** Gold price behavior involves non-linear interactions (e.g., oil and interest rate correlations changing over time). Random Forest handles these complexities better and is less prone to overfitting than a simple linear model.

### 5. How does the system handle high-volume prediction storage?
**Ans:** It use **SQLite3**, which provides a lightweight but robust local storage solution. Every prediction record includes timestamps and all 7 input features for future audit and analysis.

---

## 💡 Tips to "Defeat" or Improve This Project

Want to build a model that outperforms this one? Here are the strategic areas where this project can be "defeated" or improved:

1.  **Algorithm Upgrade:** While Random Forest is stable, switching to **XGBoost, LightGBM, or CatBoost** can often squeeze out higher accuracy on tabular data through gradient boosting.
2.  **Time-Series Analysis:** This project treats data points as independent. Implementing **LSTM (Long Short-Term Memory)** or **Prophet** would allow the model to capture temporal trends and seasonality.
3.  **Advanced Hyperparameter Tuning:** Using `GridSearchCV` or `RandomizedSearchCV` to fine-tune `max_depth`, `min_samples_split`, and `max_features` could yield better results.
4.  **Feature Expansion:** Adding a **Volatility Index (VIX)** or **News Sentiment Analysis** (using NLP) would provide the model with "market fear" context that currently isn't captured.
5.  **Handling Overfitting:** Random Forest can overfit to historical noise. Implementing **Cross-Validation** and **feature pruning** would create a more generalized and robust model.

---

## 🛠️ How to Run
1. Activate environment: `.\venv\Scripts\activate`
2. Start server: `python app_web.py`
### 4. Access at: `http://127.0.0.1:5000/`

---

## 📈 Recommended Input Sample (April 2026)
Use these real-time values for high-accuracy predictions today:
- **SPX:** `6816.89`
- **USO:** `125.64`
- **SLV:** `69.08`
- **EUR/USD:** `1.17`
- **USD/INR:** `93.04`
- **INTEREST:** `3.6`
- **CPI:** `3.3`
#   g o l d p r i c e  
 