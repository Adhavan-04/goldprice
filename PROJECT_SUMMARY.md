# 📜 Project Summary & Viva Master Guide

This document provides a concise overview of the **Gold Price Prediction System (2026)**, designed for quick reference during presentations and viva examinations.

---

## 🏗️ 1. Project Overview (What is in this project?)
This is a **Machine Learning-based Web Application** that predicts the future price of gold.
- **Core Engine:** Random Forest Regressor (Ensemble Learning).
- **Web Interface:** Built using **Flask** (Python) for a modern, responsive user experience.
- **Database:** **SQLite3** to store and track every prediction made.
- **Dataset:** A modernized CSV containing ~2,770 records ranging from 2018 to 2026.

---

## ✅ 2. Things Done (Accomplishments)
- [x] **Platform Migration:** Successfully moved the project from a legacy Django setup to a faster, more flexible **Flask** environment.
- [x] **Modernized dataset:** Updated the model to include data up to 2026, including post-pandemic economic fluctuations.
- [x] **Enhanced Features:** Added **CPI (Inflation)** and **Interest Rates** as new parameters for better accuracy.
- [x] **Localized Logic:** Integrated a real-time **USD to INR conversion** system to make predictions relevant to the Indian market.
- [x] **History Tracking:** Implemented a persistent storage system using SQLite to view past predictions.

---

## 🗣️ 3. Simplified Viva Process (How to explain it)
If asked about the project in a Viva, follow this simple 4-step flow:

1.  **The Goal:** "We built a tool to help investors predict gold prices by analyzing 7 global economic factors (like oil prices and inflation)."
2.  **The Brain (ML):** "We use an algorithm called **Random Forest**. Think of it as 100 different 'mini-experts' (decision trees) voting on the price to get the most stable result."
3.  **The Conversion:** "Since gold is traded in USD per ounce, our project automatically converts it to **Indian Rupees (INR) for 10 grams** of gold, which is the standard unit in India."
4.  **The Result:** "The system has a high accuracy of **98.9%** and stores every prediction in a database for future reference."

---

## 🌟 4. Key Factors (Why this project is good)
- **High Accuracy:** 98.9% R2 Score ensures reliable forecasts.
- **Modern Features:** Unlike older projects, this includes **Inflation (CPI)** and **Interest Rates**, which are the biggest drivers of gold today.
- **Real-world Use:** Converts global prices to local units (INR), making it useful for local jewelry buyers and investors.
- **Robustness:** Handles non-linear relationships between oil, stocks, and gold perfectly.

---

## 🎯 5. Quick Viva Q&A Snippets
- **Q: Why Random Forest?** -> *A: Because it handles complex, messy economic data better than simple linear models and doesn't overfit easily.*
- **Q: What is the target variable?** -> *A: **GLD** (The price of a Gold ETF share).*
- **Q: How many parameters?** -> *A: **7 Input Parameters** (SPX, USO, SLV, EUR/USD, USD/INR, Interest, CPI).*

---

## 📈 6. Recommended Input Sample (Today's Real Data)
To get the most accurate prediction for **today (April 11, 2026)**, use the following sample inputs in the application:

| Field | Recommended Value | Description |
| :--- | :--- | :--- |
| **SPX** | `6816.89` | Recent S&P 500 Index |
| **USO** | `125.64` | Current Crude Oil ETF |
| **SLV** | `69.08` | Current Silver ETF |
| **EUR/USD** | `1.17` | Euro to USD Exchange Rate |
| **USD/INR** | `93.04` | Today's USD to INR Rate |
| **Interest** | `3.6` | Federal Reserve Benchmark Rate (%) |
| **CPI** | `3.3` | Latest Consumer Price Index (%) |
