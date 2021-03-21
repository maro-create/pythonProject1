import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import pandas
temperature = pandas.read_csv('temperature.csv')
import pytemperature
temperature["AvgTemperatureCelsia"] = pytemperature.f2c(temperature["AvgTemperature"])

print(temperature[temperature["AvgTemperatureCelsia"] > 30])
print(temperature[(temperature["AvgTemperatureCelsia"] > 15) & (temperature["Region"] == "Europe")])
print(temperature[(temperature["AvgTemperatureCelsia"] > 30) | (temperature["AvgTemperatureCelsia"] < -10)])