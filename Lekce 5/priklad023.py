import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
import pandas
vaccinations = pandas.read_csv('country_vaccinations.csv')
vaccinations.info()
pocet_ockovanych = vaccinations[vaccinations['date'] == "2021-03-10"]
print(pocet_ockovanych[['country', 'date', 'total_vaccinations']])
masivni_ockovani = vaccinations[(vaccinations['total_vaccinations'] > 1_000_000) & (vaccinations['date'] == "2021-03-10")]
print(masivni_ockovani[['country', 'date', 'total_vaccinations']])
daily_vaccinations = vaccinations[(vaccinations['daily_vaccinations'] > 100_000) | (vaccinations['daily_vaccinations'] < 100 )]
print(daily_vaccinations[['country', 'date', 'daily_vaccinations']])

info_ockovani = vaccinations[(vaccinations['date'].isin(["2021-03-10", "2021-03-11"])) & (vaccinations['country'].isin(["United Kingdom", "Finland", "Italy"]))]
print(info_ockovani[['country', 'date', 'total_vaccinations', 'daily_vaccinations']])

info_ockovani = vaccinations[(vaccinations['date'] >= "2021-03-03") & (vaccinations['date'] <= "2021-03-09") & (vaccinations['country'] == "Japan")]
print(info_ockovani[['country', 'date', 'total_vaccinations', 'daily_vaccinations']])






