#for now just for testing im not gonna get the texts from the chats and emails but from a file
# we need a phishing email and a normal email to test the model (It is not trained for that but i think it will work)

import os
import threading
import time
import queue
from utils import email_reader
from utils import database_work

class Reader_and_DB(database_work.DatabaseWork):
    def __init__(self):
        self.mail_obj = None
    
    def read_emails(self, filters, mail, password):
        self.mail_obj = email_reader.EmailReader(mail, password)
        self.mail_obj.login()
        # filters = {'number': 2, 'excluded_users': []}
        emails = self.mail_obj.get_emails(filters)
        # mail.debug_print()
        self.mail_obj.close()
        return emails
    
    def multithreading(self, callback, filters, end, mail, password):
        while True:
            emails = self.read_emails(filters, mail, password)
            for email in emails:
                text = self.mail_obj.get_plain_text(email)
                callback.put(text)
            # print("Reading emails")
            time.sleep(240)
            if not end.empty():
                break
        return True
    
    def read_multithreading(self, callback, filters, mail, password, end):
        threading.Thread(target=self.multithreading, args=(callback, filters, end, mail, password, )).start()
        return True
