scores = [45, 80, 32, 90, 65, 28, 75, 95, 50]

greater_scores = list(filter(lambda score: score >= 50, scores))

print(f"Original scores: {scores}")
print(f"Passing scores: {greater_scores}")