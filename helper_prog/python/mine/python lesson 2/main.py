# x = 0
# del x
# print(x)
# operatorlat
# print(10 / 5) 2.0
# print(10 // 5) 2 

# s = "python"
# print("on" in s )
# print("js" in s )
# print("java" not in s )

# print(10 == 100) True
# print(10 == 10) True
# print(10 != 10) False
# print(10 != 10.0 ) False

# x = y = [1,2] 
# print(x is y) 
# y = [1.2 , 514]
# x = y
# print(x is y) True

# a = "a"
# b = "b"
# print(a is b) False

# a = "a"
# b = "b"
# print(a is not b) True
 
# if 1 > 0:
#     print("if")
# elif 1 > 0:
#     print("elif")
# else:
#     print("else")

# user = input("text:")

# if user.isalpha():
#     if "olma" == user:
#         print('true')
#     else:
#         print("false")
# else:
#     print("matn kiritning")

# task 1

# a = 2
# print(a * 4)


# task 2

# s = 2
# print(s ** 2)

# task 3

# a = 2
# s = 4
# print("tomoni:" , a * s)
# print("yuzasi:" , 2 * (a * s))

# task 4 

# d = 3
# p = 3.14
# print("doira yuzasi: " , p * d)

# task 5

# a = 4
# print("hajmi: ", a ** 3)
# print("to'la sirti: ", 6 * (a * 6))

# task 6

# a = 4 
# b = 6
# c = 5
# print("hajmi: ", a * b * c)
# print("to'la sirti: ", 2 * (a * b + b * c + a * c))

# task 7

# r = 5
# print("uzunligi: ", 2 * 3.14 * r)
# print("to'la sirti: ", 3.14 * (r ** 2))

# task 8

# a = 5 
# b = 6
# print("o'rta arfimetigi: " , (a + b) / 2)

# task 9

# a = 4
# b = 6
# print("o'rta gio'metrigi: ", (a + b) ** 0.5)

# task 10

# a = 3 
# b = 5

# if a > 0 and b > 0:
#     print("yigindisi: ", a + b)
#     print("kopaytmasi: ", a * b)
#     print("darajasi: ", a ** 2)
#     print("darajasi: ", b ** 2)
# else:
#     print("0 dan katta son kiriting")    


# task 12

# a = 12
# b = 15
# c = ((a ** 2) + (b ** 2) )** 0.5
# print("c= ",((a ** 2) + (b ** 2) )** 0.5)
# print("p= ", a + b + c)

# task 13

# task 1.1

# s = 6
# s1 = 6
# if s % 2 != 0 and s1 % 2 != 0:
#     print("yig'indisi: ", s + s) 
# elif s % 2 == 0:
#     print("ko'paytmasi: ", s * s1)
# else:
#     print(0)

# task 1.2


# one = 64 
# two = 37
# three = 20

# if one > two and one > three:
#     print(one)
# elif two > one and two > three:
#     print(two)
# else:
#     print(three)

# task 1.3

# first_user = "xabibullayev "
# second_user = "xabibullayeva "
# third_user = "xabibullayev "
# women = 0
# man = 0
# if first_user.endswith("v "):
#     man += 1
# else:
#     women += 1
# if second_user.endswith("v "):
#     man += 1
# else:
#     women += 1
# if third_user.endswith("v "):
#     man += 1
# else:
#     women += 1
# print("erkak: ", man)
# print("ayol: ", women)

# lesson 3 
# Ternarni operator
# x = 3
# print("yes") if x > 5 else print("no")
# x = 5
# print("yes" if x >= 5 else "no")

# for i in "python":
#     print(i)

# for i in range(1 , 5 +1):
#     print(i ,"son")

# print(type(range(1 , 8)))
# print(dir(range(1 , 8)))

# start = 1
# step = 3
# stop = 15
# for i in range(start , stop , step):
#     print(i)
# print(list(range(start , stop , step)))
# for k in "python python python":
#     if k == "y":
#         print(k)

