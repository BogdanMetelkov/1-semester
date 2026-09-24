
logins = ["student1", "student2", "student3", "student4"]
passwords = ["111", "222", "333", "444"]
all_grades = [
    [10, 8, 3, 11, 5],
    [2, 3, 4, 1, 6],
    [12, 10, 9, 8, 7],
    [4, 5, 5, 3, 2]
]

print("=== СИСТЕМА ОБЛІКУ ОЦІНОК ===")
user_login = input("Введіть логін: ")
user_pass = input("Введіть пароль: ")


found = False
index = 0

for i in range(len(logins)):
    if logins[i] == user_login and passwords[i] == user_pass:
        found = True
        index = i
        break

if found == True:
    print("\nВхід успішний!")

    my_grades = all_grades[index]
    print("Ваші оцінки:", my_grades)

    zadowilno = 0  # від 5 до 12
    nezadowilno = 0  # від 1 до 4

    for grade in my_grades:
        if grade >= 5 and grade <= 12:
            zadowilno = zadowilno + 1
        elif grade >= 1 and grade <= 4:
            nezadowilno = nezadowilno + 1

    print("Кількість задовільних (від 5 до 12):", zadowilno)
    print("Кількість незадовільних (від 1 до 4):", nezadowilno)

else:
    print("\nНеправильний логін або пароль!")