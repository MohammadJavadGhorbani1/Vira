import random

def random_product(product_range , collection):
    for item in product_range:
        x = random.choice(collection)
    return x
