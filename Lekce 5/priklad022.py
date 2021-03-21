import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")
import pandas
character_deaths = pandas.read_csv('character-deaths.csv')
character_deaths = character_deaths.set_index('Name')

character_deaths.info()

character_deaths.loc['Hali']
print(character_deaths.loc['Hali'])

character_deaths.loc["Gevin Harlaw" : "Gillam"]
print(character_deaths.loc["Gevin Harlaw": "Gillam"])

character_deaths.loc["Gevin Harlaw":"Gillam", "Death Year"]
print(character_deaths.loc["Gevin Harlaw":"Gillam", "Death Year"])

character_deaths.loc["Gevin Harlaw":"Gillam","GoT":"DwD"]
print(character_deaths.loc["Gevin Harlaw":"Gillam","GoT":"DwD"])
