import pandas as pd
import numpy as np
import sqlite3
from sklearn.ensemble import RandomForestRegressor
import os

# Configuration
DATA_PATH = "static/gld_price_data.csv"
DB_PATH = "gold_predictions.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS GoldPrice (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            SPX REAL,
            USO REAL,
            SLV REAL,
            EUR_USD REAL,
            GOLD REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def train_model(data_path):
    print("Training model... please wait.")
    gold_data = pd.read_csv(data_path)
    X = gold_data.drop(['Date', 'GLD'], axis=1)
    Y = gold_data['GLD']
    
    regressor = RandomForestRegressor(n_estimators=100)
    regressor.fit(X, Y)
    return regressor

def save_prediction(spx, uso, slv, eur, pred):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO GoldPrice (SPX, USO, SLV, EUR_USD, GOLD)
        VALUES (?, ?, ?, ?, ?)
    ''', (spx, uso, slv, eur, float(pred)))
    conn.commit()
    conn.close()

def show_history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM GoldPrice ORDER BY timestamp DESC LIMIT 10')
    rows = cursor.fetchall()
    
    if not rows:
        print("\nNo history found.")
    else:
        print("\n--- Recent Predictions ---")
        print(f"{'ID':<5} {'SPX':<10} {'USO':<10} {'SLV':<10} {'EUR/USD':<10} {'PRED GOLD':<10} {'Time'}")
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<10.2f} {row[2]:<10.2f} {row[3]:<10.2f} {row[4]:<10.2f} {row[5]:<10.2f} {row[6]}")
    conn.close()

def main():
    data_path = DATA_PATH
    if not os.path.exists(data_path):
        # Check alternative path
        alt_path = os.path.join("GoldPrice", DATA_PATH)
        if os.path.exists(alt_path):
            data_path = alt_path
        else:
            print(f"Error: Data file {data_path} not found.")
            return

    init_db()
    regressor = train_model(data_path)
    
    while True:
        print("\n--- Gold Price Prediction Menu ---")
        print("1. Predict Gold Price")
        print("2. View History")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            try:
                spx = float(input("Enter SPX: "))
                uso = float(input("Enter USO: "))
                slv = float(input("Enter SLV: "))
                eur = float(input("Enter EUR/USD: "))
                
                input_data = np.array([[spx, uso, slv, eur]])
                prediction = regressor.predict(input_data)[0]
                
                print(f"\nPredicted Gold Price: {prediction:.2f}")
                save_prediction(spx, uso, slv, eur, prediction)
                print("Prediction saved to database.")
                
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == '2':
            show_history()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
