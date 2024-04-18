from utils.utils import *
from AI.AI_helper import *
from dotenv import load_dotenv

#for now only run it once

ai = AI()
reader = Reader_and_DB()


class Checker:
    def __init__(self):
        self.emails = []
        self.email = None
        self.text = ""
        self.percentage = 0
        self.avg = 0
        self.prompt = ""
    
    
    def get_email(self):
        if len(self.emails) > 0:
            self.email = self.emails.pop(0)
            return self.email
        return None
    
    def get_text(self):
        self.text = str(self.email)
        return self.text
    
    def get_percentage(self, ai_response):
        for i in range(10):
            print(i)
            print(self.text)
            self.prompt = ai.create_prompt(self.text)
            print(self.prompt)
            response = ai.get_response(self.prompt)
            print(response)
            self.percentage = ai.get_percentage(response)
            ai.clear_prompt()
        self.avg = ai.get_avrg()
        ai_response.put(self.avg)
        return self.avg
    
    def clear_all(self):
        ai.clear_all()
        return True
    
    def run(self, end, filters, email, password, ai_response):
        callback = queue.Queue()
        reader.read_multithreading(callback, filters, email, password, end)
        while True:
            if not end.empty():
                break
            if not callback.empty():
                self.emails.append(callback.get())
                if(self.get_email()):
                    self.get_text()
                    self.get_percentage(ai_response)
                    self.clear_all()
            time.sleep(1)
        return True
    

