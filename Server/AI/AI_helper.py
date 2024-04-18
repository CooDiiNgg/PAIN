# this should be the model for the AI that we will use to classify the emails
# it will use a simple local model hosted by ollama
#themodel is called llama2-uncensored it has a local api that we can use to classify the emails
# we need to write the prompts for the model to classify the emails and make him answer with only percentages so we can verify the results
# that means we need to run the tests multiple times and get the average of the results so we have a more accurate result


import ollama

class AI:
    def __init__(self):
        self.avrg = 0
        self.current = 0
        self.curr_arr = []
        self.response = None
        self.text_response = ""
        self.prompt = "I want you to answer with a percentage of how sure you are that the email is a phishing email. Only the percentage and nothing else. Start the percentage with 10%% and increase or decrease the vlue of your liking. If the email contains a link or an attachment please increase the percentage. If it does not contain information about passwords or usernames please decrease the percentage with 10%. If you are not sure just say 55%% and we will take it from there. Include ONLY one percentage value! The email is the following:"
    
    def get_response(self, text):
        self.response = ollama.chat(model='llama2-uncensored', messages=[{'role': 'user', 'content': text,}])
        print(self.response)
        self.text_response = self.response['message']['content']
        return self.text_response
    
    def get_percentage(self, text):
        self.text_response = text
        try:
            self.current = self.text_response.split("%")[-2]
            self.current = self.current.split(" ")[-1]
            self.current = float(self.current)
            self.curr_arr.append(self.current)
            self.avrg = sum(self.curr_arr) / len(self.curr_arr)
        except:
            self.current = 55.0
            self.curr_arr.append(self.current)
            self.avrg = sum(self.curr_arr) / len(self.curr_arr)
        return self.current
    
    def get_avrg(self):
        return self.avrg
    
    def create_prompt(self, text):
        self.prompt = self.prompt + " " + text
        return self.prompt
    
    def clear_all(self):
        self.avrg = 0
        self.current = 0
        self.curr_arr = []
        self.response = None
        self.text_response = ""
        self.prompt = "I want you to answer with a percentage of how sure you are that the email is a phishing email. Only the percentage and nothing else. Start the percentage with 10%% and increase or decrease the vlue of your liking. If the email contains a link or an attachment please increase the percentage. If it does not contain information about passwords or usernames please decrease the percentage with 10%. If you are not sure just say 55%% and we will take it from there. Include ONLY one percentage value! The email is the following:"
        return True
    
    def clear_prompt(self):
        self.prompt = "I want you to answer with a percentage of how sure you are that the email is a phishing email. Only the percentage and nothing else. Start the percentage with 10%% and increase or decrease the vlue of your liking. If the email contains a link or an attachment please increase the percentage. If it does not contain information about passwords or usernames please decrease the percentage with 10%. If you are not sure just say 55%% and we will take it from there. Include ONLY one percentage value! The email is the following:"
        return True
    
