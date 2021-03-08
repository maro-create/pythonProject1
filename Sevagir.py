hesla = [
  'xyz101',
  'punťa',
  'razor-blade',
  '1234',
  '12011986',
  'martin111',
  'trhnisi',
  'hokuspokus',
  'jeník15',
  'kristus-te-spasi',
  'beruška',
  'strčprstskrzkrk'
]
for heslo in hesla:
  if len(helo) > 8:
    print(heslo)


    class Auto:
      def getInfo(self):
        return f'{self.registracni_znacka},{self.typ_vozidla},{self.pocet_kilometru},{self.volne_auto}'

    def __init__(self, registracni_znacka, typ_vozidla, pocet_kilometru, volne_auto, dostupnost):
      self.registracni_znacka = registracni_znacka
      self.typ_vozidla = typ_vozidla
      self.pocet_kilometru = pocet_kilometru
      self.volne_auto = True

  auto1 = Auto()
  auto1.registracni_znacka = '4A2 3020'
  auto1.typ_vozidla = 'Peugeot 403 Cabrio'
  auto1.pocet_kilometru = '47534'
  auto1.volne_auto = True

  auto2 = Auto()
  auto2.registracni_znacka = '1P3 4747'
  auto2.typ_vozidla = 'Škoda Octavia'
  auto2.pocet_kilometru = '41253'
  auto2.volne_auto = True

  print(auto1.getInfo())
  print(auto2.getInfo())


