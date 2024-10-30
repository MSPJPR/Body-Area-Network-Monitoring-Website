from flask import Flask, render_template, jsonify
import sqlite3
import random
import time

app = Flask(__name__)

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('health_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS health_metrics
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       timestamp TEXT,
                       heart_rate INTEGER,
                       oxygen_level INTEGER)''')
    conn.commit()
    conn.close()

# Simulate real-time data insertion
def insert_data():
    conn = sqlite3.connect('health_data.db')
    cursor = conn.cursor()
    heart_rate = random.randint(60, 100)  # Simulate heart rate
    oxygen_level = random.randint(90, 100)  # Simulate oxygen level
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO health_metrics (timestamp, heart_rate, oxygen_level) VALUES (?, ?, ?)",
                   (timestamp, heart_rate, oxygen_level))
    conn.commit()
    conn.close()

# Route to serve the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch data as JSON
@app.route('/data')
def data():
    insert_data()  # Simulate data insertion
    conn = sqlite3.connect('health_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, heart_rate, oxygen_level FROM health_metrics ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    data = [{'timestamp': row[0], 'heart_rate': row[1], 'oxygen_level': row[2]} for row in rows]
    return jsonify(data)

if __name__ == '__main__':
    init_db()  # Initialize database
    app.run(host='0.0.0.0', port=5000)
