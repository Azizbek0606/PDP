participant_arr = []
participant_ball_arr = []
participant_team_members = []
stage = ["Listening", "reading", "speaking", "writing", ""]


def get_positive_input(inner_text):
    while True:
        try:
            user_input = int(input(inner_text))
            if user_input >= 2:
                return user_input
            else:
                print("Noto'g'ri qiymat. Kamida 2 yoki undan yuqori son kiriting.")
        except ValueError:
            print("Noto'g'ri qiymat. Faqat son kiriting.")


def get_participant_name(index, alert_input):
    while True:
        participant = input(f"{index + 1}-{alert_input}:\n")
        if type(participant) == str and participant != "":
            return participant


def get_ball_players(participant_index, input_text):
    while True:
        try:
            ball = int(
                input(
                    f"\n{participant_index + 1} - {input_text}: {participant_arr[participant_index]} uchun ball: "
                )
            )
            if type(ball) == int and ball >= 0:
                return ball
            else: 
                print("Noto'g'ri qiymat. Faqat son kiriting.")
        except ValueError:
            print("Noto'g'ri qiymat. Faqat son kiriting.")


def alone():
    participant_count = get_positive_input("\nIshtirokchi sonini kiriting: ")
    print("-----------------------------------------------------------------------")
    for i in range(int(participant_count)):
        participant_arr.append(get_participant_name(i, "ishtirokchi ismini kiriting"))
    print("-----------------------------------------------------------------------")

    print(f"\nO'yin boshlandi.\nJami ishtirokchilar soni {participant_count}ta ular:\n")

    for i in range(int(len(participant_arr))):
        print(f"{i + 1} - ishtirokchi: {participant_arr[i]}")
    print("-----------------------------------------------------------------------")
    game_counter = 0
    for i in range(5):
        print(
            f"\n{game_counter + 1} - bosqich yakunlandi\nishtirokchilarga {game_counter + 1} - bosqich bo'yicha ball bering\n"
        )
        limited_arr_for_ball = []

        for k in range(int(len(participant_arr))):
            limited_arr_for_ball.append(get_ball_players(k, "Ishtirokchi"))
        game_counter += 1
        participant_ball_arr.append(limited_arr_for_ball)
    print("-----------------------------------------------------------------------")

    level_counter = 0
    print("\nBarcha bosqichlar yakunlandi\nishtirokchilarning umumiy ballari:\n")
    get_max_ball = []
    for i in range(int(len(participant_arr))):
        ball_arr = []
        for k in participant_ball_arr:
            level_counter += 1
            print(f"{participant_arr[i]} {level_counter} - bosqichda {k[i]}: ball oldi")
            ball_arr.append(k[i])
            if level_counter == 5:
                level_counter = 0
                print("\n\n")
                get_max_ball.append(sum(ball_arr))
    max_ball = max(get_max_ball)
    max_ball_index = get_max_ball.index(max_ball)
    print("-----------------------------------------------------------------------")
    print(f"G'olib: {participant_arr[max_ball_index]}\njami to'plagan bali: {max_ball}")


def team():
    group_count = get_positive_input("Gurux sonini kiriting:\n")
    group_member = get_positive_input("Gurux a'zolari sonini kiriting:\n")
    print("-----------------------------------------------------------------------")
    for i in range(group_count):
        participant_arr.append(get_participant_name(i, "gurux nomini kiriting"))
    for i in range(group_member * group_count):
        participant_team_members.append(get_participant_name(i, "ishtirokchining ismi"))
    print("-----------------------------------------------------------------------")
    print(
        f"\nO'yin boshlandi.\nJami ishtirokchilar soni {group_member * group_count}ta ular:\n"
    )

    for i in range(int(group_member * group_member)):
        print(f"{i + 1} - ishtirokchi: {participant_team_members[i]}")
    print("-----------------------------------------------------------------------")
    game_counter = 0
    for i in range(5):
        print(
            f"\n{game_counter + 1} - bosqich yakunlandi\nguruxlarga {game_counter + 1} - bosqich bo'yicha ball bering\n"
        )
        limited_arr_for_ball = []

        for k in range(int(len(participant_arr))):
            limited_arr_for_ball.append(get_ball_players(k, "gurux"))
        game_counter += 1
        participant_ball_arr.append(limited_arr_for_ball)
    print("-----------------------------------------------------------------------")
    print("\nBarcha bosqichlar yakunlandi\nguruxlarning umumiy ballari:\n")
    level_counter = 0
    get_max_ball = []
    for i in range(int(len(participant_arr))):
        ball_arr = []
        for k in participant_ball_arr:
            level_counter += 1
            print(f"{participant_arr[i]} {level_counter} - bosqichda {k[i]}: ball oldi")
            ball_arr.append(k[i])
            if level_counter == 5:
                level_counter = 0
                print("\n\n")
                get_max_ball.append(sum(ball_arr))
    print("-----------------------------------------------------------------------")
    max_ball = max(get_max_ball)
    max_ball_index = get_max_ball.index(max_ball)
    print(
        f"G'olib: {participant_arr[max_ball_index]} guruhi\n. Jami to'plagan ballari: {max_ball}\n\n"
    )


while True:
    print(
        "__________________________________________________________________________\n"
    )
    print("1 - Yakka tartib")
    print("2 - Jamoavi tartib")
    print("3 - Dasturni to'xtatish")
    print(
        "\n__________________________________________________________________________"
    )
    input_inducator = int(input("\nFaqat son kiriting: "))
    if type(input_inducator) == int and input_inducator > 0 and input_inducator <= 3:
        if input_inducator == 1:
            alone()
        elif input_inducator == 2:
            team()
        elif input_inducator == 3:
            break
    else:
        continue
