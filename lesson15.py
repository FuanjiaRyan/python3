def create_profile(name, age, country="Cameroon"):
    print("===== PROFILE =====")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Country: {country}")
    print("===================")

    return

pro1 = create_profile("Ryan", 20, "Nigeria")
pro2 = create_profile("Ryan", 20)

print(pro1)
print("")
print(pro2)