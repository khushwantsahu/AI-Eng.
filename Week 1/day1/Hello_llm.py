import os       # to connect with system and set path
from pathlib import Path
from pickle import load  #To acces Path
from dotenv import load_dotenv #Load the env file
from groq import Groq  # to use Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Error")

client = Groq(api_key= my_api_key)

model = "llama-3.3-70b-versatile"

role = "user"

prompt = "Specification of Samsung m56"

message = {
    'role':role,
    'content':prompt
}
messages = [message]

response = client.chat.completions.create(model=model,messages=messages)

print(response)
