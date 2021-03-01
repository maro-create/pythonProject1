def criteria(odvetvi,zeme,obrat,konference=False,newsletter=False):
  celkoveBody = 0
  if odvetvi == "automotive":
    celkoveBody += 3
  if odvetvi == "retail":
    celkoveBody += 2
  if obrat > 10000000 and obrat < 1000000000:
    celkoveBody += 3
  if obrat > 1000000000:
    celkoveBody += 1
  if zeme == "Cesko" or zeme == "Slovensko":
    celkoveBody += 2
  if zeme == "Nemecko" or zeme == "Francie":
    celkoveBody += 1
  if konference:
    celkoveBody += 1
  if newsletter:
    celkoveBody += 1
  return celkoveBody
odvetvi = input("Zadejte odvetvi: ")
zeme = input("Zadejte zemi: ")
obrat = int(input("Zadejte obrat: "))
konference = input("Potvrdte, jestli jste se ucastnil(a) konference. Pokud ne, nechte polem prazdne: ")
newsletter = input("Potvrdte, jestli odebirate newsletter. Pokud ne, nechte pole prazdne: ")
celkoveBody = criteria(odvetvi, zeme, obrat, konference, newsletter)
if celkoveBody < 5:
  print("Sance na ziskani zakazky je mala.")
elif celkoveBody < 8:
  print("Sance na ziskani zakazky je stredni.")
else:
  print("Sance na ziskani zakazky je vysoka.")