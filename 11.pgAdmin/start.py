from lib.db import dbpostgress, add_card
import random


class Account:
    def __init__(self, number, name, surname, amount, currancy):
        self.name = name
        self.surname = surname
        self.number = number
        self.amount = amount
        self.currancy = currancy

    def save_data(self):
        add_card(self.number, self.name, self.surname,
                 self.amount, self.currancy)

    def show_account_info(self):
        print("Number => ",  self.number, "\nName => ", self.name, "\nSurname => ", self.surname,  "\nAmount => ",
              self.amount, "\nCurrency => ", self.currancy)

    def set_money(self, amount):
        print("Added money... ", amount, self.currancy)
        self.amount += amount

    def get_money(self, amount):
        print("Get money... ", amount, self.currancy)
        self.amount -= amount


def menu():
    choice = int(input("1. Create card "))
    if choice == 1:
        name = input("Client name: ")
        surname = input("Client surname: ")
        amount = float(input("Amout: "))
        currency = input("Currancy: ")
        card1 = Account(random.randint(10000000,
                                       99999999), name, surname, amount, currency)
        card1.save_data()
    else:
        print("NOT Working")


menu()
