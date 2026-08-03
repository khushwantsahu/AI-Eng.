import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Groq Api Key is not here.")

client = Groq(api_key= my_api_key)

model = "llama-3.3-70b-versatile"

Sys_msg = {
    "role":"system",
    "content":"You are a helpful assistant that suggests online food delivery apps based on user preferences. Provide recommendations and brief descriptions of each app."
}
message = {
    "role":"user",
    "content":"suggest me online app delivery food app"
}
messages = [Sys_msg,message]

response = client.chat.completions.create(model=model,messages= messages,temperature= 0)

print(response)