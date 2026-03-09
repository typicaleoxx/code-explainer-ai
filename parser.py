# this module parses the AI generated analysis into structured sections
# it detects section headings even if the AI adds formatting like ### or **


def parse_analysis(text: str):

    sections = {
        "Code Summary": "",
        "Logic Explanation": "",
        "Execution Walkthrough": "",
        "Code Quality Issues": "",
        "Performance Analysis": "",
        "Security Concerns": "",
        "Improved Version": "",
    }

    current_section = None

    for line in text.split("\n"):

        clean_line = line.strip().lower()

        if "code summary" in clean_line:
            current_section = "Code Summary"
            continue

        elif "logic explanation" in clean_line:
            current_section = "Logic Explanation"
            continue

        elif "execution walkthrough" in clean_line:
            current_section = "Execution Walkthrough"
            continue

        elif "code quality issues" in clean_line:
            current_section = "Code Quality Issues"
            continue

        elif "performance analysis" in clean_line:
            current_section = "Performance Analysis"
            continue

        elif "security concerns" in clean_line:
            current_section = "Security Concerns"
            continue

        elif "improved version" in clean_line:
            current_section = "Improved Version"
            continue

        if current_section:
            sections[current_section] += line + "\n"

    return sections
