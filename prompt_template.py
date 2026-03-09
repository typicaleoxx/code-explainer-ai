# this module defines the structured prompt sent to the Gemini model
# separating prompts from application logic makes it easier to improve instructions later


# build_prompt receives the user code and constructs a structured analysis request
def build_prompt(code_snippet: str) -> str:

    # this instruction tells the AI to behave like a senior engineer performing a code review
    prompt = f"""
You are a senior software engineer performing a professional code review.

Analyze the following code and produce a structured report.

Your report must contain these sections.

Code Summary
Explain what the code is intended to do.

Logic Explanation
Explain how the code works step by step.

Execution Walkthrough
Simulate what happens during program execution.

Code Quality Issues
Identify poor practices or maintainability concerns.

Performance Analysis
Explain time complexity and inefficiencies.

Security Concerns
Identify unsafe patterns or vulnerabilities.

Improved Version
Provide a cleaner refactored version of the code.

Here is the code to analyze:

{code_snippet}

Return the analysis using clear section headings.
"""

    return prompt
