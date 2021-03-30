import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")
import pandas
vykazy = pandas.read_csv('vykazy.csv')
print(vykazy.groupby('project')['hours'].sum())

zamestnanci = pandas.read_csv('zamestnanci.csv')
celkovy_pocet_hodin = pandas.merge(vykazy,zamestnanci)
print(celkovy_pocet_hodin)

vykazy = vykazy.rename(columns={'emloyee_id': 'cislo_zamestnance'})
propojena_tabulka = pandas.merge(zamestnanci, vykazy, on=['cislo_zamestnance'])
print(propojena_tabulka.groupby('mesto')['hours'].sum())