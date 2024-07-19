import random

def random_code():
    var = ''
    for item in range(0 , 6):
        code = random.choice(range(0 , 10))
        var += str(code)
    return var