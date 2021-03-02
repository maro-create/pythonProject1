telCislo = input("Zadejte číslo, kam chcete zprávu zaslat:")
telCislo = telCislo.replace(" ","")
cenaZpravy = 3
# Zprava ma max. 180 znaku
if (len(telCislo)) == 9 or (len(telCislo)) == 13:
    textZpravy = input("Zadejte text zprávy, kterou chcete zaslat:")
    pocetZprav = (len(textZpravy))//180+1
    cenaZpravy += pocetZprav*(3)
    print(f"Cena zprávy je {cenaZpravy} Kč.")
else:
    print("Zadali jste chybní telefonní číslo.")
