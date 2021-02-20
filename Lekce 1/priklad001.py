baliky = {
  "B541X": True,
  "B547X": False,
  "B251X": False,
  "B501X": True,
  "B947X": False,
}
kodBaliku = input('Zadej cislo baliku:')
if baliky[kodBaliku] is True:
  print('Balík byl předán kurýrovi')
else:
  print('Balík zatím nebyl předán kurýrovi')




