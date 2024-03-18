#for now just for testing im not gonna get the texts from the chats and emails but from a file
# we need a phishing email and a normal email to test the model (It is not trained for that but i think it will work)

class Reader:
    def __init__(self):
        self.phishing = open('phishing.txt', 'r').read()
        self.normal = open('normal.txt', 'r').read()

    def get_phishing(self):
        return self.phishing

    def get_normal(self):
        return self.normal