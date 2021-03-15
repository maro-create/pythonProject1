from faker import Faker
generator_falesnych_dat = Faker("cs_CZ")

class Balik:
  def get_info(self):
    print(f"Příjemce balíku: {self.name}")
    print(f"Balík doručte na adresu: {self.address}")

  def __init__(self, name, address):
    self.name = name
    self.address = address

zasilka = Balik(generator_falesnych_dat.name(), generator_falesnych_dat.address())
print(zasilka.get_info())

from faker import Faker
generator_falesnych_dat = Faker(['cs_CZ', 'sk_SK'])

class Balik:
  def get_info(self):
    print(f"Příjemce balíku: {self.name}")
    print(f"Balík doručte na adresu: {self.address}")

  def __init__(self, name, address):
    self.name = name
    self.address = address

zasilka = Balik(generator_falesnych_dat.name(), generator_falesnych_dat.address())
print(zasilka.get_info())