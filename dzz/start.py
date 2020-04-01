from lib.db import add_capital, del_capital, show_all_country, edit_capital, edit_population


def menu():
    while True:
        choice = int(input(
            "1>Добавить страну \n2>Удалить страну \n3>Показать страну \n4>Изменить столицу \n5>Изменить население\n6>exit\n==>>:"))
        if choice == 1:
            country = input("Country: ")
            capital = input("Capital: ")
            population = int(input("Population: "))
            Mayor = input("Mayor: ")
            add_capital(country, capital, population, Mayor)
        elif choice == 2:
            country = input("яку страну хочете удалити?: ")
            del_capital(country)
        elif choice == 3:
            show_all_country()
        elif choice == 4:
            country = input("Введіть назву країни ==> ")
            capital = input("Введіть нову столицю == >")
            edit_capital(country, capital)
        elif choice == 5:
            country = input("Введіть назву країни ==> ")
            population = input("Введіть нову кількість населення ==> ")
            edit_population(country, population)
        elif choice == 6:
            print("eror(=_+)")
            break


menu()
