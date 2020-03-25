# Написати функцію, яка отримує дату (день, місяць) і виводить назву свята,
# що випадає на цей день (наприклад, 7.01 – Різдво, 9.05 – День Перемоги). Запрограмувати реакцію програми на 4 – 5 свят.


def holiday():
    month = int(input("Введіть місяць року від 1 до 12:"))
    day = int(input("Введіть день місяця від 1 до 31:"))

    if month == 1 and day == 1:
        print(month, ".", day, ": Новий рік ")
    elif month == 1 and day == 7:
        print(month, ".", day, ": Різдво Христове")
    elif month == 3 and day == 8:
        print(month, ".", day, ": Міжнародний жіночий день")
    elif month == 5 and day == 27:
        print(month, ".", day, ": Великдень")
    elif month == 5 and day == 1:
        print(month, ".", day, ": День праці")
    elif month == 6 and day == 28:
        print(month, ".", day, ": День Конституції України")
    elif month == 8 and day == 16:
        print(month, ".", day, ": Трійця")
    elif month == 10 and day == 14:
        print(month, ".", day, ": День захисника України")
    elif month == 12 and day == 25:
        print(month, ".", day, ": Різдво Христове")
    else:
        print("Відпустки немає, до роботи")


holiday()
