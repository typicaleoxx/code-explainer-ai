def build_prompt(code, structure_analysis):

    return f"""
You are a senior software engineer performing a code review.

Static analysis of the code:

Functions: {structure_analysis["functions"]}
Loops: {structure_analysis["loops"]}
Conditionals: {structure_analysis["conditionals"]}
Assignments: {structure_analysis["assignments"]}
Function Calls: {structure_analysis["function_calls"]}
Imports: {structure_analysis["imports"]}
Security warnings: {structure_analysis["security_warnings"]}

Code:

{code}

Provide:

1. Code Summary
2. Logic Explanation
3. Execution Walkthrough
4. Code Quality Issues
5. Performance Analysis
6. Security Concerns
7. Improved Version
"""
