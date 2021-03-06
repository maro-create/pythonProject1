import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import pandas
teplota = pandas.read_csv('temperature.csv')
import pytemperature
teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])

teploty_den_13 = teplota[(teplota["Day"] == 13)]
teploty_den_13_bez_chyb = teploty_den_13[teploty_den_13.AvgTemperature != -99]

print(teploty_den_13_bez_chyb.groupby('Region').size())
print(teploty_den_13_bez_chyb.groupby('Region')['AvgTemperatureCelsia'].mean())
print(teploty_den_13_bez_chyb.groupby('Region')['AvgTemperatureCelsia'].max())
print(teploty_den_13_bez_chyb.groupby('Region')['AvgTemperatureCelsia'].min())