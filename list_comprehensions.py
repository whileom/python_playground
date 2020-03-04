products = [
    ("Product1", 20),
    ("Product2", 30),
    ("Product3", 10),
]

# Method Map
# mapped = list(map(lambda product: product[1], products))
mapped = [product[1] for product in products]
print(mapped)

# Method Filter
# filtered = list(filter(lambda product: product[1] >= 20, products))
filtered = [product for product in products if product[1] >= 20]
print(filtered)