# def main(num):
#     return num ** num
# for x in range(1, 10):
#     print(main(x))
# s = "Python is n1"

# for i in enumerate(s):
#     print(i)

# enemrate element va uni indexni ham qaytaradi 

# for i in range(5):
#     if i % 2 == 0:
#         print(i)
# else: 
#     print("loop tugadi")

# passWord = "qwertyui"
# while True:
#     user = input("parolni kiriting")
#     if user == passWord:
#         print("Xush kelibsiz")
#         break
#     else:
#         print("qayta urinib ko'ring")        
# i = 0
# while True:
#     i += 1
#     if i == 150:
#         print("true")
#         break
#     elif i % 2 == 0:
#         continue
#     print(i)

# num = 0

# while True:
#     user = input("son kiriting")
#     if user.isdigit():
#         user_num = int(user)
#         num += user_num
#     if user == "stop":
#         print(num)
#         break

# alpha = "abcdifghijklmonpqrstuvwxyz"
# inp = input("text...")
# for latter in enumerate(alpha):
#     if inp == latter[1]:
#         print(latter[0] + 1)
# output = 0
# condition = True
# while condition:
#     user_nam = input("son...")
#     if len(user_nam) == 2 and user_nam % 10 == 0:
#         output += int(user_nam)
#     if user_nam == "stop":
#         condition = False
# print(output)


# lesson 4

# print(int("1.2")) xato

# print(float("1.2")) type = int

# bin 

# print(bin(10)) 0b1010

# print(oct(10)) 0o12

# print(hex(10)) 0xa

# print(round(12.5)) # 12
# print(round(12.7)) # 13 round ichki funksiya 

# print(abs(-24)) # 24

# print(pow(2 , 2)) #4

# print(min([1 , 2 , 3])) # 3 
# print(max([1 , 2 , 3])) # 1
# print(sum([1 , 2 , 3])) # 6
# arr = [1 , 2 , 3]
# print(min(arr))
# print(max(arr))

# n = 10.0 
# n1 = 10.3
# print(n.is_integer())# float qiymatni butun son qilsa bolishini yoki bolmasligini chiqaradi
# print(n1.is_integer())# float qiymatni butun son qilsa bolishini yoki bolmasligini chiqaradi

# import math 
# print(math.pi) #3.141592653589793

# from math import pi

# print(pi) #3.141592653589793

# import math

# print(math.ceil(12.4)) # 13
# print(round(12.4)) # 12
# print(math.floor(12.7)) # 12

# import random

# print(round(random.random())) # 0 va kiritilgan son orasidagi son 

# print(random.randint(1 , 50)) # ikkita son orasidagi tasodifiy son 

# import random

# print(random.choice("python")) # ketma ketlikdan bitta tasodify lelementlarni qaytaradi 
# print(random.sample("python" , 2)) # ketma ketlikdan tasodifiy bir nechta elementlarni qaytaradi 
# arr = [1 , 2 , 3 , 4 , 5 ]
# random.shuffle(arr)
# print(arr)

# import random

# input_num = int(input("1-sonni kiriting: "))
# input_len_pass = int(input("2-sonni kiriting: "))

# lowerText = 'qwertyuiopasdfghjklzxcvbnm'
# upperText = lowerText.upper()
# numbers = '123456789'
# simbols = '/-=+*_'
# user_pass = lowerText + upperText + numbers + simbols

# if input_len_pass >= 6 :
#     for i in range(input_num):
#         password = "".join(random.sample(user_pass , input_len_pass))
#         print(password)
# else:
#     print("ikkinchi son 6 dan kichik ")

# str_uz = "yangi o'zbekiston"
# str_key = "svet"
# counter = 0
# for i in str_uz:
#     for k in str_key:
#         if i == k:
#             counter += 1
# print(counter)

# print(len("".join([x for i in "svet" for x in "yangi o'zbekiston" if i == x])))

# import random
# counter = 0
# user_num = int(input("son kiriting: "))
# for i in range(1 , 101):
#     random_num = random.randint(1 , 100)
#     if  user_num == random_num:
#         counter += 1
#     print(random_num)
# print(counter)

