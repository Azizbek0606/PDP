# dict

# arr = [1,34,56,78,98,65,43,21]
# print(12 if 12 in arr else "qiymat topilmadi")
# txt = ""
# num = 12
# float_num = 1.3
# set_data = {"azizbek", "kmdr", 12}
# dictionart = {
#     "key": "value",
#     "arr": [1, 2, 3, 5],
#     "number": 12,
#     "txt": "text",
#     "first_dict": {
#         "name": "MuhammadAmin",
#         "surname": "Boymuhammedov",
#         "age": [12, 34, 65, 17, 18, 20],
#     },
#     "new_dict": {"massiv": [1, 2, 3]},
# }
# print(dictionart.values())
# for i in dictionart.values():
#     print(i)
# x = dictionart["first_dict"]["surname"]
# print(x)
# print(dictionart)
# dictionart.clear()
# print(dictionart)
# dictionart.update({"name": "azizbek"})
# print(dictionart)
# dictionart["name"] = "Dilshod"
# print(dictionart)
# dictionart.pop("name")
# print(dictionart)

# x = ("key1", "key2", "key3")
# y = 0
# thisdict = dict.fromkeys(x, y)
# print(thisdict)

# print(dictionart.get("arr"))

# for i in range(10):
#     print(i)

# print(dictionart)
# dictionart.popitem()
# print(dictionart)


# from faker import Faker
# import random

# name = Faker()
# print(name.name())

# print(random.randint(1, 50))

# new_dict = {}
# for i in range(20):
#     new_dict.update({i:i})
# print(new_dict)
from faker import Faker
name = Faker()
print(name.name())