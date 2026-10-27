#age = 34
#num = 45

#age = int(age)
#text = str(num)

#print(age)
#print(type(age))
#print(text)
#print(type(text))

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
student = bool(input("Are you a student? "))

print("------ STUDENT INFORMATION ------")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Student? {student}")

print(type(name))
print(type(age))
print(type(height))
print(type(student))