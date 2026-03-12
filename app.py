from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_devops():
    version = "1.0.0"
    return f"""
    <html>
    <head>
        <title>DevOps Project</title>
        <style>
            body {{
                font-family: Arial;
                text-align: center;
                background-color: #0f172a;
                color: white;
                margin-top: 80px;
                overflow: hidden;
            }}

            h1 {{
                font-size: 40px;
            }}

            .version {{
                font-size: 20px;
                margin-bottom: 40px;
            }}

            .container {{
                font-size: 60px;
                position: relative;
                animation: move 6s linear infinite;
            }}

            @keyframes move {{
                0%   {{ left: -200px; }}
                100% {{ left: 100%; }}
            }}
        </style>
    </head>
    <body>

        <h1>Witaj w Projekcie Dyplomowym DevOps!</h1>
        <div class="version">Wersja aplikacji: {version}</div>

        <div class="container">
            🐳🚢⚙️
        </div>

        <p>Kontener DevOps w ruchu...</p>

    </body>
    </html>
    """

@app.route('/health')
def health_check():
    # Endpoint do sprawdzania stanu aplikacji przez Kubernetes
    return jsonify(status="healthy", message="Aplikacja działa poprawnie"), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)