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
    
    def get_response(self, text):
        self.response = ollama.chat(model='llama2', messages=[{'role': 'user', 'content': 'Why is the sky blue?',}])
        self.text_response = self.response['messages']['content']
        try:
            self.current = self.text_response.split("%")[0]
            self.current = self.current.split(" ")[-1]
            self.current = float(self.current)
            self.curr_arr.append(self.current)
            self.avrg = sum(self.curr_arr) / len(self.curr_arr)
        except:
            self.current = 55
            self.curr_arr.append(self.current)
            self.avrg = sum(self.curr_arr) / len(self.curr_arr)
        return self.current