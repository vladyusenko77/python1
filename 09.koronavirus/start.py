from korona.db import add_corona, dell, vyvid_str
import requests

URL = "https://api.covid19api.com/summary"


def XZ_URL(URL):
    responce = requests.get(URL)
    return responce.json()


coron = requests.get(URL)
coron = coron.json()


def zapov(coron):
    # print(coron)
    for item in coron["Countries"]:
        Country = item["Country"]
        Slug = item["Slug"]
        NewConfirmed = item["NewConfirmed"]
        TotalConfirmed = item["TotalConfirmed"]
        NewDeaths = item["NewDeaths"]
        TotalDeaths = item["TotalDeaths"]
        NewRecovered = item["NewRecovered"]
        TotalRecovered = item["TotalRecovered"]
        add_corona(Country, Slug, NewConfirmed, TotalConfirmed,
                   NewDeaths, TotalDeaths, NewRecovered, TotalRecovered)


def menu(coron):
    exit = True
    while exit:
        koronav = int(input("1.output\n2.Update\n0.Exit\n=>"))
        if koronav == 1:
            print("output")
            vyvid_str()
        elif koronav == 2:
            print("output")
            dell()
            zapov(coron)
        elif koronav == 0:
            exit = False


menu(coron)
# coronavirus
