import imaplib
import email



class EmailReader:
    def __init__(self, email_address, password, email_server = 'imap.gmail.com'):
        self.email_address = email_address
        self.password = password
        self.email_server = email_server
        self.mail = None
        self.channel = None
        self.number_to_read = "0"
        self.emails = []

    def login(self):
        self.mail = imaplib.IMAP4_SSL(self.email_server)
        self.mail.login(self.email_address, self.password)
    
    def open_channel(self, channel):
        self.channel = self.mail.select(channel)

    def get_emails(self, filters):
        self.number_to_read = filters['number']
        if self.number_to_read == '0':
            return []
        if self.number_to_read == 'all':
            self.number_to_read = str(min(1000, int(self.channel[0])))
        self.number_to_read = int(self.number_to_read)
        self.emails = []
        excluded_users = filters['excluded_users']
        for i in range(self.channel[0], self.channel[0] - self.number_to_read, -1):
            result, data = self.mail.fetch(str(i), '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            if email_message['From'] in excluded_users:
                continue
            self.emails.append(email_message)
        return self.emails
    
    def close(self):
        self.mail.close()
        self.mail.logout()
        self.mail = None
        self.channel = None
        self.number_to_read = "0"
        self.emails = []