import pandas
from dateutil import easter

data = []
for rok in range(2010, 2020):
  datum = easter.easter(rok)
  naformatovany_datum = datum.strftime("%m, %d")
  data += naformatovany_datum

data = pandas.DataFrame(data, columns=["Datum"])
data = data.groupby("Datum").size()