student = {
    "name": "Ryan",
    "age": 20,
    "email": "ryan@example.com",
    "country": "Cameroon",
    "level": "Degree"
}

student["course"] = "Computer Software Engineering"

for key, value in student.items():
    print(f"{key}: {value}")