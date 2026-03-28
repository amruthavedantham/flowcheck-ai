from src.ingestion import extract_text_from_pdf
from src.nlp_processing import extract_steps
from src.embeddings import generate_embeddings
from src.vector_search import build_faiss_index, search_similar
from src.rules import run_all_checks


def run_pipeline(file_path):

    print(f"\nProcessing file: {file_path}")

    # 1️ Extract text from PDF
    text = extract_text_from_pdf(file_path)

    print("\nExtracted Text:")
    print(text[:1000])


    # 2️ Extract workflow steps
    steps = extract_steps(text)

    print("\nDetected Steps:")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")


    # 3️ Clean steps (remove noise)
    cleaned_steps = []

    for step in steps:
        if 3 <= len(step.split()) <= 15:
            cleaned_steps.append(step)

    steps = cleaned_steps

    print("\nCleaned Steps:")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")


    # 4️ Generate embeddings
    embeddings = generate_embeddings(steps)


    # 5️ Build FAISS index
    index = build_faiss_index(embeddings)


    # Optional similarity search
    if len(steps) > 0:
        query_embedding = embeddings[0]
        distances, indices = search_similar(index, query_embedding)

        print("\nSimilarity Search Results:")
        print(indices)


    # 6️ Run rule-based gap detection
    rule_results = run_all_checks(steps)

    print("\nRule Engine Results:")
    print(rule_results)


    # 7️ AI reasoning placeholder (Phi-3 not yet enabled)
    print("\nSkipping AI reasoning (Phi-3 disabled for now)\n")

    ai_results = {
        "missing_steps": [],
        "unclear_steps": [],
        "logical_issues": []
    }


    # 8️ Final result format for frontend
    result = {
        "missing_steps": rule_results.get("missing_steps", []),

        "unclear_steps": rule_results.get("unclear_steps", []),

        "logical_issues": (
            rule_results.get("duplicate_steps", []) +
            rule_results.get("short_steps", [])
        ),

        "suggested_improvements": [
            "Clarify ambiguous workflow steps",
            "Add more specific action descriptions"
        ]
    }
    return result