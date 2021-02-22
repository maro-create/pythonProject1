prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}
celkoveProdeje = 0
nazevKnihy = input("Zadej nazev knihy: ")
if nazevKnihy in prodeje2020:
    celkoveProdeje += prodeje2020[nazevKnihy]
    if nazevKnihy in prodeje2019:
        celkoveProdeje += prodeje2019[nazevKnihy]
        print(f"Celkove prodeje za rok 2019 a 2020 jsou {celkoveProdeje} Kc.")
    else:
        print(f"Celkove prodeje za rok 2019 a 2020 jsou {prodeje2020[nazevKnihy]} Kc.")
elif nazevKnihy in prodeje2019:
    print(f"Celkove prodeje za rok 2019 a 2020 jsou {prodeje2019[nazevKnihy]} Kc.")
else:
    print("Tato kniha v roce 2019 a 2020 nebyla prodana.")