# first_num = int(input("birinchi son "))
# secon_num = int(input("ikinchi son "))
# for i in range(first_num , secon_num):
#     print(i)


# first_num = int(input("birinchi son "))
# secon_num = int(input("ikinchi son "))
# counter = 0
# second_counter = 0
# for i in range(first_num , secon_num):
#     print(i)
#     counter += i
#     second_counter += i ** 2
    
# print("sonlar yig'indisi {}".format(counter))
# print("sonlar kvadrati {}".format(second_counter))

# lesson 5
# String Methods

# s = "bu 'qora' olma"
# s = 'bu "qora" olma'
# print(s)



# s = "bu qora olma"
# print(s[len(s) - 1])
# print(s[-1])
# print(s[2:5])
# print(s[:5])
# print(s[2:])
# print(s[:])

# str_book = "kitob"
# print(str_book[:-1])

# age = 30
# name = "John Doe"
# PYTHO V2
# user = "name = %s ,age = %s" %(name , age)
# print(user)
# user = "name = {} ,age = {}".format(name , age)
# print(user)

# # PYTHON V3
# user = f"name = {name} , age = {age}"
# print(user)

# s = "pyhon string methods"
# print(s.center(50))
# s = " salom hayr qale "
# print(len(s))
# print(len(s.strip())) ikkala tarafdagi probellarni o'chiradi
# print(len(s.lstrip())) chapdagi probelni o'chiradi
# print(len(s.rstrip())) o'ngdagi probelni o'chiradi 

# s = "salom,hayr,qale"
# print(s.split(",")) ['salom', 'hayr', 'qale']
# print(s.rsplit(","))

# s = """lorem 0100 0 011  1100100 1 00000 1  001 1 00000  00 1101 0101100 1
#  011 1 101 00 1 0 1 0 0 0   1010000 01 00 1   01  110011 110 1010
#   11111 11 110  0 0  1111\n   010 1 00101 11 000 00 10110001 01
#  1  0 11 0  101 0  11 1  010   10101001 1 0000001 1 1 1000 00001
# 0  10 111 11101 1 00 001 011\n0  1 101  1 111100 101  1100010
# 0     11101001110  1 100001   11011   10 10011 110 10100  111"""
# print(len(s.splitlines()))
# print(s.splitlines())

# s = "hohla ishla  ishlama"
# print(s.split("h"))
# print("".join(s.split("h")))
# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.swapcase())
# print(s.title())
# print(s.find("ishla"))
# print(s.index("ishla"))
# print(s.rfind("ishla"))
# print("on table non table".count("on"))
# print("aloha chicas".replace("chicas" , "muchachos"))
# print("gandi".startswith("gand"))
# print("gandi".endswith("di"))

# user_text = input("matn kiriting:\n").lower().split(' ')
# fire = 0
# ener = 0
# no = 0
# fireList = ""
# enerList = ""
# noList = ""
# for i in user_text:
#     if i.startswith("gaz"):
#         fire += 1
#         fireList += i
#     if i.startswith("svet"):
#         ener += 1
#         enerList += i
#     if i.startswith("yo'q") or i.startswith("yo`q"):
#         no += 1
#         noList += i
# print(fire , ener , no)
# print(fireList ,"\n", enerList ,"\n" , noList)

# lesson 6

# print("11ss".isalnum())
# print("abc".isalpha())
# print("1500".isdigit())
# print("Az".isupper())
# print("Az".lower())
# print("Az".title())

# password:
#     minimum 6ta belgi,
#     kamida 1ta katta harf ,
#     kamida bitta maxsus belgi(\/@_-),
#     kamida bitta butun son

# task 1

# pasword = input("your password\n")

# upper_latter = False
# digit = False
# symbol = False

# if len(pasword):
#     for latter in pasword:
#         if latter.isdigit():
#             digit = True
#         if latter.isupper():
#             upper_latter = True
#         if latter in "\\/@-_":
#             symbol = True
#     if upper_latter and digit and symbol:
#         print("Pasword true ")
# else:
#     print("password wrong!")



