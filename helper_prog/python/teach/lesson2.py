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


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, "qwer", "tyui", "opas"]
arr1 = []
for p in arr:
    if type(p) == str:
        arr1.append(p)
print(arr1)
