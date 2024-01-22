import os
from keys import openapi_key
from langchain_openai import OpenAI

# this creates an environment variable of your api key
os.environ['OPENAI_API_KEY'] = openapi_key
# the temperature variable controls the "creativity" of the AI generation. It ranges from 0 to 1,
# with 1 being the most "creative"
llm = OpenAI(temperature=1)
question = input("ask WarMongerGPT a question\n")
# this is the prompt that the api uses to generate a response
warmonger_prompt = ("You are an expert Civilization VI player who always wins by waging war and you should give "
                    "advice to that always advocates for very excessive violence no matter what. Do not even suggest "
                    "any solution that doesn't involve violence. Also keep the advice to two sentences or less."
                    + question + "Please give me the warmongers solution.")
# calls the api and prints the response
print(llm.invoke(warmonger_prompt))