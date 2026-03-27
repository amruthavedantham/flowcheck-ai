import subprocess
import json


def call_phi3(prompt):
    """
    Calls Phi-3 properly (non-interactive mode)
    """

    result = subprocess.run(
        ["ollama", "run", "phi3:mini"],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    return result.stdout


def analyze_process(steps):
    """
    Send steps to Phi-3 for reasoning
    """

    formatted_steps = "\n".join([f"{i+1}. {step}" for i, step in enumerate(steps)])

    prompt = f"""
You are a process analyst.

Analyze the workflow and return ONLY valid JSON.

STRICT RULES:
- No explanation
- No comments
- No extra text
- No null values
- Use simple strings only
- Output must be valid JSON

Workflow:
{formatted_steps}

Return format:
{{
  "missing_steps": ["step1", "step2"],
  "unclear_steps": ["step1"],
  "logical_issues": ["issue1"]
}}
"""
    print("Calling Phi-3 model...")
    
    response = call_phi3(prompt)

    cleaned = clean_json_response(response)

    return cleaned

def clean_json_response(response):
    """
    Extract and parse JSON safely
    """
    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        json_str = response[start:end]
        return json.loads(json_str)
    except:
        return {
            "missing_steps": [],
            "unclear_steps": [],
            "logical_issues": [],
            "error": "Invalid JSON from model"
        }