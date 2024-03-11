# data types
# str =========> "",  """""", qo'shtirnoq ichidagi har qanday belgi string turida bo'ladi
# int ========> 1,2,3,4,5 butun son qabul qiladi
# float ========> 1,2 , 2.3 , 2.7 qoldiqli son qabul qiladi
# bool ========> True , False , rost yoki yolg'on qo'lgan yani true yoki false qabul qiladi
# range ========> 1,4,7,8,76543 , asosan for uchun ishlatiladi va faqat butun son qabul qiladi
# list ========> [1,2,3,"text" , True , [1,2,3] , (1,2,3, "text")] har qanday turdagi qiymat qabul qiladi va tarqibli holda bo'ladi
# tuple ========> (1,2,3, "text" , ["array" , "1,2,3" , 1,2,3]) har qanday turdagi qiymat qabul qiladi va berilgan qiymatarni o'zgartirish va yangilash o'chirsa bo'lmydi
# set ========> {1,2,3} tartibsz holda joylashadi malumotlar yangi qiymat qabul qiladi ammo eski qiymatni o'chirish va tahrirlash imkonsiz
# frozenset ========> {1,2,3} set ichiga array qo'shish uchun ishlatiladi


# methods:
# str:
# count() , isalnum() , isalpha() , replace() , startswith() , endswith() , lower() , upper() , join() , isdigit() , capitalize() va hokazo


# list / array / massiv
# append() clear() copy() count() extend() index() insert() pop() remove() reverse() sort()
# txt = "azizbek xabibullayev 220 group pogramming language python"
# # count_a_txt = txt.count("x")
# # print(type(count_a_txt))
# # print(txt.split())
# # txt1 = txt.replace("azi" , "A21")
# arr = ["Asliddin", "Muhammadamin", "Muhammad Sodiq"]
# multiplay = "".join(arr)
# print(multiplay)
# for i in "ASLIDDIN":
#     print(i)

# txt = "yangi o'zbekiston"
# counter = 0
# for i in txt:
#     counter += 1
# print(counter)
# shaptoli = "12344567"
# print(shaptoli.isdigit())

# txt = "12345"
# num = ""
# for i in txt:
#     num += i
# print(num)

# txt_num="Kmdr123nmagap64jdfhsj"
# num = ""
# word = ""
# for i in txt_num:
#     if i.isalpha():
#         word += i
#     elif i.isdigit():
#         num += i
#     # elif i == " ":
#     #     prabel += 1
# print(word)
# print(num)

# txt_num="Kmdr 123 nma gap64 jdfhsj"
# num = ""
# word = ""
# prabel = 0
# for i in txt_num:
#     if i.isalpha():
#         word += i
#     elif i.isdigit():
#         num += i
#     # elif i == " ":
#     #     prabel += 1
#     else:
#         prabel +=1
# print(word)
# print(num)
# print(prabel)
# txt = "a1jf4j46h5b7h6j9784ggb5656jh7j47h5"
# cleaning_txt = ""
# for i in txt:
#     if len(txt) % 2 == 0:
#         if i.isdigit():
#             if int(i) % 2 == 0:
#                 i = " "
#                 cleaning_txt += i
#     else:
#         if i.isdigit():
#             if int(i) % 2 != 0:
#                 i = " "
#                 cleaning_txt += i
#     cleaning_txt += i
# print(cleaning_txt)