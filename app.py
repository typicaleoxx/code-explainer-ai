# this file defines the Streamlit user interface
# it allows a user to paste code and receive an AI generated analysis


import streamlit as st

from prompt_template import build_prompt
from ai_client import generate_explanation


# configure page settings
st.set_page_config(page_title="Code Intelligence AI", layout="wide")


# main title displayed in the browser
st.title("Code Intelligence AI")


# short explanation of what the tool does
st.markdown(
    """
Paste a code snippet and receive a structured engineering analysis.

The AI will analyze:

• Code purpose  
• Logic breakdown  
• Execution walkthrough  
• Code quality issues  
• Performance analysis  
• Security concerns  
• Refactored version
"""
)


# create a large input box for the user to paste code
code_input = st.text_area("Paste your code here", height=300)


# analyze button triggers the AI analysis
if st.button("Analyze Code"):

    # ensure the user entered code
    if code_input.strip() == "":
        st.warning("Please paste some code before analyzing.")

    else:

        # show the code with syntax highlighting
        st.subheader("Submitted Code")
        st.code(code_input, language="python")

        # build the prompt sent to the AI model
        prompt = build_prompt(code_input)

        # show a spinner while the model processes the request
        with st.spinner("Analyzing code..."):

            result = generate_explanation(prompt)

        # display the AI analysis
        st.subheader("AI Analysis")
        st.markdown(result)
