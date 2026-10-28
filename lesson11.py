scores = [70, 85, 90, 65, 100]
total = 0
average = 0
count = 0

print("========== SCORE ANALYZER ==========")
print("")

for score in scores:
    print(f"Score: {score}")
    total += score
    if score >= 80:
        count += 1

average = total / len(scores)
print("")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Students with 80+: {count}")