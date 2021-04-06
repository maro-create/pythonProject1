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

platy_unor_2021 = pandas.merge(zam_platy,zamestnanci)
platy_unor_2021.to_csv('platy_unor_2021.csv', index=False)

import matplotlib.pyplot as plt
zam_platydf = pandas.DataFrame(platy_unor_2021, columns=['plat','mesto'])
zam_platydf.hist(by=['mesto'], bins=[30_000, 40_000, 50_000, 60_000])
plt.show()