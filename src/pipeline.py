from src.ingestion import extract_text_from_pdf
from src.nlp_processing import extract_steps
from src.embeddings import generate_embeddings
from src.vector_search import build_faiss_index, search_similar
from src.rules import run_all_checks

import re


def run_pipeline(file_path):
    """
    Full FlowCheck AI pipeline
    """

    # 1️⃣ Extract text
    with open(file_path, "r") as f:
        text = f.read()

    # 2️⃣ Extract steps
    steps = extract_steps(text)

    # ✅ Clean steps
    def clean_steps(steps):
        cleaned = []

        for step in steps:
            if 3 <= len(step.split()) <= 15:
                cleaned.append(step)

        return cleaned

    steps = clean_steps(steps)

    # 3️⃣ Generate embeddings
    embeddings = generate_embeddings(steps)

    # 4️⃣ Build FAISS index
    index = build_faiss_index(embeddings)

    # Optional similarity
    if len(steps) > 0:
        query_embedding = embeddings[0]
        distances, indices = search_similar(index, query_embedding)

    # 5️⃣ Rule-based checks
    rule_results = run_all_checks(steps)

    print("\nSkipping AI reasoning (Phi-3 disabled for performance)\n")

    ai_results = {
        "missing_steps": [],
        "unclear_steps": [],
        "logical_issues": []
    }

    # Final output
    final_output = {
        "steps": steps,
        "rule_based_results": rule_results,
        "ai_analysis": ai_results
    }

    return final_output