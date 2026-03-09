# this file defines the Streamlit web interface
# it handles user interaction and communicates with the backend AI logic


import streamlit as st

from gemini_client import generate_explanation
from prompt_template import build_prompt


# configure the page title shown in the browser
st.set_page_config(page_title="Code Intelligence AI")


# display the application title
st.title("Code Intelligence AI")


# short description shown under the title
st.write("Paste code and receive a structured engineering analysis.")


# create a large text input area where users paste their code
code_input = st.text_area("Paste your code here", height=300)


# create a button that triggers the AI analysis
if st.button("Analyze Code"):

    # ensure the user provided code before sending a request
    if code_input.strip() == "":
        st.warning("Please paste some code before analyzing.")

    else:

        # build the AI prompt using the provided code
        prompt = build_prompt(code_input)

        # show a loading indicator while the AI processes the request
        with st.spinner("Analyzing code..."):

            # send the prompt to Gemini and retrieve the explanation
            explanation = generate_explanation(prompt)

        # display the AI generated report
        st.markdown(explanation)
