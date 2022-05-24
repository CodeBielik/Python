import numpy as np
import pandas as pd

# Zadanie 1
df = pd.read_excel(pd.ExcelFile('imiona.xlsx'), header=0)
# print(df)

# Zadanie 2
# zapytanie1 = df[df.Liczba > 1000]
# print(zapytanie1)
# zapytanie2 = df[df.Imie == 'KRYSTIAN']
# print(zapytanie2)
# zapytanie3 = df.agg({'Liczba': ['sum']})
# print(zapytanie3)
# zapytanie4 = df[df.Rok < 2006].agg({'Liczba': ['sum']})
# print(zapytanie4)
# zapytanie5 = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# print(zapytanie5)
# zapytanie6 = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
# for index, group in enumerate(zapytanie6, start=1):
#     print(f"{index} {group[0]}")
#     print(f" {group[1].iloc[0]['Imie']}", end='')
#     print(f" {group[1].iloc[0]['Liczba']}")
# zapytanie7_1 = df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'), ascending=False).iloc[0]
# print("Chłopiec", zapytanie7_1)
# zapytanie7_2 = df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'), ascending=False).iloc[0]
# print("Dziewczynka", zapytanie7_2)

# Zadanie 3
df2 = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')
# print(df2)
# zapytanie1 = df2.Sprzedawca.drop_duplicates()
# print(zapytanie1)
# zapytanie2 = df2.sort_values('Utarg', ascending=False).head(5)
# print(zapytanie2)
# zapytanie3 = df2.groupby('Sprzedawca').size()
# print(zapytanie3)
# zapytanie4 = df2.groupby('Kraj').agg({'Utarg': ['sum']})
# print(zapytanie4, df2.groupby('Kraj').size())
# zapytanie5 = df2[(df2['Kraj'] == 'Polska') & (df2['Data zamowienia'] >= '2005-01-01') & (df2['Data zamowienia'] <= '2005-12-31')].agg({'Utarg':['sum']})
# print(zapytanie5)
# zapytanie6 = df2[df2['Data zamowienia'].str[:4] == '2004'].agg({'Utarg': ['mean']})
# print(zapytanie6)
# zapytanie7 = df2[((df2['Data zamowienia'] >= '2004-01-01') & (df2['Data zamowienia'] <= '2004-12-31'))]
# zapytanie7.to_csv('zamowienia_2004.csv', index=False)