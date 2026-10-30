flutter_students = {"Ryan", "Peter", "John", "Mary"}
python_students = {"Ryan", "Mary", "David", "Grace"}

flutter_students.add("John Doe")
python_students.add("Francis")

#union
print("All students: ")
print(flutter_students.union(python_students))

#intersection
print("Students learning both: ")
print(flutter_students.intersection(python_students))

#Difference
print("flutter students only: ")
print(flutter_students.difference(python_students))