student = {
    "name": "Ryan",
    "age": 20,
    "email": "ryan@example.com",
    "country": "Cameroon",
    "level": "HND"
}

print(student["name"])
print(student["email"])
student["level"] = "Degree"
print(student["level"])
student["phone"] = "679751591"
print(student["phone"])
print(student)

if "email" in student:
    print("email exists")
else:
    print("email not available")