# l = list("str") faqat bitta qiymat qabul qiladi 

# l = [1 , 2 , 3 , [1 , 2 , 3] , "number"]
# print(l[0])
# print(len(l))
# append - oxiriga qo'shish
# pop - oxiridan o'chirish
# index - ko'rsatilgan element indexsini olish
# insert - index orqali element qo'shish
# reverse - listni teskari qilish
# count - elementlar sonini hisoblash
# sort - saralash
# remove - element o'chirish
# extend - boshqa massiv bilan listni kengaytirish
# copy - list nusqasini olish
# del l[index] - element o'chirish
# clear - listni tozalsh


# x , y , *z = [1 , 2 , 3 , 4 , 5 , 6]
# print(x , y , z)
# print(type(z))

# def chask_user(*args):
#     for i in args:
#         print(i)
        
# chask_user("nbvfnv" , 17 , True , "dsedsjerjer")


# arr = [1,2,3,4,5]
# print(arr[:])
# print(arr[3:])
# print(arr[2:3])
# arr.reverse()
# print(arr)

# arr = [[1,2,3,] ,[4,5,6],[7,8,9]]

# for i in arr:
#     for k in i:
#         print(k)


# arr = input("text\n")
# print( f"{arr[-1]}{arr[1:-1]}{arr[0]}")
# arr = [1,2,3,4,5]
# # l = [i**2 for i in arr]
# # print(l)
# l = [i**2 for i in arr if i % 2 == 0]
# print(l)

# arr = [[1,2] , [3,4] , [5,6]]
# new_arr = [j * 10 for i in arr for j in i if j % 2 == 0]
# print(new_arr) #[20, 40, 60]

# user = "qwertyuioplkjhgfsasdsasadsasdsssasdsajhgyugyuayuasauauaAAHAA "
# l = [latter for latter in user if latter in "aA"]
# print(l)

# l = ["olma" , "behi" , "nok" , "kivi"]
# k = ["ning" , "ni" , "ga" , "da" , "dan"]
# print(list(zip(l , k)))


# alpha = "abcdifg"
# print(list(zip(alpha , list(range(len(alpha))))))

# l = "aaaa"
# arr = [1,2,3,4,5,6,7,8,9]
# print(list(zip(l , arr))) #[('a', 1), ('a', 2), ('a', 3), ('a', 4)]


# def odd(n):
#     if n % 2 == 1:
#         return n
    
# arr = list(range(1,11))
# print(list(filter(odd , arr)))

# task 4

# first_l , last_l , helper = [1,2,3,4,5] , [7,5,4,9,1,9] , []
# [helper.append(i) for i in first_l for k in last_l if i == k]
# for j in helper:
#     first_l.remove(j)
#     last_l.remove(j)
# print(first_l , last_l)

# lesson 7

# from functools import reduce

# arr = list(range(6))
# def func(x , y):
#     print(f"x={x}\ny={y}")
#     return(x + y)
# r = reduce(func , arr)
# print(r)
# a1 = [1,2,3]
# b1 = [4,5,6]
# a1.extend(b1)
# print(a1)

# arr = [1 , 2]
# arr.insert(4,4)
# print(arr)
# print(len(arr))
# arr[:0] = [-1 , -2 , 0]
# print(arr)
# del arr[:2]
# print(arr)
# print(2 in arr)
# print(6 in arr)
# print(6 not in arr)
# import random
# arr = [random.randint(1 , 50) for i in range(10)]
# arr.sort()
# print(arr)
# arr.sort(reverse=True)
# print(arr)
# print(sorted(arr , reverse=True))
# print(sorted(arr))
# for i in sorted(arr):
    # print(i)
# print(sorted("AqwsxedcYHN" , key=str.upper))
# print(sorted("AqwsxedcYHN" , key=str.upper , reverse=True))
# arr = list(range(10 , 100 , 10))
# print(arr)
# arr = random.sample(range(100) , 10)
# print(arr)

