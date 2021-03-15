
class Uzivatel:
  def __init__(self, uzivatelske_jmeno):
    self.uzivatelske_jmeno = uzivatelske_jmeno
    self.delka_sledovani = 0
  def pripocti_zhlednuti(self, celkova_delka):
    self.delka_sledovani += celkova_delka
    return f" Celkova delka sledovani u uzivatele {self.uzivatelske_jmeno} je {self.delka_sledovani} minut."

class Polozka:
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka
  def get_celkova_delka(self):
    celkova_delka = self.delka
    return int(celkova_delka)

class Serial(Polozka):
  def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
    super().__init__(nazev, zanr)
    self.pocet_epizod = pocet_epizod
    self.delka_epizody = delka_epizody
  def get_celkova_delka(self):
    celkova_delka = int(self.delka_epizody) * int(self.pocet_epizod)
    return int(celkova_delka)

film = Film("Past", "horor", "34")
serial = Serial("Pratele", "sitcom", "2", "22")

martin = Uzivatel("Martin")
print(martin.pripocti_zhlednuti(film.get_celkova_delka()))
print(martin.pripocti_zhlednuti(serial.get_celkova_delka()))


