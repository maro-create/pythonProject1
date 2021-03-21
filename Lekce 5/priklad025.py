import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import pandas
temperature = pandas.read_csv('temperature.csv')
import pytemperature
temperature["AvgTemperatureCelsia"] = pytemperature.f2c(temperature["AvgTemperature"])

print(temperature.head())
print(temperature[temperature['Day'] == 13])
print(temperature[(temperature ['Day'] == 13) & (temperature['Country'] == 'US')])

nova_tabulka = temperature[(temperature ['Day'] == 13) & (temperature['Country'] == 'US')]
print(nova_tabulka[(nova_tabulka['City'] == 'Washington') & (nova_tabulka['City'] == 'Philadelphia')])

print(nova_tabulka["AvgTemperatureCelsia"].mean())
print(nova_tabulka["AvgTemperatureCelsia"].median())
print(nova_tabulka["AvgTemperatureCelsia"].var())