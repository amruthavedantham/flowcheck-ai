from src.pipeline import run_pipeline

file_path = "data/sample.txt"  # put your SOP here

result = run_pipeline(file_path)

print("\nFINAL OUTPUT:\n")
print(result)