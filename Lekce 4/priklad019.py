pozadovana_mena = input('Zadej pozadovanou menu')
pozadovane_mnozstvi = int(input('Zadej pozadovane mnozstvi'))

from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = pozadovane_mnozstvi
cena_v_korunach = prevodnik.convert(pozadovana_mena, 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)


mena = input('Zadej menu')
pozadovane_mnozstvi_bitcoinu = int(input('Zadej pozadovane mnozstvi bitcoinu'))

from forex_python.bitcoin import BtcConverter
b = BtcConverter()
b.convert_btc_to_cur(pozadovane_mnozstvi_bitcoinu, mena)
print(b.convert_btc_to_cur(pozadovane_mnozstvi_bitcoinu, mena))