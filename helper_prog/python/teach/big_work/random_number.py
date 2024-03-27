import random

def get_randomnumber():
    return random.randint(1, 100)

def until_50():
    while True:
        random_num = get_randomnumber()
        if random_num <= 50:
            return random_num
            break
