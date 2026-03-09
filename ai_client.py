# this module communicates with the OpenRouter API
# it sends prompts to a language model and returns the generated explanation


import os
import requests
from dotenv import load_dotenv


# load environment variables from the .env file
load_dotenv()


# retrieve the OpenRouter API key
API_KEY = os.getenv("OPENROUTER_API_KEY")


# OpenRouter endpoint used for chat completions
API_URL = "https://openrouter.ai/api/v1/chat/completions"


# function that sends the prompt to the model and returns the explanation
def generate_explanation(prompt: str) -> str:

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    payload = {
        # use a stable model available through OpenRouter
        "model": "openai/gpt-4o-mini",
        # messages follow the standard chat format used by modern LLM APIs
        "messages": [{"role": "user", "content": prompt}],
    }

    try:

        # send the HTTP request to the OpenRouter API
        response = requests.post(API_URL, headers=headers, json=payload)

        # convert the API response into JSON format
        data = response.json()

        # ensure the expected response structure exists before accessing it
        if "choices" in data:
            return data["choices"][0]["message"]["content"]

        # if something unexpected happens return the raw response for debugging
        return str(data)

    except Exception as e:

        # return a readable error message
        return f"API request failed: {str(e)}"
