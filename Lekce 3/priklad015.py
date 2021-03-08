datum = input("Zadejte datum, pro které chcete vstupenky koupit ve formátu DD.MM.RRRR: ")
from datetime import datetime
pozadovaneDatum = datetime.strptime(datum, "%d.%m.%Y")
print("pozadovaneDatum =", pozadovaneDatum)
pocetOsob = int(input ("Zadejte počet osob: "))
zacatekSezonyA = datetime(2021,7,1)
konecSezonyA = datetime(2021,8,10)
zacatekSezonyB = datetime(2021,8,11)
konecSezonyB = datetime(2021,8,31)
if zacatekSezonyA <= pozadovaneDatum <= konecSezonyA:
  cenaVstupenky = 250
  celkovaCena = cenaVstupenky * pocetOsob
  print(f"Cena vstupenek je {celkovaCena} Kč.")
if zacatekSezonyB <= pozadovaneDatum <= konecSezonyB:
  cenaVstupenky = 180
  celkovaCena = cenaVstupenky * pocetOsob
  print(f"Cena vstupenek je {celkovaCena} Kč.")
else:
  print("Letní kino je v té době uzavřené.")