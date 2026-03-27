import spacy
import re

# load spaCy model
nlp = spacy.load("en_core_web_sm")


def extract_steps(text):
    lines = text.split("\n")
    steps = []

    for line in lines:
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # ❌ Remove references, URLs, citations
        if any(keyword in line.lower() for keyword in [
            "http", "www", "cdc", "mmwr", "journal", "doi", "published", "source:"
        ]):
            continue

        # ❌ Remove very long sentences (likely paragraphs)
        if len(line.split()) > 20:
            continue

        # ❌ Remove question-like lines
        if line.endswith("?"):
            continue

        # ❌ Remove random single words
        if len(line.split()) <= 2:
            continue

        # ✅ Keep only structured steps
        if re.match(r"^\d+\.|\-|\•", line):
            steps.append(line)

        # ✅ OR action sentences (start with verb)
        elif re.match(r"^(Check|Verify|Ensure|Collect|Analyze|Prepare|Submit|Review)", line):
            steps.append(line)

    return steps