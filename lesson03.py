name = input("Enter student name: ")
math = int(input("Enter Math score: "))
english = int(input("Enter English score: "))
computer = int(input("Enter Computer score: "))

total = math + english + computer
average = total / 3

print("====================")
print("Student Grade")
print("====================")
print("")
print(f"Student: {name}")
print("")
print(f"Math: {math}")
print(f"English: {english}")
print(f"Computer: {computer}")
print("")
print(f"Total: {total}")
print(f"Average: {average:.2f}")

if average >= 10:
    print("Pass")
else:
    print("Fail")

print("====================")


