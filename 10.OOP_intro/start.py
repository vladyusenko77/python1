# class Person:
#     def __init__(self, name, salary):
#         # print("Constructor works")
#         self.name = name
#         self.salary = salary

#     # def __del__(self):
#     #     print("Destructor works")

#     def show_person(self):
#         print("Name: ", self.name)
#         print("Salary: ", self.salary)


# person1 = Person("Bill", 1100)
# person1.show_person()

# person2 = Person("Tom", 1350)
# person2.show_person()

# if person1.salary > person2.salary:
#     print(person1.name, ">", person2.name)
# elif person1.salary < person2.salary:
#     print(person1.name, "<", person2.name)
# else:
#     print("Salary =", person1.name, "=", person2.name)


# Написати клас "Банківський рахунок" (Account), який містить:
# Номер рахунку
# 	  Розмір коштів на рахунку
# 	  Назва валюти рахунку (рублі, гривні, евро тощо), для позначення якої можна скористатись одним символом: R, G, E, $ тощо
# Забезпечити можливість:
# Відкривати рахунок та первинно вносити гроші на рахунок
# 	  Знімати гроші з рахунку
#     Докладати гроші на рахунок
# ПРИМІТКА! На 12 балів реалізувати також можливість здійснювати переказ грошей з одного рахунку на другий.

import random


from random import randint


class Account:
    def __init__(self, card_number, amount, currancy):
        self.__card_number = card_number
        self.__amount = amount
        self.__currancy = currancy
        print("____________________________________________")

    def show_open(self):
        print("Your Card number:", self.__card_number, "\nAmount:",
              self.__amount, self.__currancy)

    def get_cash(self):
        cost = int(input("Сколько денег вы хотите взять?: "))
        self.__amount -= cost
        return self.__amount

    def set_cash(self):
        value = int(
            input("сколько денег вы добавляете к своей сумме?: "))
        self.__amount += value
        return self.__amount


while True:
    print("\t\tBANK *Offshore* ")
    first_answear = int(input(
        "\t\t________\n\t\t++MENU++\n1. Зареєструвати новий акаунт\n2. Показати рахунок\n3. зняти гроші\n4. Добавить деньги\n0.EXIT\n\tВаше действие: "))
    if first_answear == 1:
        amount = int(
            input("скільки ви хочете положит грошей на картку?:"))
        second_answear = int(
            input("Выбор валюты\n1. USD\n2. EURO\n3. UAN\n4. RUB\n\tYour action: "))
        if second_answear == 1:
            currancy = "USD"
        elif second_answear == 2:
            currancy = "EURO"
        elif second_answear == 3:
            currancy = "UAN"
        elif second_answear == 4:
            currancy = "RUB"
        card_number = randint(10000000000000000, 99999999999999999)
        input("Вы создали аккаунт в нашем банке\nСпасибо за ваше доверие\nНажмите Enter,чтобы перейти в меню:")
    elif first_answear == 2:
        credit_card = Account(card_number, amount, currancy)
        credit_card.show_open()
        input("Войдите для выхода в меню")
        print("=========================")
    elif first_answear == 3:
        amount = credit_card.get_cash()
        print("=========================")
        print("Remainder", amount, currancy)
        print("=========================")
    elif first_answear == 4:

        amount = credit_card.set_cash()
        print("==========================")
        print("Remainder", amount, currancy)
        print("==========================")
    elif first_answear == 0:
        break
    else:
        print("Извините, это неправильно. Прощай!")
        break
