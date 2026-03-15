# Używamy lekkiego obrazu Pythona
FROM python:3.12-slim

# Ustawiamy katalog roboczy
WORKDIR /flask_app

# Kopiujemy wymagania i instalujemy je
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy resztę kodu
COPY . .

# Otwieramy port 5000 dla Flaska i metryk
EXPOSE 5000

# Uruchamiamy aplikację
CMD ["python", "app.py"]