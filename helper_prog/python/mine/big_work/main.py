import fake_name
import random_number


def create_fake_workers():
    salary_arr = [random_number.for_salary() for _ in range(12)]
    salary = {"salary": salary_arr}
    email = {"email": fake_name.get_random_email()}

    age = {"age": random_number.until_50()}
    experience_num = random_number.for_experience(age["age"])
    experience = {"experience": experience_num}

    worker = {**salary, **email, **age, **experience}
    return worker


def worker():
    worker_list = {}
    for i in range(4):
        worker_name = fake_name.get_random_name()
        worker_list.update({worker_name: create_fake_workers()})
    return worker_list

def works(work_name):
    work_list = {}
    company = {}
    for i in work_name:
        work_list.update({i: worker()})
    company.update(work_list)
    return company
