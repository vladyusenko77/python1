# 1. Написати функцію, яка порівнює два цілих числа і повертає
# результат порівняння в вигляді одного з знаків: <, > або =.


# def por(a, b):
#     if a > b:
#         result = " > "
#     elif b > a:
#         result = " < "
#     elif a == b:
#         result = " = "
#     return result


# a = int(input("ведьть перше число:"))
# b = int(input("ведьть друге число:"))

# res = por(a, b)
# print("перше", res, "друге")


# 2. Написати функцію, яка отримує в якості параметрів два цілих числа і повертає суму чисел з діапазону між ними.

# def sum(a=0, b=0):
#     su = 0
#     i = a+1
#     while i < b:
#         print(i)
#         su += i
#         i += 1
#     return su


# a = int(input("enter A ="))
# b = int(input("enter B ="))
# res = sum(a, b)
# print("сума діапазон", res)

# 3. Написати функцію, яка обчислює вартість поїздки на автомобілі на дачу (туди і назад). Вхідними даними є: відстань до дачі (км);
#  кількість бензину, яку споживає автомобіль на 100 км пробігу; ціна одного літру бензину. Дані для розрахунків вводяться користувачем.

# print("сколько будет стоить ваша поездка:\n")


# def su():
#     km = float(input("Сколько километров до вашей дачи:"))
#     benz = float(input("Скільки жре ваш автомобіль на  100 км ?:"))
#     wog = float(input("цiна бензину?:"))
#     suma = ((benz/(km/wog))*100)
#     print("ваша поїздка обійдеться в:", suma, "грн")


# su()


# 4.Написати калькулятор, робота якого буде основана на функціях. Введення цифр та вибір математичної операції виконати в
#  діалоговомустилі (запитати у користувача, вивести меню). У програмі передбачити уникнення помилок
#  (ділення на нуль і т.д.). Фантазія та «дизайн» меню – ціниться та вітається!!!
# Примітка! Кожна арифметична операція описується окремою функцією. Побудова самого меню також винесена в окрему функцію

# print("1.Калькулятор \n "'2.Степені \n ''3.Про калькулятор')
# a = int(input("Виберіть фукнкцію: "))
# if a == 1:
#     x = float(input("Введіть перше число: "))
#     y = float(input("Введіть друге число: "))
#     operation = input('Введіть знак операції: ')
#     result = None
#     if operation == "+":
#         result = x + y
#     elif operation == '-':
#         result = x - y
#     elif operation == '*':
#         result = x * y
#     elif (operation == "/") and (y != 0):
#         result = x / y
#     else:
#         print("Ви поламали калькулятор, перезапустіть його")
#     print("Результат: ", result)

# elif a == 2:
#     b = float(input("Введіть число, яке хочете піднести до степеня: "))
#     c = float(input("Введіть степінь: "))
#     some = b ** c
#     print(some)
# elif a == 3:
#     print("Версія: v1.0 \n ""©BOMBA Production \n ""vlad yusenko")
# else:
#     print('eroor тут тільки 3 можливих функції!!!')


def add_num():
    a = int(input("ведіть першу цифру:"))
    b = int(input("ведіть другу цифру:"))
    print(a+b)


def subst_num():
    a = int(input("ведіть першу цифру:"))
    b = int(input("ведіть другу цифру:"))
    print(a-b)


def mult_num():
    a = int(input("Eведіть першу цифру"))
    b = int(input("ведіть другу цифру:"))
    print(a*b)


def div_num():
    a = int(input("ведіть першу цифру"))
    b = int(input("ведіть другу цифру:"))
    print(a/b)


calc = input("1 - додавання, 2 - віднімання, 3 - множення, 4 - ділення: ")
if calc == "1":
    add_num()
elif calc == "2":
    subst_num()
elif calc == "3":
    mult_num()
elif calc == "4":
    div_num()
else:
    print("eror")