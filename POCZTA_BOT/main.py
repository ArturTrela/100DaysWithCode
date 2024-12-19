import imaplib
import smtplib
from email.utils import parseaddr
from email.header import decode_header
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email
import time
from dotenv import load_dotenv
import os
load_dotenv()


# Konfiguracja
EMAIL = os.getenv("GMAIL_ADDRESS")
PASSWORD = os.getenv('GMAIL_BOT_PASSWORD') # Uzyj hasla aplikacji
IMAP_SERVER = 'imap.gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


def decode_header_field(header):
    """Funkcja dekodująca dowolny nagłówek (np. subject, from) z obsługą polskich znaków."""
    if not header:
        return ""
    decoded_parts = decode_header(header)
    decoded_text = ""
    for part, encoding in decoded_parts:
        if isinstance(part, bytes):
            # Dekodowanie na podstawie kodowania lub domyślnie utf-8
            decoded_text += part.decode(encoding or 'utf-8', errors='ignore')
        else:
            decoded_text += part
    return decoded_text

def decode_email_body(msg):
    """Funkcja dekodująca treść wiadomości (body) z obsługą UTF-8."""
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            if content_type in ("text/plain", "text/html") and "attachment" not in content_disposition:
                # Dekodowanie treści wiadomości
                payload = part.get_payload(decode=True)
                if payload:
                    body = payload.decode(part.get_content_charset() or 'utf-8', errors='ignore')
                    break
    else:
        # Dla wiadomości niemultipartowych
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode(msg.get_content_charset() or 'utf-8', errors='ignore')
    return body

def read_emails():
    # Połączenie z serwerem IMAP
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select('inbox')

    # Szukamy nieprzeczytanych wiadomości
    result, data = mail.search(None, 'UNSEEN')
    email_ids = data[0].split()

    for email_id in email_ids:
        # Odczytanie wiadomości
        result, msg_data = mail.fetch(email_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])

        # Dekodowanie tematu
        raw_subject = msg['subject']
        subject = decode_header_field(raw_subject) if raw_subject else "(Brak tematu)"

        # Dekodowanie nadawcy
        raw_from = msg['from']
        sender = decode_header_field(parseaddr(raw_from)[0]) if raw_from else "(Nieznany nadawca)"

        # Dekodowanie treści wiadomości (body)
        body = decode_email_body(msg)

        print(f'Odebrano wiadomość od: {sender}')
        print(f'Temat: {subject}')
        print(f'Treść wiadomości:\n{body}')

        adr = parseaddr(raw_from)[1]
        # Odpowiadanie na wiadomosc
        reply_to_email(adr,sender, subject)
    mail.logout()



def load_html_template(filepath):
    """Funkcja wczytuje treść szablonu HTML z pliku."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def reply_to_email(adr,sender, subject):
    try:
        # Tworzenie wiadomości e-mail
        msg = MIMEMultipart('related')
        msg['From'] = EMAIL
        msg['To'] = adr
        msg['Subject'] = f'Re: {subject}'

        # Wczytanie szablonu HTML
        html_template = load_html_template('email_template.html')

        # Personalizacja treści szablonu
        personalized_html = html_template.replace('{sender}', sender).replace('{subject}', subject)

        # Dodanie treści HTML
        msg_alternative = MIMEMultipart('alternative')
        msg.attach(msg_alternative)
        msg_alternative.attach(MIMEText(personalized_html, 'html'))

        # Dodanie obrazu jako załącznika inline
        with open('POWERALL_BEZ_TLA.png', 'rb') as img:
            logo = MIMEImage(img.read())
            logo.add_header('Content-ID', '<logo_powerall>')
            logo.add_header('Content-Disposition', 'inline', filename="POWERALL_BEZ_TLA.png")
            msg.attach(logo)

        # Wysyłanie wiadomości
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
            print(f'Odpowiedź wysłana do: {sender}')
    except Exception as e:
        print(f"Błąd podczas wysyłania odpowiedzi: {e}")



if __name__ == '__main__':
    while True:
        print("Sprawdzanie czy są nowe wiadomości... ")
        read_emails()
        time.sleep(60)  # Sprawdzaj co minute