# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr2 = [3, 4, 6, 7]
# for k in arr2:
#     if k in arr1:
#         arr1.remove(k)
# print(arr1)


# arr = [1, 2, 3, "fi", "fi", "fi"]
# num = 0
# text = 0
# for i in arr:
#     if type(i) == str:
#         text += 1
#     else:
#         num += 1
# print(f"raqamlar soni {num} ta\nso'zlar soni {text} ta")


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, "qwer", "tyui", "opas"]
# arr1 = []
# for p in arr:
#     if type(p) == str:
#         arr1.append(p)
# print(arr1)


# txt = "azizbek xabibullayev lorem ipsum dolor sit two one"
# arr = txt.split(" ")
# found_word = ''
# checker_word_index = 0
# for i in arr:
#     if arr.count(arr[checker_word_index]) >= 2:
#         found_word = arr[checker_word_index]
#         break
#     else:
#         checker_word_index += 1
# print(found_word if found_word else "takrorlangan so'zlar mavjud emas")

# txt = "azizbek xabibullayev  ipsum dolor sit two one"
# arr = txt.split(" ")
# found_word = arr[0]
# all_word_len = True

# for i in arr:
#     if len(i) > len(found_word):
#         found_word = i
#         all_word_len = False

# if all_word_len:
#     print("barcha so'zlarning uzunligi bir xil")
# else:
#     print(found_word)

# txt = "azizbek xabibullayev ipsum dolor sit two one"
# arr = txt.split(" ")
# words_count = txt.count(" ") + 1
# print(f"mantda ishlatilgan so'zlar soni: {words_count} ta")
# print("har bir so'zlar soni: ")
# for i in arr:
#     print(len(i))

# a = False
# if (a != False) and (4 % 2 != 0) or (type("int") != int):
#     print(True)
# elif len("azizbek") % 2 != 0 and bool(False):
#     print("True1")
# else:
#     print("tugadi")
# txt = "azizbek xabibullayev ipsum dolor sit two one"
# arr = txt.split(" ")
# second_str = ""
# for i in arr:
#     second_str += f" {i[::-1]}"
# print(second_str)


arr = [1,2,3,4,5,6,99,66 , 8,9,7,6,5,44]
max_arr = 0
min_arr = 0
sorted_arr = []
juft__arr = []
toq_arr = []
arr.sort()
print(arr)
