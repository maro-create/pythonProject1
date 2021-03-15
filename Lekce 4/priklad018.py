class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Uchazec(Kontakt):
  def __init__(self, name, position, datum_pohovoru):
    super().__init__(name, position)
    self.datum_pohovoru = datum_pohovoru
    self.zapis_z_pohovoru = ""
  def uloz_zapis(self, zapis_z_pohovoru):
    from datetime import datetime
    datum=datetime.strptime(self.datum_pohovoru,'%d.%m.%Y')
    if datetime.now()< datum:
      return 'Pohovor jeste neprobehl'
    else:
      return 'Zapis byl ulozen.'

martin = Uchazec("Martin Přísný", "vedoucí konstrukčního oddělení", "10.3.2021")
print(martin.uloz_zapis("jjj"))
print (martin.zapis_z_pohovoru)

