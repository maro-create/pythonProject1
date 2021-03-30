import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")
import pandas
staty = pandas.read_json('staty.json')
gdp = pandas.read_csv('gdp.csv')

evropske_staty = staty[staty['region'] == "Europe"]
print(evropske_staty)
print(evropske_staty.groupby('subregion')['name'].count())
print(evropske_staty.groupby('subregion')['population'].sum())

