students = [
    ("Анна", 19, ["Математика", "Информатика"]),
    ("Иван", 22, ["Физика", "Информатика"]),
    ("Мария", 19, ["Литература", "Искусство"]),
    ("Алексей", 20, ["Химия", "Биология"]),
    ("Елена", 21, ["Физика", "Искусство"]),
    ("Дмитрий", 18, ["Математика", "Литература"]),
    ("Ольга", 22, ["Информатика", "Биология"]),
    ("Павел", 20, ["Искусство", "Физика"]),
    ("Алина", 19, ["Информатика", "Математика"]),
    ("Артем", 21, ["Биология", "Химия"]),
    ("Наталья", 18, ["Литература", "Искусство"]),
    ("Сергей", 23, ["Информатика", "Физика"]),
    ("Евгения", 20, ["Химия", "Биология"]),
    ("Андрей", 24, ["Искусство", "Литература"]),
    ("Виктория", 22, ["Физика", "Информатика"]),
    ("Максим", 19, ["Биология", "Химия"]),
    ("Юлия", 21, ["Информатика", "Физика"]),
    ("Кирилл", 20, ["Математика", "Биология"]),
    ("Анастасия", 23, ["Литература", "Искусство"]),
    ("Роман", 18, ["Информатика", "Физика"]),
]

sp_curs = set()
vgroupl21 = []
vgroup21 = []

for i in students:
    for j in i[2]:
        sp_curs.add(j)
    if i[1] < 21:
        vgroupl21.append(i[0])
    else:
        vgroup21.append(i[0])

print(*sorted(sp_curs))
print(*sorted(vgroupl21))
print(*sorted(vgroup21))
