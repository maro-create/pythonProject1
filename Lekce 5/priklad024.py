import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import pandas
temperature = pandas.read_csv('temperature.csv')
temperature.info()
mereni_v_praze=temperature[temperature['City'] == 'Prague']
print(mereni_v_praze)
print(temperature.iloc[:5])
avg_temperature=temperature[temperature['AvgTemperature']>80]
print(avg_temperature)
avg_temperature= temperature[(temperature['AvgTemperature']<60) & (temperature['Region'] == 'Europe')]
print(avg_temperature)
avg_temperature=temperature[(temperature['AvgTemperature']>80) | (temperature['AvgTemperature']<20)]
#print(avg_temperature)

