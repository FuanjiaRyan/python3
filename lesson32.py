prices = [1000, 2500, 5000, 7500, 10000]

increase = list(map(lambda price: price * 1.10, prices))

print(f"Original prices: {prices}")
print(f"New prices: {increase}")