from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_devops():
    return "<h1>Witaj w Projekcie Dyplomowym DevOps!</h1><p>Wersja: 1.0.0</p>"

@app.route('/health')
def health_check():
    # Standardowy endpoint do sprawdzania stanu aplikacji przez K8s
    return jsonify(status="healthy", message="Aplikacja działa poprawnie"), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)