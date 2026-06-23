from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import pandas as pd
import numpy as np
import sqlite3
from sklearn.ensemble import RandomForestRegressor
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Configuration
DATA_PATH = "static/gld_price_data.csv"
if not os.path.exists(DATA_PATH):
    DATA_PATH = "GoldPrice/static/gld_price_data.csv"

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
            USD_INR REAL,
            INTEREST REAL,
            CPI REAL,
            GOLD REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def train_model():
    print("Training model (7 features)... please wait.")
    gold_data = pd.read_csv(DATA_PATH)
    # X now includes SPX, USO, SLV, EUR/USD, USD_INR, Interest_Rate, CPI
    X = gold_data.drop(['Date', 'GLD'], axis=1)
    Y = gold_data['GLD']
    
    regressor = RandomForestRegressor(n_estimators=100)
    regressor.fit(X, Y)
    return regressor

# Initialize global regressor
init_db()
regressor = train_model()

@app.route('/')
def index():
    return render_template('index_flask.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Simple placeholder for registration
        return redirect(url_for('login'))
    return render_template('register_flask.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simple placeholder for login logic
        return redirect(url_for('predict'))
    return render_template('login_flask.html')

@app.route('/adminlogin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        # Simple placeholder for admin login
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return redirect(url_for('history'))
    return render_template('adminlogin_flask.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            spx = float(request.form['spx'])
            uso = float(request.form['uso'])
            slv = float(request.form['slv'])
            eur = float(request.form['eur'])
            usd_inr = float(request.form['usd_inr'])
            ir = float(request.form['ir'])
            cpi = float(request.form['cpi'])
            
            input_data = np.array([[spx, uso, slv, eur, usd_inr, ir, cpi]])
            prediction = regressor.predict(input_data)[0]
            
            # Gold price calculation
            # GLD ETF tracks roughly 1/10th of an ounce
            usd_per_ounce = float(prediction) * 10
            # Gram Gold = Ounce / 31.1035
            # Use the user-provided exchange rate
            price_inr_10g = (usd_per_ounce * usd_inr) / 3.11035
            
            # Save to database
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO GoldPrice (SPX, USO, SLV, EUR_USD, USD_INR, INTEREST, CPI, GOLD)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (spx, uso, slv, eur, usd_inr, ir, cpi, float(prediction)))
            conn.commit()
            conn.close()
            
            return render_template('predict_flask.html', 
                                 spx=spx, uso=uso, slv=slv, eur=eur, 
                                 usd_inr=usd_inr, ir=ir, cpi=cpi,
                                 price_usd=f"{prediction:.2f}",
                                 price_inr=f"{price_inr_10g:,.2f}")
        except Exception as e:
            return f"Error: {str(e)}"
    
    return render_template('data_flask.html')

@app.route('/history')
def history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM GoldPrice ORDER BY timestamp DESC LIMIT 20')
    rows = cursor.fetchall()
    
    processed_rows = []
    for row in rows:
        # row schema: id(0), spx(1), uso(2), slv(3), eur_usd(4), usd_inr(5), ir(6), cpi(7), gold(8), timestamp(9)
        # Calculate INR using the stored USD_INR rate for that specific record
        try:
            rate = row[5] if row[5] else 83.5
            gold_usd = row[8]
            price_inr = (gold_usd * 10 * rate) / 3.11035
            processed_rows.append(list(row) + [f"{price_inr:,.2f}"])
        except:
            processed_rows.append(list(row) + ["N/A"])
            
    conn.close()
    return render_template('history_flask.html', rows=processed_rows)

# Helper for static files if they are in the GoldPrice/static directory
@app.route('/static/<path:filename>')
def custom_static(filename):
    static_dirs = ['static', 'GoldPrice/static']
    for s_dir in static_dirs:
        if os.path.exists(os.path.join(s_dir, filename)):
            return send_from_directory(s_dir, filename)
    return "File not found", 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
