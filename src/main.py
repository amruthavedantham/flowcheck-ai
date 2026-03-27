from src.ingestion import extract_text_from_pdf
from src.nlp_processing import extract_steps


def run_pipeline(file_path):

    print(f"Processing file: {file_path}")

    # extract text from PDF
    text = extract_text_from_pdf(file_path)

    print("Extracted Text:")
    print(text[:1000])

    # extract workflow steps
    steps = extract_steps(text)

    print("\nDetected Steps:")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")

    result = {
        "missing_steps": [],
        "unclear_steps": [],
        "logical_issues": [],
        "suggested_improvements": []
    }

    return result