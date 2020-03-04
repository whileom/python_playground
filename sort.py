products = [
    ("Product1", 20),
    ("Product2", 30),
    ("Product3", 10),
]

# case asc
products.sort(key=lambda product: product[1])

# case desc
products.sort(key=lambda product: product[1], reverse=True)

