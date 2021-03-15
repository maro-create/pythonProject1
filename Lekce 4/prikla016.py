class Polozka:
  def getInfo(self):
   return f'nazev: {self.nazev}, zanr: {self.zanr}.'
  def __init__(self, nazev,zanr):
    self.nazev = nazev
    self.zanr = zanr
class Film(Polozka):
    def __init__(self,nazev,zanr,delka):
        super().__init__(nazev,zanr)
        self.delka = delka
    def getInfo(self):
        return super().getInfo() + f'Delka filmu je {self.delka}.'
class Serial(Polozka):
    def __init__(self,nazev,zanr,pocet_epizod, delka_epizody):
        super().__init__(nazev,zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody
    def getInfo(self):
        super().getInfo() + f'Pocet epizod je {self.pocet_epizod} a delka epizody je {self.delka_epizody}minut.'
polozka = Polozka('Past','horor')
print(polozka.getInfo())
film = Film('Past','horor','1:30')
print(film.getInfo())
serial = Serial('Pratele','sitcom','236','22')
print(serial.getInfo())