# t = tuple() qiymatini o'zgartirib bo'lmaydi
# t = ()
# arr = [1,2,3]
# del arr[1]
# print(arr)
# t = (1,2,3)
# del t[1]

# supported methods min max count index [:] len
# t = (1,2,3)
# s = set()
# s = {}
# unikal tartibsiz elementlar to'plami 
# print(set("assalom"))

# fs = frozenset("assalom")
# print(fs)

# d = dict(name = "John Doe",age = 30)
# print(d)
# d = {
#     "name":"John",
#     "surname":"Doe",
#     "age": 17
# }
# print(d)
# print(d["name"])
# print(d.get("lanstname")) getning qulayligi element kaliti topilmasa none qiymat qaytaradi va kod ishlashda davom etadi

# k = ["monkey ", "elephent"]
# v = [12,5]
# print(dict(zip(k,v)))


# import random
# from faker import Faker

# fake = Faker()

# users = {}

# for i in range(10):
#     name = fake.name()
#     temp = {
#         f'{name.split(" ")[0].lower()}':random.randint(15 , 30)
#     }
#     users.update(temp)
# print(users)
# import random
# arr = []
# for i in range(5):
#     arr.append(random.randint(10 , 35))
# print(arr)
# l = list(random.sample(range(10 , 35),5))
# print(l)

# arr = [True , 1 , 1.3 , 3.3 , "str" , "qale"]
# bools = []
# ints = []
# floats = []
# strs = []
# for i in arr:
#     if type(i) == bool:
#         bools.append(i)
#     elif type(i) == float:
#         floats.append(i)
#     elif type(i) == str:
#         strs.append(i)
#     elif type(i) == int:
#         ints.append(i)
# print(f'bool={bools}\nint={ints}\nfloat={floats}\nstr={strs}')

# user_input = 21

# etaj = 0
# padyezd = 1

# for i in range(user_input):
#     if i % 6 == 0:
#         etaj += 1
#     if etaj > 7:
#         etaj -= 7
#         padyezd +=1
        
# print(f'etaj={etaj}\npadyezd={padyezd}')

# lesson 8

# d = {}
# d["name"] = "john"
# print(d)

# d = {}
# d["name"]="john"
# print(d.setdefault("age" , 20))
# print(d.get("name"))
# print(len(d))
# del d["name"]
# print(d)
# print(len(d))

# d = {}
# d["name"]="john"
# d["age"] = 17
# d["age"] = 1
# d["age"] = 5

# for i in d.keys(): faqat kalitlarni olish 
#     print(i)
# for k in d.values(): faqat qiymatlarini olish
#     print(k)
# for item in d.items(): barcha elemenlarini olis 
#     print(item)

# d.pop("name") ko'rsatilgan kalt ostidagi elementni ochirish
# print(d)

# print(d.popitem())

# d.clear()
# print(d)
# d.update({"salary": 30})
# print(d)

# keys = "abc"
# values = [1,2,3]
# d = {k: v for (k , v) in zip(keys , values)}
# print(d)

# keys = "abc"
# values = [1,2,3]
# d = {}
# for i in keys:
#     for k in values:
#         d.update({i:k})
# print(d)

# task 1

# from faker import Faker

# fake = Faker()

# users = {}
# for i in range(30):
#     user = fake.name().split()
#     if user[0].lower().count("a") >= 2:
#         users.update({user[0].lower():fake.address()})
# print(users)


# arr = []
# while True:
#     user = input("sana kiriting")
#     if len(user) == 10:
#         arr = user.split(".")
#     else:
#         print("kam son kiritdingiz ")
    
#     break

# for i in arr:
#     if int(arr[0]) <= 12 and int(arr[1]) <= 31 and int(arr[2]) >= 1970 and int(arr[2]) <=2023:
#         print(True)
#         break
#     else:
#         print(False)
#         break

# user = int(input("son\n"))
# counter = user
# for i in range(9):
#     if counter == 24:
#         counter = 0
#     counter +=1
# print(f"uxlsh vaqti {user}:00 uyg'onish vaqti {counter}:00")

