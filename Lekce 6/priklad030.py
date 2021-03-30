import pandas
vykazy = pandas.read_csv('vykazy.csv')
vykazane_hodiny_za_projekty = (vykazy.groupby('project')['hours'].sum())

vykazane_hodiny_za_projekty.to_excel('vykazane_hodiny_za_projekty.xlsx')

vykazane_hodiny_za_projekty = pandas.read_excel('vykazane_hodiny_za_projekty.xlsx')