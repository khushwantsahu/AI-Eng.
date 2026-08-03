import os
from pathlib import Path
import re
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

my_api = os.getenv("GROQ_API_KEY")

if not my_api:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key = my_api)

model = "llama-3.3-70b-versatile"

def calculator(exp):
    try:
        return eval(exp)
    except Exception as e:
        print(f"Error evaluating expression: {e}")

def bookPrice(book_name):
    # Define a dictionary of book prices
    
    book_prices = {
        "The Great Gatsby": 100,
        "To Kill a Mockingbird": 250,
        "1984": 200,
        "Pride and Prejudice": 280,
        "The Catcher in the Rye": 230
    }

    if book_name in book_prices:
        return f"The price of '{book_name}' is {book_prices[book_name]} rupees."
    else:
        return None
    # Return the price of the book if it exists, otherwise return None
    #return book_prices.get(book_name, None)

tools = {
    "calculator": calculator,
    "bookPrice": bookPrice
}

System_prompt = '''
You are a BookShop Ai Assistent.

You have this Tools:
bookPrice(book_name) - returns the price of the book if it exists, otherwise returns None.
calculator(exp) - evaluates a mathematical expression and returns the result.
Important:
Call the tools Exactly like this example: bookPrice("The Great Gatsby") or calculator("200 + 50").

never write: 
calculator(exp="200 + 50")

never write:
bookPrice(book_name="The Great Gatsby")

Follow this rules:
1. Deside what you need to do based on the user input.
2. If you need to use a tool, call the tool with the correct parameters.only one tool at a time.
3. after writing action stop immediatly
4.never guess and invent a tool result.
5.wait until you receive the observation.
6.then decide the next ation.
7.when the tast complete, write the final answer.

formate:
Thought: <your thought process>
Action: <tool name>(<tool parameters>)

when you have the final answer, write it like this:
Final Answer: <your final answer>

'''

def run(prompt):
    messages = [
        {"role": "system", "content": System_prompt},
        {"role": "user", "content": prompt}
    ]

    
    for step in range(8):
        print(f"\n\n---- Step {step + 1} ---\n\n")

        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
    
        ans = response.choices[0].message.content
        print(ans)

        if "Final Answer:" in ans:
            break

        match = re.search(r'Action:\s*(\w+)\((.*)\)',ans)

        if match:
            tool_name = match.group(1)
            tool_input = match.group(2)
            tool_input = tool_input.strip()
            tool_input = tool_input.strip('"')  # Remove quotes if present

            

            if tool_name in tools:
                tool = tools[tool_name]
                observation = tool(tool_input)
            else:
                observation = f"Tool {tool_name} not found."

            print(f"\nObservation: {observation}\n")


            messages.append({
                    'role':'assistant',
                    'content':ans
                 })
            messages.append({
                'role':'user',
                'content':"Observation: "+str(observation)
            })


            time.sleep(2)


prompt = """
i want to buy the book "The Great Gatsby" is it available ?. How much does it cost? i have only 300 rupees. Can you tell me if I can buy it?and after buying it, if I have any money left?
"""
run(prompt)