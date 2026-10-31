def calculate_total(*prices):
    total = 0

    for price in prices:
        total += price

    return total

result = calculate_total(5000, 10000, 2500, 7500,3000)
print(f"Total: {result}")