scores = [65, 80, 45, 90, 72]

fail = any(score < 50 for score in scores)
passed = all(score >= 50 for score in scores)

print(fail)
print(passed)