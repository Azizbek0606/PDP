txt = True
counter = 0
while txt:
    print(1)
    counter += 1
    if counter == 10:
        print("loop tugadi")
        txt = False

check = True
arr = []
while check:
    inp_txt = input("matn kiriting: ")
    if inp_txt.lower() != "stop":
        arr.append(inp_txt)
    else:
        check = False
else:
    print("Dastur to'xtatildi \nkiritilgan so'zlar:")

for i in arr:
    print(i)