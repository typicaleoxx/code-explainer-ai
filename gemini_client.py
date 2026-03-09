# this module handles communication with the Gemini API
# isolating API communication in a separate file keeps the system modular


import os
import google.generativeai as genai
from dotenv import load_dotenv


# load environment variables from the .env file
load_dotenv()


# configure the Gemini client using the API key from environment variables
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# initialize the model that will generate responses
model = genai.GenerativeModel("gemini-pro")


# this function sends a prompt to Gemini and returns the generated explanation
def generate_explanation(prompt: str) -> str:

    # send the prompt to the Gemini model
    response = model.generate_content(prompt)

    # extract and return the generated text
    return response.text
