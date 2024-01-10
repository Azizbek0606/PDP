class Employes:
    def init(self):
        self.First_Name = ""
        self.Last_Name = ""

class CRUD:
    def init(self):
        self.first_name = []
        self.last_name = []
        self.group_scores = []
        self.azo = Employes()

    def add_scores(self):
        total_scores = []
        for first, last in zip(self.first_name, self.last_name):
            score = int(input(f"Umumiy ballarni kiriting {first} {last} uchun: "))
            total_scores.append(score)
        print("--------------------------------------------------------")

    def add_group_score(self, group_score):
        self.group_scores.append(group_score)

    def display_scores_descending(self):
        total_scores = []
        for first, last in zip(self.first_name, self.last_name):
            score = int(input(f"Umumiy ballarni kiriting {first} {last} uchun: "))
            total_scores.append(score)

        sorted_participants = sorted(
            zip(self.first_name, self.last_name, total_scores),
            key=lambda participant: participant[2],
            reverse=True
        )

        print("Umumiy ballarga ko'ra tartiblangan ishtirokchilar:")
        for participant in sorted_participants:
            print(f"|Ism| => {participant[0]}; |Familya| => {participant[1]}; |Umumiy Ballar| => {participant[2]};")
        print("-----------------------------------------------------")

    def create_ishtirokchi(self):
        try:
            last_name = input("Familya kiriting : ")
            first_name = input("Ism kiriting : ")

            self.last_name.append(last_name)
            self.first_name.append(first_name)
        except Exception as e:
            print(f"Xatolik: {e}")

    def index_find(self, name):
        for i, first in enumerate(self.first_name):
            if first == name:
                return i
        return -1

    def delete_ishtirokchi(self):
        print("-----------------------------------------------------")
        name = input("Ismni kiriting : ")
        index = self.index_find(name)

        if index > -1:
            self.last_name.pop(index)
            self.first_name.pop(index)
            print("Student o'chirildi ")
            print("Qolgan Studentlar ro'yxati ")
        else:
            print("Siz qidirgan student mavjud emas")

    def info(self):
        for first, last in zip(self.first_name, self.last_name):
            print(f"|Ism| => {first}; |Familya| => {last};")
        print("-----------------------------------------------------")


def add_participants(crud, group=False):
    count = int(input("Nechta ishtirokchi qo'shmoqchisiz : "))
    print("--------------------------------------------------")

    for _ in range(count):
        print("ishtirokchini kiriting ")
        crud.create_ishtirokchi()

    if group:
        group_score = int(input("Butun guruh uchun umumiy ballni kiriting: "))
        crud.add_group_score(group_score)

    print("Ishtirokchilar muvofaqqiyatli qo'shildi")
    print("-----------------------------------------------------")


def add_participants_group(crud, group=False):
    count = 5

    for _ in range(count):
        print("ishtirokchini kiriting ")
        crud.create_ishtirokchi()

    if group:
        group_score = int(input("Butun guruh uchun umumiy ballni kiriting: "))
        crud.add_group_score(group_score)

    print("Ishtirokchilar muvofaqqiyatli qo'shildi")
    print("-----------------------------------------------------")


def add_group(crud):
    add_participants_group(crud, group=True)


def main():
    print("Xush kelibsiz")

    ishtirokchi = CRUD()

    while True:
        print("---------------------------------------------------")
        print(" 1-Yangi azo qo'shish\n 2-ishtirokchilarni o'chirish\n 3-Yangi jamoa qo'shish")
        print("---------------------------------------------------")
        tanlov = int(input("Tanlovdan birini tanlang : "))


if tanlov == 1:
    add_participants(ishtirokchi)
    ishtirokchi.info()
    print("1-Ballarni belgilash\n2-Dasturni yakunlayman")
    print("--------------------------------------------------")
    tanlov = int(input("Tanlovni kiriting : "))

if tanlov == 1:
    ishtirokchi.add_scores()
    ishtirokchi.display_scores_descending()
    print("1-Davom etaman\n2-Dasturni yakunlayman")
    print("------------------------------------------------------")
    tanlov = int(input("Tanlovni kiriting : "))

    if tanlov == 1:
        continue
    elif tanlov == 2:
        break

elif tanlov == 2:
    break

elif tanlov == 2:
    ishtirokchi.delete_ishtirokchi()
    ishtirokchi.info()
    print("1-Davom etaman\n2-Dasturni yakunlayman")
    print("------------------------------------------------------")
    tanlov = int(input("Tanlovni kiriting : "))

    if tanlov == 1:
        continue
    elif tanlov == 2:
        break

elif tanlov == 3:
    count = int(input("Nechta Jamoa qo'shmoqchisiz : "))
    print("--------------------------------------------------")

    for i in range(1, count + 1):
        print(f"{i} - Jamoaning ", end="")
        add_group(ishtirokchi)

    ishtirokchi.info()
    print("1-Davom etaman\n2-Dasturni yakunlayman")
    print("--------------------------------------------------")
    tanlov = int(input("Tanlovni kiriting : "))

if tanlov == 1:
    continue
elif tanlov == 2:
    break


if name == "main":
    main()