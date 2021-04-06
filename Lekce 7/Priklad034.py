import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")
import pandas
import matplotlib.pyplot as plt
velikonoce = pandas.read_csv("velikonoce.csv")
pocet = [3, 7, 2, 9, 15, 15, 12, 13, 18, 22, 17, 15, 16, 16, 21, 18, 15, 15, 12, 18, 21, 18, 14, 15, 18, 22, 17, 16, 17, 15, 17, 14, 6, 6, 5]
cetnost = pandas.Series(pocet, velikonoce ['Datum'])
ax = cetnost.plot
ax = velikonoce.plot.bar()
ax.set_ylabel("Počet dnů")
ax.set_xlabel('Datum')
ax.set_title("Cetnost Velikonoc ve vybranych datumech v letech 1600 až 2100")
plt.show()

import pandas
from dateutil import easter

data = []
for rok in range(2010, 2020):
  datum = easter.easter(rok)
  naformatovany_datum = datum.strftime("%m, %d")
  data += naformatovany_datum

data = pandas.DataFrame(data, columns=["Datum"])
data = data.groupby("Datum").size()

