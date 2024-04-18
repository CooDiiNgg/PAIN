import email
import oauth2
import imaplib
import ssl
import re
from bs4 import BeautifulSoup



class EmailReader:
    def __init__(self, email_address, password, email_server = 'valkanovi.com', port = 993):
        self.email_address = email_address
        self.password = password
        self.email_server = email_server
        self.port = port
        self.mail = None
        self.number_to_read = "0"
        self.emails = []

    def login(self):
        #fix ssl dh key too small
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.set_ciphers('DEFAULT@SECLEVEL=1')
        self.mail = imaplib.IMAP4_SSL(self.email_server, self.port, ssl_context=context)
        self.mail.login(self.email_address, self.password)
        # if self.email_server == 'imap.gmail.com':
        #     #we ned to us the google authentification function because else we cannot login
        #     #use OAuth2
        #     self.mail = imaplib.IMAP4_SSL(self.email_server)
        #     self.auth_string = oauth2.GenerateOAuth2String(self.email_address, self.password, base64_encode=True)
    
    def open_channel(self, channel = 'INBOX'):
        self.channel = self.mail.select(channel)

    def get_emails(self, filters):
        self.open_channel()
        self.number_to_read = filters['number']
        if self.number_to_read == 0:
            return []
        self.number_to_read = int(min(self.number_to_read, int(self.channel[1][0])))
        self.emails = []
        excluded_users = filters['excluded_users']
        for i in range(int(self.channel[1][0]) + 1 - self.number_to_read, int(self.channel[1][0]) + 1):
            status, data = self.mail.fetch(str(i), '(RFC822)')
            if status == 'OK':
                email_message = email.message_from_bytes(data[0][1])
                if email_message['From'] not in excluded_users:
                    self.emails.append(email_message)
        return self.emails
    
    def get_plain_text(self, email):
        text = ""
        for payload in email.walk():
            if payload.get_content_type().lower() == 'text/plain' or payload.get_content_type().lower() == 'text/html':
                pload = payload.get_payload(decode = True)
                if pload:
                    text += pload.decode()
        text = BeautifulSoup(text, 'html.parser').get_text()
        text = re.sub(r"=\d{2}", "", text)
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text
    
    def debug_print(self):
        for email in self.emails:
            print()
            print()
            print("From: " + email['From'])
            print("Subject: " + email['Subject'])
            print("Date: " + email['Date'])
            text = ""
            for payload in email.walk():
                print("Content type: " + str(payload.get_content_type()))
                if payload.get_content_type().lower() == 'text/plain' or payload.get_content_type().lower() == 'text/html':
                    text += str(payload.get_payload())
            text = BeautifulSoup(text, 'html.parser').get_text()
            text = re.sub(r"=\d{2}", "", text)
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            print("Body: " + str(text))

    def close(self):
        self.mail.close()
        self.mail.logout()
        self.mail = None
        self.channel = None
        self.number_to_read = "0"
        self.emails = []