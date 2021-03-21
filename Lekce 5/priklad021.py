import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
import pandas
akcie=pandas.read_csv('twlo.csv')

print(akcie.shape)
print(akcie.iloc[-1])
print(akcie.iloc[:5])
print(akcie.head(5))
import pandas
akcie=pandas.read_csv('twlo.csv')

pocet_radku = int(akcie.shape[0])
print(pocet_radku)

prvni_zaviraci_cena = (akcie.iloc[0, 5])
print(prvni_zaviraci_cena)
posledni_zaviraci_cena = (akcie.iloc[301, 5])
print(posledni_zaviraci_cena)

procento = (posledni_zaviraci_cena-prvni_zaviraci_cena) / (prvni_zaviraci_cena/100)
print(procento)

print(akcie.iloc[:, 3])
Max = (akcie['High'].max())
Min = (akcie['Low'].min())
price_range = Max - Min
print(price_range)
