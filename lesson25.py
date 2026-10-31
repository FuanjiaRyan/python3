def create_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

create_profile(
    name = "Ryan",
    age = 20,
    course = "Software",
    country = "Cameroon"
)