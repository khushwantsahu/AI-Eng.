import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("No Api Key")

client = Groq(api_key = my_api_key)

model = "llama-3.3-70b-versatile"
role= "user"
prompt1 = "hii"
prompt2 = "write an email to my HR of 300 words"
prompt3 = "write an essay of 1000 words"


prompts = [prompt1,prompt2,prompt3]
#messages = []

for prmt in prompts:
    message = {
        "role":role,
        "content":prmt
    }
    
    messages=[message]
    
    response = client.chat.completions.create(model=model,messages= messages,max_tokens=100)
    usage = response.usage
    print(f"Prompt : {prmt}  -->Prompt Token : {usage.prompt_tokens}  --> Complition Token : {usage.completion_tokens} = Totlal Tokens = {usage.total_tokens} finish Reason :{response.choices[0].finish_reason}")

    