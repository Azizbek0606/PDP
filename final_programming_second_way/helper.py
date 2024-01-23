def yakka():
    print("Yakka tartib tanlandi\n")
    input_num = int(input("Ishtirokchilar sonini kiriting:"))
    ishtirokchilar = []
    musobaqa_bosqichi = []
    ball = []
    if input_num >= 2 and input_num <= 20:
        for i in range(input_num):
            input_name = input(f"{i + 1} - ishtirokchi ismini kiriting:\n")
            ishtirokchilar.append(input_name)
    input("Ishtirokchilar ismi muvofaqqiyatli saqlandi\n\n\nMusobaqa turini kiriting: ")
    for i in range(5):
        bosqich = input(f"{i + 1} - bosqich nomini kiriting: ")
        musobaqa_bosqichi.append(bosqich)
    for i in range(input_num):
        ball.append([])
    for i in range(int(len(musobaqa_bosqichi))):
        print(f"{musobaqa_bosqichi[i]} - bosqichi yakunlandi")
        for k in range(input_num):
            input_ball = int(
                input(f"\n{ishtirokchilar[k]} - ishtirokchiga ball bering:")
            )
            ball[k].append(input_ball)
    max_index = ball.index(max(ball))
    print(
        f"G'olib {max_index + 1} - ishtirokchi {ishtirokchilar[max_index]} bo'ldi {sum(ball[max_index])} ball bilan"
    )


def jamoaviy():
    print(" Jamoaviy tartib tanlandi\n")
    input_group_num = int(input("guruxlar sonini kiriting: "))
    input_num = int(input("Ishtirokchilar sonini kiriting: "))
    gurux_nomi = []
    ishtirokchilar = []
    musobaqa_bosqichi = []
    ball = []
    if input_group_num >= 2 and input_group_num <= 20:
        for i in range(input_group_num):
            gurux_nomi.append(input(f"{i + 1} - gurux nomini kiriting:"))
        for i in range(input_group_num * input_num):
            input_name = input(f"{i + 1} - ishtirokchi ismini kiriting:\n")
            ishtirokchilar.append(input_name)
    input("Gurux nomi va ishtirokchilar ismi muvofaqqiyatli saqlandi\n\n\nMusobaqa turini kiriting: ")
    for i in range(5):
        bosqich = input(f"{i + 1} - bosqich nomini kiriting: ")
        musobaqa_bosqichi.append(bosqich)
    for i in range(input_num):
        ball.append([])
    for i in range(int(len(musobaqa_bosqichi))):
        print(f"{musobaqa_bosqichi[i]} - bosqichi yakunlandi")
        for k in range(input_group_num):
            input_ball = int(
                input(f"\n{gurux_nomi[k]} - guruxga ball bering:")
            )
            ball[k].append(input_ball)
    max_index = ball.index(max(ball))
    print(
        f"G'olib {max_index + 1} - gurux {gurux_nomi[max_index]} bo'ldi {sum(ball[max_index])} ball bilan"
    )


print("Xush kelibsiz !\nMusobaqa qanday tartibda bo'lishini tanlang: ")
while True:
    print("1 - yakka tartib\n2 - Jamoaviy\n3 - Dasturni to'xtatish")
    input_num = int(input("\n\n 1 dan 3 gacha bo'lgan sonlar ichidan birini tanlang: "))
    if input_num > 0 and input_num <= 3:
        if input_num == 1:
            yakka()
        elif input_num == 2:
            jamoaviy()
        elif input_num == 3:
            print("Dastur to'xtatildi!")
            break
    else:
        continue
