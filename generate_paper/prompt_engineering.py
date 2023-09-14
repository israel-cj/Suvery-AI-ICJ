import openai
import time
import json
from .run_llm import run_llm_code

def generate_prompt():
    prompt = """
Given a sentence asking for a specific topic generate a prompt to create a paper of 1500 words in a json format.
The goal is to generate a survey paper of no more than 1500 words incluiding references. 
This prompt must make sure the paper will be generated in a correct json format, where the heading will be the parts of the paper, e.g.  if the sentence required is: 
"Write a systematic survey or overview about the effectiveness of various scaffold cue presentation and methods to combine gradient approaches in neural tissue engineering for directed cell migration, with a focus on chemical, adhesive, mechanical, topographical, and electrical types of gradients."
The prompt format should be something like this:

```start
Write a survey paper as clear as posssible about the effectiveness of various scaffold cue presentation and methods to combine gradient approaches in neural tissue engineering for directed cell migration, with a focus on chemical, adhesive, mechanical, topographical, and electrical types of gradients.
This survey paper must be generated in json format including the next structure:
"
paper = [   
    {"heading": "Title", "text":"..."},
    {"heading": "Abstract", "text":"..."},
    {"heading": "Introduction", "text":"..."},
    {"heading": "Chemical Gradients", "text":"..."},
    {"heading": "Topographical Gradients", "text":"..."},
    {"heading": "Electrical Gradients", "text":"..."},
    {"heading": "Combining Gradient Approaches", "text":"..."},
    {"heading": "Conclusion", "text":"..."},
    {"heading": "References", "text":"..."}
]
"

Consider the max lenght of the paper 1500 words including references. The json format must be correct (every head should be close correctly). Always citing your sources, the format of the references should be the standar IEEE
```end

Each prompt generated ends with "```end" and starts with "```start".
The sentence to generate the prompt is: \n
"""
    return prompt
def generate_code(model, messages, max_tokens=500):
    if model == "skip":
        return ""

    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        stop=["```end"],
        temperature=0.5,
        max_tokens=max_tokens,
    )
    code = completion["choices"][0]["message"]["content"]
    code = code.replace("```start", "").replace("```", "").replace("<end>", "")
    return code

def generate_paper(model, messages):
    if model == "skip":
        return ""

    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        stop=["```end"],
        temperature=0.5,
        max_tokens=2048,
    )
    code = completion["choices"][0]["message"]["content"]
    code = code.replace("```start", "").replace("```", "").replace("<end>", "")
    return code

def generate_iterations(generator_X, instructions, model, iterations):
    prompt = generate_prompt()

    message = [
        {
            "role": "system",
            "content": "You are an expert scientist assistant creating a prompt for input in a LLM in order to create a survey paper. You answer only by creating a prompt. Answer as concisely as possible.",
        },
        {
            "role": "user",
            "content": prompt + generator_X,
        },
    ]

    i = 0
    while i < iterations:
        try:
            first_prompt = generate_code(model, message)
        except Exception as e:
            print("Error in LLM API." + str(e))
            time.sleep(60)  # Wait 1 minute before next request
            continue
        second_prompt = f"""
        ```start
        {first_prompt}
        ```end

        """
        second_message = [
        {
            "role": "system",
            "content": f"""
            You are an expert scientist assistant creating a paper of around 1500 words including references, not more. You answer only by creating a paper in the asked format. Answer as concisely as possible.\n
            {instructions}
            """,
        },
        {
            "role": "user",
            "content": second_prompt,
        },
        ]

        try:
            paper_json_string = generate_code(model, second_message, max_tokens=2000)
        except Exception as e:
            print("Error in LLM API." + str(e))
            time.sleep(60)  # Wait 1 minute before next request
            continue

        try:
            #paper = run_llm_code(
            #    paper_json_string,
            #)
            paper = json.loads(paper_json_string)
        except Exception as e:
            print(e)
            paper = None
        i = i + 1
    return paper
