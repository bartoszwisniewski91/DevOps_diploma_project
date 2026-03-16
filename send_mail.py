import smtplib
import os
from email.mime.text import MIMEText
from datetime import datetime

def send_notification():
    # Pobieranie danych z GitHub Secrets przekazanych przez main.yml
    gmail_user = os.getenv('GMAIL_USER')
    gmail_password = os.getenv('GMAIL_APP_PASSWORD')
    
    if not gmail_user or not gmail_password:
        print("Błąd: Brak danych logowania w zmiennych środowiskowych!")
        return

    # Pobieramy aktualny czas wdrożenia
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Treść wiadomości z informacją o Zero Downtime
    body = f"""
    🚀 Nowa wersja aplikacji została wdrożona!
    
    Szczegóły techniczne:
    - Typ wdrożenia: Zero Downtime (Gunicorn Hot Reload)
    - Data i godzina: {now}
    - Status: Sukces
    
    Aplikacja jest dostępna pod adresem: http://192.168.0.108:5000
    Metryki Prometheus: http://192.168.0.108:5000/metrics
    
    Wiadomość wygenerowana automatycznie przez GitHub Actions.
    """

    msg = MIMEText(body)
    msg['Subject'] = f'✅ DevOps Success: Zero Downtime Deployment ({now})'
    msg['From'] = gmail_user
    msg['To'] = gmail_user

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()
        print("Powiadomienie e-mail o wdrożeniu Zero Downtime zostało wysłane!")
    except Exception as e:
        print(f"Błąd wysyłki: {e}")

if __name__ == "__main__":
    send_notification()