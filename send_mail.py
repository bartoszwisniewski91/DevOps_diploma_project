import smtplib
import os
from email.mime.text import MIMEText

def send_notification():
    # Pobieranie danych z zmiennych środowiskowych (GitHub Secrets)
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    
    if not MAIL_USERNAME or not MAIL_PASSWORD:
        print("Błąd: Brak danych logowania w zmiennych środowiskowych!")
        return

    msg = MIMEText('Aplikacja Flask została pomyślnie wdrożona i uruchomiona!')
    msg['Subject'] = '🚀 DevOps Project - Deployment Success'
    msg['From'] = MAIL_USERNAME
    msg['To'] = MAIL_USERNAME # Wysyłasz do siebie

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Powiadomienie e-mail zostało wysłane pomyślnie!")
    except Exception as e:
        print(f"Błąd wysyłki: {e}")

if __name__ == "__main__":
    send_notification()