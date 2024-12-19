import imaplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email
import time
from dotenv import load_dotenv
env = load_dotenv(".env")

# Konfiguracja
EMAIL = 'arturtrela.automation@gmail.com'
PASSWORD = ""  # Uzyj hasla aplikacji
IMAP_SERVER = 'imap.gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


def read_emails():
    # Polaczenie z serwerem IMAP
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select('inbox')

    # Szukamy nieprzeczytanych wiadomosci
    result, data = mail.search(None, 'UNSEEN')
    email_ids = data[0].split()

    for email_id in email_ids:
        # Odczytanie wiadomosci
        result, msg_data = mail.fetch(email_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])

        subject = msg['subject']
        sender = msg['from']

        print(f'Odebrano wiadomosc od: {sender}, Temat: {subject}')

        # Odpowiadanie na wiadomosc
        reply_to_email(sender, subject)

    mail.logout()


def reply_to_email(to_email, subject):
    # Tworzenie wiadomosci
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg['Subject'] = f'Re: {subject}'

    body = 'Dziekujemy za Twoja wiadomosc. Odpowiemy jak najszybciej.'
    msg.attach(MIMEText(body, 'plain'))

    # Wysylanie wiadomosci
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        print(f'Odpowiedz wyslana do: {to_email}')


if __name__ == '__main__':
    while True:
        read_emails()
        time.sleep(60)  # Sprawdzaj co minute