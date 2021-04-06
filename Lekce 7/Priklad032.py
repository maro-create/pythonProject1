import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
import pandas
zam_platy = pandas.read_csv('platy_2021_02.csv')
import matplotlib.pyplot as plt
zam_platydf = pandas.DataFrame(zam_platy, columns=['plat'])
zam_platydf.hist(bins=[30_000, 35_000, 40_000, 50_000, 55_000, 60_000])
plt.show()

