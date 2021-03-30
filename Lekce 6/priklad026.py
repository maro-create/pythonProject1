import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

import pandas
zam_praha = pandas.read_csv('zam_praha.csv')
zam_plzen = pandas.read_csv('zam_plzeň.csv')
zam_liberec = pandas.read_csv('zam_liberec.csv')
zam_platy = pandas.read_csv('platy_2021_02.csv')

zam_praha['mesto'] = 'praha'
zam_plzen['mesto'] = 'plzen'
zam_liberec['mesto'] = 'liberec'
zamestnanci = pandas.concat([zam_praha,zam_plzen,zam_liberec], ignore_index=True)

zamestnanci.to_csv('zamestnanci.csv', index=False)
zamestnanci = pandas.read_csv('zamestnanci.csv')

platy_unor_2021 = pandas.merge(zamestnanci, zam_platy, on=['cislo_zamestnance'], how='outer')
platy_unor_2021.to_csv('platy_unor_2021.csv', index = False)
platy_unor_2021 = pandas.read_csv('platy_2021_02.csv')
print(zam_platy.shape)
print(zamestnanci.shape)
print(platy_unor_2021.shape)
print(platy_unor_2021.groupby('mesto')['plat'].mean())

byvali_zamestnanci = platy_unor_2021[platy_unor_2021['plat'].isnull()]
pocet_byvalych_zamestnancu = byvali_zamestnanci.count()
print(pocet_byvalych_zamestnancu)

jmena_byvalych_zamestnancu = byvali_zamestnanci[['jmeno','prijmeni']]
print(jmena_byvalych_zamestnancu)

jmena_byvalych_zamestnancu = jmena_byvalych_zamestnancu.to_csv('jmena_byvalych_zamestnancu.csv', index=False)





