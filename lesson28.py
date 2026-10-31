scores = [85, 45, 90, 30, 65, 75, 40, 100]
grades = []

grades = [
    "A" if score >= 80
    else "B" if score >= 70
    else "C" if score >= 60
    else "D" if score >= 50
    else "F"
    for score in scores
]

print(grades)