import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Zadanie 1
# x = np.arange(1, 21)
# y = 1 / x
# plt.plot(x, y, label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([1, len(x), 0, 1])
# plt.legend()
# plt.show()

# Zadanie 2
# x = np.arange(1, 21)
# y = 1 / x
# plt.plot(x, y, 'g:>', label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, len(x), 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) dla x [1, 20]')
# plt.show()

# Zadanie 3
# x = np.arange(0, 30, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x, y1, 'r', x, y2, 'g')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Wykres funkcji sin(x) i cos(x)')
# plt.legend(labels=['sin(x)', 'cos(x)'], loc='upper right')
# plt.show()

# Zadanie 4
# df = pd.read_csv('iris.csv', header=0, sep=',', decimal='.')
# x = df['sepallength']
# y = df['sepalwidth']
# s = np.abs(x - y)
# plt.scatter(x, y, c='#8c564b', s=s)
# plt.xlabel('Sepal length')
# plt.ylabel('Sepal width')
# plt.show()

# Zadanie 5
# df = pd.read_excel(pd.ExcelFile('imiona.xlsx'), header=0)
# wykres1 = df.groupby(['Plec']).agg(suma = ('Liczba', 'sum'))
# plt.subplot(1, 3, 1)
# plt.title('Wykres 1')
# plt.xlabel('Plec')
# plt.ylabel('Liczba')
# plt.bar(wykres1.index, wykres1['suma'], color=['green', 'cyan'])
# plt.subplot(1, 3, 2)
# wykres2_1 = df[df['Plec'] == 'M'].groupby(['Rok']).agg(suma = ('Liczba', 'sum'))
# wykres2_2 = df[df['Plec'] == 'K'].groupby(['Rok']).agg(suma = ('Liczba', 'sum'))
# plt.title('Wykres 2')
# plt.xlabel('Rok')
# plt.ylabel('Liczba')
# plt.plot(wykres2_1.index, wykres2_1['suma'], 'm:', wykres2_2.index, wykres2_2['suma'], 'y-')
# plt.legend(labels=['M', 'K'])
# plt.subplot(1, 3, 3)
# wykres3 = df.groupby(['Rok']).agg(suma = ('Liczba', 'sum'))
# plt.title('Wykres 3')
# plt.xlabel('Rok')
# plt.ylabel('Liczba')
# plt.bar(wykres3.index, wykres3['suma'], color='red')
# plt.subplots_adjust(wspace=0.7)
# plt.show()

# Zadanie 6
# df = pd.read_csv('zamowienia.csv', header=0, sep=';')
# dane = df.groupby(['Sprzedawca']).agg(suma = ('Utarg', 'sum'))
# explode = (0.3, 0.1, 0.2, 0, 0, 0, 0.4, 0.6, 0)
# plt.pie(x=dane['suma'], labels=dane.index, autopct='%.2f %%', shadow=True, explode=explode)
# plt.title('Procentowy udział kwot zamówień sprzedawców')
# plt.show()