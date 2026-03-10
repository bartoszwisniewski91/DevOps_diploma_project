# Obraz bazowego Pythona
FROM python:3.11-slim

# Katalog roboczy wewnątrz kontenera
WORKDIR /app

# Kopiowanie listy zależności
COPY requirements.txt .

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie kodu źródłowego
COPY app.py .

# Port aplikacji
EXPOSE 5000

# Komenda startowa
CMD ["python", "app.py"]