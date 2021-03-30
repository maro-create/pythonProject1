import pandas
staty = pandas.read_json('staty.json')
gdp = pandas.read_csv('gdp.csv').dropna()

staty = staty.rename(columns={'alpha3Code': 'Country Code'})

staty_a_gdp = pandas.merge(staty, gdp, on=['Country Code'])

subregiony_gdp_2019 = staty_a_gdp.groupby('subregion')['2019'].sum()
print(subregiony_gdp_2019)

subregiony_population = staty_a_gdp.groupby('subregion')['population'].sum()
print(subregiony_population)

staty["GDP_na_obyvatele_2019"] = subregiony_gdp_2019 / subregiony_population