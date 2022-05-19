import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_excel(pd.ExcelFile('imiona.xlsx'), header=0)
# df2 = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')

# Zadanie 1
# zapytanie1 = df.groupby(['Rok']).agg({'Liczba': ['sum']})
# print(zapytanie1)
# plt.plot(zapytanie1, marker='o')
# plt.xlabel('Rok')
# plt.ylabel('Liczba')
# plt.title('Liczba urodzonych dzieci dla każdego roku')
# plt.show()

# Zadanie 2
# zapytanie2 = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# print(zapytanie2)
# zapytanie2.plot.bar()
# plt.xlabel('Płeć')
# plt.ylabel('Liczba')
# plt.title('Liczba urodzonych chłopców i dziewczynek z całego zbioru')
# plt.show()

# Zadanie 3
# zapytanie3 = df[df.Rok > 2012].groupby(['Plec']).agg({'Liczba': ['sum']})
# print(zapytanie3)
# zapytanie3.plot.pie(subplots=True, autopct='%.2f %%')
# plt.title('Ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach')
# plt.show()

# Zadanie 4
# zapytanie4 = df2.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})
# print(zapytanie4)
# zapytanie4.plot.bar()
# plt.xlabel('Sprzedawcy')
# plt.ylabel('Ilość złożonych zamówień')
# plt.title('Ilość złożonych zamówień przez poszczególnych sprzedawców')
# plt.show()