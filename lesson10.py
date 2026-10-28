print("Numbers with break: ")

for number in range(1, 11):
    if number == 10:
        break
    print(number)

print("")

print("Numbers with continue: ")
for num in range(1, 11):
    if num == 5:
        continue
    print(num)
    