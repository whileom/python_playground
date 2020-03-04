products = [
    ("Product1", 20),
    ("Product2", 30),
    ("Product3", 10),
]

_products = map(lambda product: product[1], products)
print(_products)
# map return map object 

# convert list
_products = list(map(lambda product: product[1], products))
print(_products)
