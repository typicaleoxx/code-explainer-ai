import re


def clean_markdown(text):
    # remove markdown headings
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)

    # remove stray triple quotes
    text = text.replace('"""', "")

    # remove bold markers
    text = text.replace("**", "")

    return text


def parse_analysis(text):

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

        for section in sections.keys():
            if section.lower() in line.lower():
                current_section = section
                continue

        if current_section:
            sections[current_section] += line + "\n"

    # clean formatting
    for key in sections:
        sections[key] = clean_markdown(sections[key]).strip()

    return sections
