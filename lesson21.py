courses = {"Python", "Flutter", "Dart", "Python", "Java"}

print(type(courses))
print(courses)
print(len(courses))

courses.add("Cybersecurity")
print(courses)

courses.remove("Dart")
print(courses)

for course in courses:
    print(course)

courses.add("Java Script")
print(courses)

courses.remove("Java")
print(courses)