import os
import openai
import csv

openai.api_key = open('key.txt', 'r').readline()

with open('systemPrompt.txt', 'r') as file:
    SYSTEM_PROMPT = file.read()

def get_explanation(system_prompt, user_prompt):
    response = openai.ChatCompletion.create(
                   model='gpt-4',
                   messages=[
                       {'role': 'system', 'content': system_prompt},
                       {'role': 'user', 'content': user_prompt}
                   ],
# other parameters if you want
               )
    return response['choices'][0]['message']['content']

answers = []

for filename in os.listdir('jsons'):
    f = os.path.join('jsons', filename)
    file = open(f, 'r')
    user_prompt = file.read()
    subanswer = [int(filename[3:-5]),get_explanation(SYSTEM_PROMPT,user_prompt)]
    answers.append(subanswer)

answers = sorted(answers,key=lambda x:(x[0],x[1]))

fields = ['sampleNumber', 'GPT4_Score']

with open('output.csv', 'w') as f:
     
    # using csv.writer method from CSV package
    write = csv.writer(f)
     
    write.writerow(fields)
    write.writerows(answers)