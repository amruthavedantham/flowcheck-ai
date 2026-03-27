import re


def extract_steps(text):
    """
    Extract workflow steps from SOP text.
    Supports formats like:
    - Step 1:
    - 1.
    """

    steps = []

    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        # match "Step 1:"
        step_match = re.match(r"Step\s*\d+:\s*(.*)", line, re.IGNORECASE)

        # match "1."
        number_match = re.match(r"\d+\.\s*(.*)", line)

        if step_match:
            steps.append(step_match.group(1).strip())

        elif number_match:
            steps.append(number_match.group(1).strip())

    return steps