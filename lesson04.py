name = input("Name: ")
score = int(input("Score: "))

print("====================")
print("GRADE CLASSIFICATION")
print("====================")
print("")
print(f"Student: {name}")
print(f"Score: {score}")

if score >=90:
    print("A+")
    print("Outstanding")
elif score >= 80:
    print("A")
    print("Excellent")
elif score >= 70:
    print("B")
    print("Very Good")
elif score >= 60:
    print("C")
    print("Good!")
elif score >= 50:
    print("D")
    print("Passed")
else:
    print("F")
    print("Failed")

print("")
print("====================")