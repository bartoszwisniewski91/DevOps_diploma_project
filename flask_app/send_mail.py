import smtplib
import os
from email.mime.text import MIMEText

def send_notification():
    # Pobieranie danych z zmiennych środowiskowych (GitHub Secrets)
    gmail_user = os.getenv('GMAIL_USER')
    gmail_password = os.getenv('GMAIL_APP_PASSWORD')
    
    if not gmail_user or not gmail_password:
        print("Błąd: Brak danych logowania w zmiennych środowiskowych!")
        return

    msg = MIMEText('Aplikacja Flask została pomyślnie wdrożona i uruchomiona!')
    msg['Subject'] = '🚀 DevOps Project - Deployment Success'
    msg['From'] = gmail_user
    msg['To'] = gmail_user # Wysyłasz do siebie

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()
        print("Powiadomienie e-mail zostało wysłane pomyślnie!")
    except Exception as e:
        print(f"Błąd wysyłki: {e}")

if __name__ == "__main__":
    send_notification()