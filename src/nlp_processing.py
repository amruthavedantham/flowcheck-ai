import spacy
import re

# load spaCy model
nlp = spacy.load("en_core_web_sm")


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

        # Skip empty lines
        if not line:
            continue

        # Remove references / citations
        if any(keyword in line.lower() for keyword in [
            "http", "www", "cdc", "mmwr", "journal", "doi", "published", "source:"
        ]):
            continue

        # Remove very long sentences
        if len(line.split()) > 20:
            continue

        # Remove question lines
        if line.endswith("?"):
            continue

        # Remove random short words
        if len(line.split()) <= 2:
            continue

        # Detect "Step 1:"
        step_match = re.match(r"Step\s*\d+:\s*(.*)", line, re.IGNORECASE)

        # Detect "1."
        number_match = re.match(r"\d+\.\s*(.*)", line)

        if step_match:
            steps.append(step_match.group(1).strip())

        elif number_match:
            steps.append(number_match.group(1).strip())

        # Bullet steps
        elif re.match(r"^\-|\•", line):
            steps.append(line)

        # Action sentences
        elif re.match(r"^(Check|Verify|Ensure|Collect|Analyze|Prepare|Submit|Review)", line):
            steps.append(line)

    return steps