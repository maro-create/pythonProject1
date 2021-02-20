from typing import Dict

sklad: Dict[str, int] = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
kodSoucastky = input('Zadej kod soucastky:')
if kodSoucastky in sklad:
  pozadovaneMnozstvi = int(input('Zadej pozadovaneMnozstvi'))
  if pozadovaneMnozstvi > sklad[kodSoucastky]:
    print("Lze prodat pouze omezené množství kusů.")
    sklad.pop(kodSoucastky)
    print(len(sklad))
  else:
    print("Poptávku lze uspokojit v plné výši.")
    sklad[kodSoucastky] -= pozadovaneMnozstvi
    print(sklad)
else:
  print("Součástka není skladem.")
