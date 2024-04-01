import fake_name
import random_number

company = {}


# examples = {
#     "ishnomi":{
#         "ishchiismi"{
#             "yoshi":random_number,
#             "tajribasi":for_experience,
#             "email":"email@gmail.com",
#             "salary":[2000 x 12]
#         }
#     }
# }
def create_fake_workers():
    salary = {}
    salary_arr = []
    for i in range(12):
        salary_arr.append(random_number.for_salary())
    else:
        salary.update({"salary": salary_arr})
    email = {"email": fake_name.get_random_email()}
    experience = {}
    age = {}
    age.update({"age": random_number.until_50()})
    while True:
        experience_num = random_number.for_experience()
        if (age["age"] - experience_num) >= 18 and (age["age"] - experience_num) < 25:
            experience.update({"experience": experience_num})
            break
        else:
            continue
    result_dict = {}
    result_dict.update(age)
    result_dict.update(email)
    result_dict.update(experience)
    result_dict.update(salary)
    return result_dict

def worker():
    worker_list = {}
    for i in range(4):
        worker_name = fake_name.get_random_name()
        worker_list.update({worker_name: create_fake_workers()})
    return worker_list

def works(work_name):
    work_list = {}
    for i in work_name:
        work_list.update({i: worker()})
    return work_list

names_list = ["front end" , "back end" , "designer" , "project manger"]
company.update(works(names_list))
print(company)
