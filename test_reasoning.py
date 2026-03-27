from src.reasoning import analyze_process

steps = [
    "User submits request",
    "Manager approves request",
    "Deliver product"
]

result = analyze_process(steps)

print("\nAI Analysis:\n")
print(result)