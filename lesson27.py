numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers}")

squares = [number ** 2 for number in numbers]
print(f"Squares: {squares}")

even_numbers = [number for number in numbers if number % 2 == 0]
print(f"Even numbers: {even_numbers}")