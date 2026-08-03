import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key = my_api_key)

model = "llama-3.3-70b-versatile"

def get_text(prompt):
    message = {
        'role': 'user',
        'content':prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model,messages=messages)
    ans = response.choices[0].message.content
    print(ans)


prompt = """
#role -
you are an support assistent in reseption of mobile shop.
#task -
you have to classify the issue in category
#constraints -
you have to classify the issue in one of the following categories:
1. Billing Issue   
2. Technical Issue
3. Account Issue
return

#output formate-
your answer should be in one or two word only and answer only in one of the above categories.

#zero/one shot -
for example if an user say my laptop is stoped working then its an technical issue.

#FallBack-
if the issue is unrelevent to any of the categories mention in contraints, then the answer OTHER


this is a user complaint:
my gf is angry
"""

get_text(prompt)



