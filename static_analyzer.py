# this module performs static code analysis using Python's AST module
# it extracts structural information about the program before sending it to the LLM

import ast


def analyze_code_structure(code: str):
    """
    Parse the input code into an AST and extract structural metrics.
    """

    analysis = {
        "functions": 0,
        "loops": 0,
        "conditionals": 0,
        "assignments": 0,
        "function_calls": 0,
        "imports": 0,
        "security_warnings": [],
    }

    try:
        # convert the code string into an abstract syntax tree
        tree = ast.parse(code)

    except SyntaxError as e:
        return {"error": f"Syntax error in code: {e}"}

    # walk through every node in the syntax tree
    for node in ast.walk(tree):

        # count function definitions
        if isinstance(node, ast.FunctionDef):
            analysis["functions"] += 1

        # count loops
        if isinstance(node, (ast.For, ast.While)):
            analysis["loops"] += 1

        # count if statements
        if isinstance(node, ast.If):
            analysis["conditionals"] += 1

        # count assignments
        if isinstance(node, ast.Assign):
            analysis["assignments"] += 1

        # count imports
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            analysis["imports"] += 1

        # detect function calls
        if isinstance(node, ast.Call):
            analysis["function_calls"] += 1

            # detect potentially dangerous calls
            if isinstance(node.func, ast.Name):

                if node.func.id in ["eval", "exec"]:
                    analysis["security_warnings"].append(
                        f"Use of dangerous function: {node.func.id}"
                    )

    return analysis
