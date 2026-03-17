# Używamy lekkiego obrazu Pythona
FROM python:3.10-slim

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy plik wymagań i instalujemy je
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy resztę kodu (folder flask_app i inne)
COPY . .

# Gunicorn będzie nasłuchiwał na porcie 5000
EXPOSE 5000

# Komenda startowa
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "flask_app.app:app"]