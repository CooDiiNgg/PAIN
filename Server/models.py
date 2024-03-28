from utils.utils import *
from AI.AI_helper import *

#for now only run it once

ai = AI()
reader = Reader()

phishing = reader.get_phishing()
normal = reader.get_normal()

for i in range(10):
    prompt = ai.create_prompt(phishing)
    response = ai.get_response(prompt)
    percentage = ai.get_persentage(response)
    ai.clear_prompt()
    print(percentage)

avrg = ai.get_avrg()
print("AVRG:", avrg)
ai.clear_all()

for i in range(10):
    prompt = ai.create_prompt(normal)
    response = ai.get_response(prompt)
    percentage = ai.get_persentage(response)
    ai.clear_prompt()
    print(percentage)

avrg = ai.get_avrg()
print("AVRG:", avrg)
ai.clear_all()