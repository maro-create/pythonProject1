class Auto:
  def __init__(self, registracniZnacka, znackaATypVozidla, pocetNajetychKilometru):
    self.registracniZnacka = registracniZnacka
    self.znackaATypVozidla = znackaATypVozidla
    self.pocetNajetychKilometru = pocetNajetychKilometru
    self.dostupnost = True

autoA = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
autoB = Auto("1P3 4747", "Škoda Octavia", 41253)

