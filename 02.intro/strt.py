# Протягом тижня вимірювали температуру повітря.
# Знайти кількість днів, коли температура перевищувала 10o С.


# days = 0
# count = 0
# while days <= 7:
#     a = int(input("temr= "))
#     if a > 10:
#         count += 1
#     days += 1
# print(count)


# 2. Скласти програму ’Атракціони’. Програма запитує суму (грн.) у користувача. Потім виводить на екран перелік доступних атракціонів.
#  Користувач обирає атракціон та ’оплачує’ його. Вихід з програми при виборі пункту ’вихід’ або при недостатній сумі грошей.


# sym = input ("ведьть вашу суму:")

# a = input(
#     "!!!доступні актриціони на вашу суму!!!\n1=колесо фортуни\n2=смертельна комната\n3=король гори\nвиберить актриціони:")


# exit = True
# while exit:
#     erormany = True
#     while erormany:
#         many = int(input("Enter you many = "))
#         if many < 100:
#             print("EROR manuy min 100")
#         elif many >= 100:
#             erormany = False

#     print("Welcom to the \n    ATTRACTION")
#     exitt = True
#     while exitt:

#         vyb = int(input(
#             "1.Swing = 100 \n2.Trampoline = 150\n3.Dars = 180\n9.Reset games\n0.EXIT ATTRACTION\nENTER NEW GAMES"))
#         if vyb == 1:
#             print("Swing - 100")
#             many -= 100
#         elif vyb == 2:
#             print("Trampoline - 150")
#             many -= 150
#         elif vyb == 3:
#             print("Dars - 180")
#             many -= 180
#         elif vyb == 9:
#             exitt = False
#         elif vyb == 0:
#             exitt = False
#             exit = False
#         if many < 100:
#             print("EROR manuy min 100")
#             exitt = False

# Написати програму, яка виводит на екран 10 випадкових чисел у діапазоні від 0 до 17 і підраховує їх суму та добуток.

# import random

# c = 0
# sum = 0
# dobutok = 1
# print("_________________")
# while c <= 10:
#     g = random.randrange(1, 17)
#     print("цифра\t", g)
#     sum += g
#     dobutok *= g
#     c += 1
# print("_________________")
# print("сума:", sum)
# print("добуток:", dobutok)


# Комп’ютер кидає кубик(за допомогою генератора випадкових чисел). Порахувати через скільки спроб випаде шістка.

# from random import randint
# import json


# i1 = 0
# i2 = 0
# while i2 <= 10:
#     p1 = 0
#     p2 = 0

#     input("Ви:_Бросить кости !\nНажмите 1 :")
#     f = randint(1, 6)
#     h = randint(1, 6)
#     sum1 = f+h
#     o = randint(1, 6)
#     p = randint(1, 6)
#     sum2 = o+p
#     print("Ваш бросок:", sum1)
#     if sum1 % 2 == 0:
#         p1 += 2
#         i1 += p1
#         print("Ви:\n", i1, "бали")
#     else:
#         p1 += 1
#         i1 += p1
#         print("ви:\n", i1, "бали")

#     print("🎲🎲🎲")
#     input("PC:_киньте кocти !\nНатисніть 2 :")
#     print("бросок PC:", sum2)

#     if sum2 % 2 == 0:
#         p2 += 2
#         i2 += p2
#         print("PC:\n", i2, "бали")
#     else:
#         p2 += 1
#         i2 += p2
#         print("PC:\n", i2, "бали")

#     print("_____________________")
# if i1 > i2:
#     print("|_-_-_-_-_-_-_-_-_-_-_-_-_-_|")
#     print("Ти Виграв:",  i1, "балів")
#     print("|_-_-_-_-_-_-_-_-_-_-_-_-_-_|")
# elif i2 > i1:
#     print("|_-_-_-_-_-_-_-_-_-_-_-_-_-_|")
#     print("PC Виграв:",  i2, "балів")
#     print("|_-_-_-_-_-_-_-_-_-_-_-_-_-_|")
# else:
#     print("|_-_-_-_-_-_-_-_-_-_-_-_-_-_|")
#     print("нічія:", i1, "=", i2)
#     print("|_-_-_-_-_-_-_-_-_-_-_-_-_-_|")
