#for now just for testing im not gonna get the texts from the chats and emails but from a file
# we need a phishing email and a normal email to test the model (It is not trained for that but i think it will work)

import os

class Reader:
    def __init__(self):
        self.path = os.path.dirname(__file__)
        self.path = self.path + "/phishing.txt"
        self.phishing = open(self.path, 'r').read()
        self.path = os.path.dirname(__file__)
        self.path = self.path + "/normal.txt"
        self.normal = open(self.path, 'r').read()

    def get_phishing(self):
        return self.phishing

    def get_normal(self):
        return self.normal