#lesson 9
# import time
# import locale
# locale.setlocale(locale.LC_ALL, "Uz_uz")
# import datetime
# import calendar

# Time
# print(time.time())
# now = datetime.datetime.now()
# print(now) 2023-01-30 16:21:03.486438

# print(now.day)
# print(now.month)
# print(now.year)

# ago = int(input("nechanchi yilsiz?\n"))
# print(now.year - ago)
# print(time.strftime("%d/%m/%y"))
# print(time.strftime("%d/%b/%Y"))
# print(time.strftime("%D"))
# print(time.strftime("%a"))
# print(time.strftime("%A"))
# print(time.strftime("%y"))
# print(time.strftime("%Y"))
# print(time.strftime("%m"))
# print(time.strftime("%m"))
# print(time.strftime("%b"))
# print(time.strftime("%B"))
# print(time.strftime("%w")) # hafta ichida qaysi kunligi chiqadi
# print(time.strftime("%W")) # yilda haftaning tartib raqami qaytadi

# print(time.strftime("%H"))
# print(time.strftime("%M"))
# print(time.strftime("%S"))
# print(time.strftime("%I"))
# print(time.strftime("%x"))
# joriy sanani qaytaradi
# print(time.strftime("%X"))
# joriy vaqatni qaytaradi 
# print(time.strftime("%Y/%m/%d/%H:%M:%S"))
# print(time.strftime("%x%X"))
# time.sleep(10)
# print("10s tugadi")
# for i in range(10):
#     time.sleep(1)
#     print(i)

# today = datetime.date.today()
# print(today)
# start_date = datetime.date.today()
# end_date = start_date + datetime.timedelta(days=7)
# print(end_date)
# print(start_date == end_date)

# start_time = datetime.timedelta(hours=1 ,minutes=30,seconds=30)
# end_time = start_time + datetime.timedelta(minutes=1)
# c = calendar.LocaleHTMLCalendar
# print(c.formatyear(datetime.date.today().year))

# from timeit import Timer


# code = """\
# i = 1
# while i < 10 ** 5:
#     i = i + 1
# """
# t = Timer(stmt=code)
# print("While : \n",t.timeit(number=1000))

# homework 


# task 7 

# 12 ta ishchi ism familyasini Faker orqali hosil qiling
# har bir ishchi 12 oy davomida (1 yil) har bir oyda ma'lum bir miqdorda oylik maosh olgan
# oylik maoshlar stabil oylik maosh summasidan ishchini ishlashiga qarab ayrim oylarda +5% ko'proq , ayrim oylarda -5% kamroq bo'lishi mumkin. Siz ushbu malumotlardan foydalanib hisoblashingiz kerak. 
# 1-Har bir ishchini 12 oyda olgan umumiy ish haqi summasi 
# 2- Har bir ishchini kvartallar boyicha ish haqlarini 
# 3- yil davomida eng ko'p maosh olgan ishchini 
# 4- yil davomida eng kam moash olgan ishchini 
# 5- eng kop maosh olgan ishchini eng kam olgan  bilan oyliklari o'rtasidagi farqni

# import random
# from faker import Faker

# fake = Faker()

# worker = []
# monthly = [[],[],[],[],[],[],[],[],[],[],[],[],]
# index_arr = -1
# worker_list = {}
# for k in range(156):
#     if k == 12 or k == 24 or k == 36 or k == 48 or k == 60 or k == 72 or k == 84 or k == 96 or k == 108 or k == 120 or k == 132 or k == 144 or k == 156 :
#         index_arr += 1
#         for x in range(12):
#             worker.append(fake.name())
#             random_monthliy = random.randint(1000 , 7000)
#             random_multiplier = random.randint(0,1)
#             if random_multiplier == 0:
#                 random_monthliy - (random_monthliy * 0.05)
#                 random_monthliy + (random_monthliy * 0.05)
#             monthly[index_arr].append(random_monthliy)
#             worker_list.update({worker[x]:sum(monthly[x])})
            
