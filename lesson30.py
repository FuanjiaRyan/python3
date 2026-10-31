students = ["Ryan", "Peter", "John", "Mary", "David"]
scores = [85, 92, 76, 88, 95]

for student, score in zip(students, scores):
    print(f"{student}: {score}")

print("")

for index, (student, score) in enumerate(zip(students, scores), start=0):
    print(f"{index}. {student}: {score}")