def calculate_average(scores):
    total = 0

    for score in scores:
        total += score

    return total / len(scores)

scores = [70, 85, 90, 65, 100]

average = calculate_average(scores)

print(f"Average {average:.1f}")