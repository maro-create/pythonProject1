from django.db import models

class Auto(models.Model):
  registrační_značka_automobilu = models.CharField(max_length=100)
  datum_poslední_technické_kontroly = models.DateField()
  značka_a_typ_vozidla = models.CharField(max_length=1000)
  počet_najetých_kilometrů = models.IntegerField()

class Zakaznik(models.Model):
  číslo_řidičského_průkazu = models.CharField(max_length=100)
  datum_narození = models.DateField()
  jméno_a_přijímení= models.CharField(max_length=1000)

class Vypujcka(models.Model):
  zacatek = models.DateTimeField()
  konec = models.DateTimeField()
  cena = models.IntegerField()

