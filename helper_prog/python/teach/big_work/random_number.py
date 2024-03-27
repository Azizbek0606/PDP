import random

def get_randomnumber():
    return random.randint(1, 100)

def for_salary():
    return random.randint(1000, 5000)

def until_50():
    while True:
        random_num = get_randomnumber()
        if random_num <= 50 and random_num >= 18:
            return random_num
            break

def for_experience():
    return random.randint(3, 25)