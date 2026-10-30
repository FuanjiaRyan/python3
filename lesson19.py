import lesson14

students = [
    {
        "name": "Ryan",
        "age": 20,
        "course": "Software Engineering",
        "score": 85
    },

    {
        "name": "Joferson",
        "age": 24,
        "course": "Lab Sciences",
        "score": 93
    },

    {
        "name": "Randy",
        "age": 30,
        "course": "Biomedical Sciences",
        "score": 50
    }
]

print("========== STUDENTS ==========")
print("")
for student in students:
    print(f"Name: {student["name"]}")
    print(f"Age: {student["age"]}")
    print(f"Course: {student["course"]}")
    print(f"Score: {student["score"]}")
    grade = lesson14.calculate_grade(student["score"])
    print(f"Grade: {grade}")
    #if student["score"] >= 90:
    #    print("A")
    #elif student["score"] >= 80:
    #    print("B")
    #else:
    #    print("Fail")
    print("")

print("==============================")