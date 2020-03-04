products = [
    ("Product1", 20),
    ("Product2", 30),
    ("Product3", 10),
]

products_filtered = list(filter(lambda product: product[1] >= 20, products))
print(products_filtered)