# first_index = -1
# second_index = 0
# third_index = -3
# kvart = []
# for i in range(52):
#     if i == 4 or i == 8 or i == 12 or i == 16 or i == 20 or i == 24 or i == 28 or i == 32 or i == 36 or i == 40 or i == 44 or i == 48:
#         first_index = first_index + 1
#         for a in range(4):
#             second_index = second_index + 3
#             third_index = third_index + 3
#             if second_index == 15:
#                 second_index = 3
#             if third_index == 12:
#                 third_index = 0
#             kvart.append(sum(monthly[first_index][third_index:second_index]))
# index = -4
# index1 = 0
# worker_kvart = {}
# arr = []
# for i in range(52):
#     if i == 4 or i == 8 or i == 12 or i == 16 or i == 20 or i == 24 or i == 28 or i == 32 or i == 36 or i == 40 or i == 44 or i == 48:
#         index += 4
#         index1 += 4
#         arr.append(kvart[index:index1])
# for i in range(12):
#     worker_kvart.update({worker[i]:arr[i]})
# arrMax = []
# for i,k in worker_kvart.items():
#     arrMax.append(sum(k))
# minVal = min(arrMax)
# maxVal = max(arrMax)
# top , bottom = [] , []
# for key,value in worker_kvart.items():
#     if maxVal == sum(value):
#         top.append((key,sum(value)))
#     if minVal == sum(value):
#         bottom.append((key,sum(value)))
# for i,k in worker_list.items():
#     print(f"{i}ning umumiy daromadi: {k}\n")
# for i,k in worker_kvart.items():
#     print(f"{i}ning har bir kvartaldagi daromadi{k}\n")
# print(f"\n\neng ko'p oylik oluvchi: {top}")
# print(f"\n\neng kam oylik oluvhi: {bottom}")
# print(f"\n\neng ko'p oylik oluvchi eng kam oylik oluvchidan {maxVal - minVal} ko'p oylik oladi")



# import random
# from faker import Faker

# fake = Faker()

# worker = []
# monthly = [[],[],[],[],[],[],[],[],[],[],[],[],]
# index_arr = -1
# worker_list = {}
# for k in range(156):
#     if k == 12 or k == 24 or k == 36 or k == 48 or k == 60 or k == 72 or k == 84 or k == 96 or k == 108 or k == 120 or k == 132 or k == 144 or k == 156 :
#         index_arr += 1
#         for x in range(12):
#             worker.append(fake.name())
#             random_monthliy = random.randint(1000 , 7000)
#             random_multiplier = random.randint(0,1)
#             if random_multiplier == 0:
#                 random_monthliy - (random_monthliy * 0.05)
#                 random_monthliy + (random_monthliy * 0.05)
#             monthly[index_arr].append(random_monthliy)
#             worker_list.update({worker[x]:sum(monthly[x])})
            
# first_index = -1
# second_index = 0
# third_index = -3
# kvart = []
# for i in range(52):
#     if i == 4 or i == 8 or i == 12 or i == 16 or i == 20 or i == 24 or i == 28 or i == 32 or i == 36 or i == 40 or i == 44 or i == 48:
#         first_index = first_index + 1
#         for a in range(4):
#             second_index = second_index + 3
#             third_index = third_index + 3
#             if second_index == 15:
#                 second_index = 3
#             if third_index == 12:
#                 third_index = 0
#             kvart.append(sum(monthly[first_index][third_index:second_index]))
# index = -4
# index1 = 0
# worker_kvart = {}
# arr = []
# for i in range(52):
#     if i == 4 or i == 8 or i == 12 or i == 16 or i == 20 or i == 24 or i == 28 or i == 32 or i == 36 or i == 40 or i == 44 or i == 48:
#         index += 4
#         index1 += 4
#         arr.append(kvart[index:index1])
# for i in range(12):
#     worker_kvart.update({worker[i]:arr[i]})
# arrMax = []
# for i,k in worker_kvart.items():
#     arrMax.append(sum(k))
# minVal = min(arrMax)
# maxVal = max(arrMax)
# top , bottom = [] , []
# for key,value in worker_kvart.items():
#     if maxVal == sum(value):
#         top.append((key,sum(value)))
#     if minVal == sum(value):
#         bottom.append((key,sum(value)))
# for i,k in worker_list.items():
#     print(f"{i}ning umumiy daromadi: {k}\n")
# for i,k in worker_kvart.items():
#     print(f"{i}ning har bir kvartaldagi daromadi{k}\n")
# print(f"\n\neng ko'p oylik oluvchi: {top}")
# print(f"\n\neng kam oylik oluvhi: {bottom}")
# print(f"\n\neng ko'p oylik oluvchi eng kam oylik oluvchidan {maxVal - minVal} ko'p oylik oladi")



