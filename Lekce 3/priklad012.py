class Auto:
  def pujc_auto(self):
    self.dostupnost = True
  def getInfo(self):
    if self.pujc_auto:
      print("Potvrzuji zapůjčení vozidla.")
      self.pujc_auto = False
    else:
      print("Vozidlo není k dispozici.")
    print(f"Značka a typ vozidla je {self.znackaATypVozidla} a jeho registrační značka je {self.registracniZnacka}.")
  def __init__(self, registracniZnacka, znackaATypVozidla, pocetNajetychKilometru):
    self.registracniZnacka = registracniZnacka
    self.znackaATypVozidla = znackaATypVozidla
    self.pocetNajetychKilometru = pocetNajetychKilometru
    self.dostupnost = False
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)
znacka = input("Jakou značku auta si přejete půjčit? peugeot/skoda")
if znacka == 'peugeot':
  peugeot.getInfo()
if znacka == 'skoda':
  skoda.getInfo()
else:
  print("Pozadovana znacka auta neni k dispozici.")





