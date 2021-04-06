import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import matplotlib.pyplot as plt
import pandas
teplota = pandas.read_csv('temperature.csv')

vybrane_mesta = teplota[teplota["City"].isin(["Helsinki", "Miami Beach", "Tokyo"])]
vybrane_mesta.to_csv('vybrane_mesta.csv', index=False)

teploty_ve_vybranych_mestech = vybrane_mesta[["City", "AvgTemperature"]]
teploty_ve_vybranych_mestech.to_csv('teploty_ve_vybranych_mestech.csv', index=False)
teploty_ve_vybranych_mestech.plot(kind='box')
plt.show()django-admin startproject czechitas