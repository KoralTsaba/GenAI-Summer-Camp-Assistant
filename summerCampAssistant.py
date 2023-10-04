import os
import openai
from dotenv import load_dotenv
import re
from prompts import *

camp_signup = {'name': None, 'age': None, 'phone': None, 'email':None}

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

# Create msg to gpt-3.5-turbo model with the relevant msg (prompt)
def send_message(msg):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": msg
        }
    ],
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response['choices'][0]["message"]["content"]+'\n\n'

# Template to prepare the prompt
def create_prompt(type, msg):
    return f"""
{prompts[type]['begin']}
{msg}
{prompts[type]['end']}
"""

def sign_up():
    global camp_signup
    camp_signup = {'name': None, 'age': None, 'phone': None, 'email':None}
    print(send_message('Generate me a message that the sign up complete (max 15 words )'))

# Extract vars from gpt model to camp_signup dictionary
def extract_vars(message):
    pattern = r'name:\s*(\w+)\s*\n|age:\s*(\d+)\s*\n|number:\s*(\d+)\s*\n|email:\s*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
    matches = re.findall(pattern, message)
    for name, age, number, email in matches:
        if name:
            camp_signup['name'] = name
        if age:
            camp_signup['age'] = int(age)
        if number:
            camp_signup['phone'] = number
        if email:
            camp_signup['email'] = email

#First provided the chat model a summery about GenAi camp
init_prompt = create_prompt(INIT_PROMPT,genai_summer_camp_details)
send_message(init_prompt)

#Main loop
finish_flag = False
while not finish_flag:
    continue_flag = True
    msg = welcome_msg
    while continue_flag:
        msg = input(msg)
        router_prompt = create_prompt(ROUTER_PROMPT,msg)
        prompt_type = send_message(router_prompt)
        new_prompt = create_prompt(int(prompt_type), msg)
        msg = send_message(new_prompt)
        if int(prompt_type) == APPLICATION_PROMPT:
            extract_vars(msg)
            keys = ''
            continue_flag = False
            for key, val in camp_signup.items():
                if val == None:
                    continue_flag = True
                    keys = f'{keys}, {key}'
            
            if not continue_flag:
                sign_up(camp_signup)
            msg = send_message(f'generate for me a short message (max 30 words) which asks the parent for the following details {keys}')
            
    msg = send_message('generate a message for the client if he wants to continue (up to 20 words).explain the client that his answer must be YES or NO)')

    res = input(msg)
    finish_flag = res.upper() =='NO'

print('Thank you and have a good day')   

        

    

