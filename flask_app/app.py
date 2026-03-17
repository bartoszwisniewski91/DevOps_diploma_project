from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
app.secret_key = 'devops-secret-key'

# Inicjalizacja metryk - TYLKO TYLE
metrics = PrometheusMetrics(app)

# Przykładowy licznik
login_counter = metrics.counter('logins_total', 'Liczba logowań')

@app.route('/')
def index():
    return "Serwer działa! Ver 1.1.4.6 Wejdź na /metrics"

@app.route('/login')
def login():
    login_counter.inc()
    return "Zalogowano!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)