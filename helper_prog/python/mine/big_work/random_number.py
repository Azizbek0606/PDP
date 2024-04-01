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
        else:
            continue

def for_experience(age):
    if age >= 19 and age <= 25:
        return age - 18
    elif age >= 25 and age <= 35:
        return age - 20
    else:
        return age - 10
