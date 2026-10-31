def student_info(name, *subjects, **details):
    print(f"Name: {name}")
    print("")


    print("Subjects:")
    for subject in subjects:
        print(subject)
    print("")

    print("Other Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(
    "Ryan",
    "Python",
    "Flutter",
    "Dart",
    age = 20,
    country = "Cameroon"
)