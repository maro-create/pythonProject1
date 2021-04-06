import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
twilio = pandas.read_csv('twlo.csv.')
import matplotlib.pyplot as plt

twilio = pandas.read_csv("twlo.csv")

twiliodf = pandas.DataFrame(twilio, columns=['Close','Date'])

ax = twiliodf.plot()
ax.set_ylabel("Cena v dolarech")
ax.set_xlabel("Datum")
ax.set_title("Vyvoj zaviraci ceny akcie")
plt.show()
twiliodf.plot()
plt.show()
