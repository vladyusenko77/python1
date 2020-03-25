import random
# Оголосити list з 7 елементів типу int. Заповнити його випадковими
# значеннями в діапазоні [-12..+50] та вивести на екран.
# Підрахувати кількість відємних та додатніх елементів масиву.

# arr = []


# def fill_arr(arr):
#     i = 0
#     while i < 7:
#         arr.append(random.randint(-12, 50))
#         i += 1


# def show_arr(arr):
#     for item in arr:
#         print(item)


# def fill_plus_minus(arr):
#     plus_numbers = 0
#     minus_numbers = 0

#     for item in arr:
#         if item > 0:
#             plus_numbers += 1
#         elif item < 0:
#             minus_numbers += 1
#     print("plus_numbers = ", plus_numbers)
#     print("minus_numbers = ", minus_numbers)


# fill_arr(arr)
# show_arr(arr)
# fill_plus_minus(arr)


# ===================================>>>
#  a = 8
#  if a % 2 == 0:
#      print("true")
#  else:
#      print("False")
# ===================================>>>


# масив з 7 елементів типу int. Визначити суму парних елементів масиву

arr = []


def fill_arr(arr):
    i = 0
    while i < 7:
        arr.append(random.randint(-12, 50))
        i += 1


def vlad(arr):
    n = 0
    z = 0
    while n != 55:
        if n % 2 == 0:
            z += 0
        else:
            z += 0


fill_arr(arr)
vlad(arr)
print("сума парних", z)

# 3.Дано масив А. Скопіювати елементи масиву А у масив В.
# import copy

# a = [34,2,34,65,79,99,101,5]
# b = []
# b=copy.deepcopy(a)
# print("Результат за допомогою копії",b)

# Дано одновимірний масив. Знайти найбільший та найменший елементи масиву та поміняти їх у масиві місцями.


# arr = []


# def fill_arr(arr):
#     i = 0
#     while i < 7:
#         arr.append(random.randint(-12, 50))
#         i += 1


# def fu_arr(arr):
#     print(arr)
#     min_index = arr.index(min(arr))
#     max_index = arr.index(max(arr))
#     print("minimum->", min(arr))
#     print("maximum->", max(arr))
#     print("min_index", min_index)
#     print("max_index", max_index)
#     arr.reverse()
#     print(arr)


# fill_arr(arr)
# fu_arr(arr)
