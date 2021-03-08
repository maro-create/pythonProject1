class Auto:
  def vrat_auto(self, stavTachometru, dobaVypujceni):
    if dobaVypujceni <= 7:
      celkovaCena = dobaVypujceni * 400
      return (f"Cena za zapůjčení vozidla je {celkovaCena} Kč.")
    else:
      celkovaCena = dobaVypujceni * 300
      return (f"Cena za zapůjčení vozidla je {celkovaCena} Kč.")
  def __init__(self, stavTachometru):
    self.dostupnost = True
    self.stavTachometru = stavTachometru

stavTachometru = int(input("Kolik kilometrů jste ujel?"))
autoA = Auto(stavTachometru)
dobaVypujceni = int(input("Jak dlouho jste měl auto zapůjčené?"))
print(autoA.vrat_auto(stavTachometru, dobaVypujceni))