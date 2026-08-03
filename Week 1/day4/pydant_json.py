import os
from pathlib import Path
from pickle import load
from groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel

class Complent(BaseModel):
    name:str
    email:str
    number:int
    issue:str


schema = Complent.model_json_schema()

response_formate={
    "type":"json_object"
}

load_dotenv()
my_api = os.getenv("GROQ_API_KEY")
if not my_api:
    raise ValueError("no api key")

client = Groq(api_key=my_api)


model = "llama-3.3-70b-versatile"


user_prompt = f'''
    Hii my name is Khushwant Sahu and i am raising an issue about my phone which produce a lot of heat during chaging , screening or even simple using can you please contact me in this number 1234539223 or you can also email me at abc@gamil.com
    '''

sys_prompt = f"""
    extrat the personal imformation from the user complent based on this schema {schema} and return the response in this format {response_formate}
"""

msg_user = {
    "role":"user",
    "content":user_prompt
}

msg_sys = {
    'role':"system",
    'content':sys_prompt
}

messages = [msg_sys,msg_user]

response = client.chat.completions.create(model=model,messages=messages,response_format=response_formate)

answer = response.choices[0].message.content
print(answer)


import json
info = answer
user_data= json.loads(info)
complent = Complent(**user_data)

print(complent.name)
print(complent.email)
print(complent.number)