# lesson 10 functions


# def func_name(argument):
    # function block
    # return natija qaytaradi
    
# def main(x):
#     pass # hech  qanday amal yo'q daegani
# class Main:
#     pass

# for i in range(12):
#     pass

# def func():
#     print("func")
#     return "func 1"
# print(func())

# def chask_user(username): # postional argument muhim bo'lgan argument
#     print(username)
# chask_user()
# def chack_user(username="gandi"): #not postional argument
#     print(username)
    
# chack_user()

# def user_date(name,age,salary,addres):
#     date = [name,age,salary,addres]
#     for item in date:
#         print(item)
# def user_date(*args):
#     for a in args:
#         print(a)

# *args - agruments
# **kwargs

# def func_kwargs(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
    
# func_kwargs(name="john" , age=30)

# def super_func(*args, **kwargs):
#     for i in args:
#         print(i)
#     for i in kwargs:
#         print(i)

# super_func( name="john" , age=30 )


# def plus(*args , **kwargs):
#     counter = 0
#     for i in args:
#         counter += i
#     for i , v in kwargs.items():
#         counter += v
#     return round(counter)
# print(plus(1,2,3,4.5,9,5.6,6.4 , name=1.2 , age=7.9))

# main = lambda x : x + 10
# print(main(10))

# arr = [1,5,9,3654,78,25,12,9,539,29.9,30,31,35,36,38,37,35]
# a = list(filter(lambda x : x > 30 , arr))
# print(a)

# res = lambda x , y , z : x + y + z
# print(res(1,2,3))

# def func(x,y):
#     for i in range(1,x+1):
#         yield i ** y
# # print(func(5,2)) # generator object
# print(list(func(5,2))) # [1, 4, 9, 16, 25]

# def bechmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'vremya vipoleniya: {round(end-start , 2)} sekund')
#     return wrapper
# @bechmark
# def fetch_webpages():
#     import requests
#     weppage = requests.get("https://google.com")
# fetch_webpages()

# from benchmark import bechmark
# @bechmark
# def count_zeros(num):
#     counter = 0
#     for i in range(1 , num):
#         if i % 10 == 0:
#             print(i)
#     return counter
# count_zeros(1000)

# lesson 11 global o'zgaruvchilar

# print(x) name error
# x = 10
# g_var = "global var"

# def main(num):
#     print(g_var)
#     # local varible
#     x = 10
#     print(x)
# print(x)NameError

# def main(num):
#     print(num)
# global varible
#     global x 
#     x = 10
#     print(x)
# print(main(4))
# print(x)

# funncsiay ichida funksiya

# def outer(string):
#     def inner(s):
#         return s.split(",")
#     return inner(string)
# print(outer("python , java , javascript , cpp"))


# def func(a:int , b:int) ->int:
#     return a + b
# print(func(1,2))

# def func(a:int , b:int) ->int:
#     return a + b
# print(func.__annotations__) #{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

# def func(a:5 , b:5 , c:)

# import os
# print(os.path)
# import benchmark
# benchmark.func(125)

# from benchmark import func 
# print(func("aas"))

# from auth_modules.login import info
# print(info)

# import sys
# print(sys.path)
