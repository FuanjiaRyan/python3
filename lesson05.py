name = input("Enter Name: ")
age = int(input("Enter age: "))
score = int(input("Enter Score: "))
certificate = input("Certificate? ").lower() == "yes"

if age >= 16 and score >= 50 and certificate:
    print(f"Congratulations {name}!")
    print("You are eligible for admission")
else:
    print(f"Sorry {name}.")
    print("You are not eligible for admission")