import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Zerówka 1

# Zadanie 1
# x1 = [0, 1, 2, 3, 4, 5]
# y1 = [20, 10, 30, 10, 50, 0]
# x2 = [0, 1, 2, 3, 4, 5]
# y2 = [85, 60, 45, 15, 0, 0]
#
# plt.bar(x1, y1, color=['slateblue', 'aqua', 'olive', 'dodgerblue', 'lime'])
# plt.bar(x2, y2, bottom=y1, color=['teal', 'darkslategray', 'darkkhaki', 'lightsalmon'])
# plt.axhline(y = 120, xmin = 0.12, xmax = 0.96, color='g')
# plt.axis([-0.7, 5.2, 0, 150])
# plt.title('Tytuł')
# plt.savefig('plot1.png')
# plt.show()
#
# im1 = Image.open('plot.png')
# im1 = im1.convert('RGB')
# im1.save('plot.pdf')
# Zadanie 2
# df = pd.read_excel(pd.ExcelFile('mieszkania1.xlsx'), header=0)
# print(df)
# df.plot.bar(color=['green', 'red'])
# plt.text(-0.5, 75000, 'Numer indeksu', fontsize=10)
# plt.title('Wykres')
# plt.xlabel('Oś x')
# plt.ylabel('Wartości')
# plt.show()

# Zadanie 3
# df2 = pd.read_excel(pd.ExcelFile('turystyka1.xlsx'), header=0)
# print(df2)

# Zerówka 2

# Zadanie 1
# x = np.arange(-7, 7, 0.1)
# y1 = np.sin(x) * 20
# y2 = (2 * x / 5) - 2
# y3 = 7 - x
#
# plt.plot(x, y1, 'r--')
# plt.plot(x, y2, c='orange', ls='--')
# plt.plot(x, y3, 'g')
# plt.axis([-7.9, 7.9, -30, 30])
# plt.title('Tytuł ABCD')
# plt.legend(labels=['y=20*sin(x)', 'y=(2x/5)-2', 'y=7-x'], loc='lower left')
# plt.show()

# Zadanie 2
# df = pd.read_excel(pd.ExcelFile('mieszkania2.xlsx'), header=0)
# zapytanie = df[['Formy budownictwa', 'Wartość']] [df['Rok'] == 2015]
# print(zapytanie)
# plt.pie(x=zapytanie['Wartość'], labels=zapytanie['Formy budownictwa'], autopct='%.2f %%')
# plt.legend()
# plt.show()

# Zerówka 11

# Zadanie 1
# x = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec']
# y1 = [50, 42, 38, 23, 26, 30]
# y2 = [22, 34, 44, 75, 69, 50]
#
# plt.plot(x, y1, 'b--', x, y2, 'g')
# plt.grid()
# plt.title('Zyski z filmów i gier')
# plt.xlabel('Miesiąc')
# plt.ylabel('Zyski')
# plt.ylim(0, 100)
# plt.legend(labels=['Filmy', 'Gry'], loc='upper left')
# plt.show()

# Zadanie 2
# df = pd.read_excel(pd.ExcelFile('lasy11.xlsx'), header=0)
# print(df)
# df.plot.bar()
# plt.text(-0.5, 1900000, 'Numer indeksu', fontsize=10)
# plt.legend(loc='upper right')
# plt.title('Wykres')
# plt.xlabel('Rekordy')
# plt.ylabel('Wartości')
# plt.show()

# Zadanie 3
# df = pd.read_csv('sklepy11.csv', sep=';', header=None)
#
# df.iloc[3] = df.iloc[3].replace(['7 659'], '7659')
# df.iloc[3] = df.iloc[3].replace(['7 945'], '7945')
#
# df2 = pd.DataFrame({'Rodzaj': list(df.iloc[0, :]), 'Rok': list(df.iloc[1, :]), 'Jednostka': list(df.iloc[2, :]), 'Wartość': list(df.iloc[3, :])})
# df2['Wartość'] = pd.to_numeric(df2['Wartość'])
# df2['Rok'] = df2['Rok'].astype('int')
# # print(df2)
# zapytanie = df2[['Rodzaj', 'Wartość']] [df2['Rok'] == 2018]
# print(zapytanie)
#
# plt.pie(x=zapytanie['Wartość'], labels=zapytanie['Rodzaj'], autopct='%.2f %%')
# plt.legend()
# plt.title('Wykres')
# plt.savefig('11.png')
# plt.show()
# im1 = Image.open('11.png')
# im1 = im1.convert('RGB')
# im1.save('11.jpg')

# Zerówka 12

# Zadanie 1
# x = ['Hipermarkety', 'Supermarkety', 'Domy handlowe']
# y1 = [6, 33, 1]
# y2 = [8, 28, 3]
#
# X_axis = np.arange(len(x))
#
# plt.bar(X_axis - 0.2, y1, 0.4)
# plt.bar(X_axis + 0.2, y2, 0.4)
#
# plt.xticks(X_axis, x)
# plt.title('Informacje o sklepach')
# plt.legend(labels=['Rok 2016', 'Rok 2017'])
# plt.savefig('12.pdf')
# plt.show()
# https://www.geeksforgeeks.org/plotting-multiple-bar-charts-using-matplotlib-in-python/

# Zadanie 2
# df = pd.read_excel(pd.ExcelFile('lasy12.xlsx'), header=0)
# print(df)
# df.plot()
# plt.text(-0.25, 1900000, 'Numer indeksu', fontsize=10)
# plt.show()

# Zadanie 3
# df = pd.read_csv('sklepy12.csv', sep=',', header=None)
# df2 = pd.DataFrame({'Rodzaj': list(df.iloc[0, :]), 'Rok': list(df.iloc[1, :]), 'Jednostka': list(df.iloc[2, :]), 'Wartość': list(df.iloc[3, :])})
#
# df2['Rok'] = pd.to_numeric(df2['Rok'])
# df2['Wartość'] = pd.to_numeric(df2['Wartość'])
# # print(df2)
# zapytanie = df2[['Rodzaj', 'Wartość']] [df2['Rok'] == 2019]
# print(zapytanie)
#
# plt.pie(x=zapytanie['Wartość'], labels=zapytanie['Rodzaj'], autopct='%.2f %%')
# plt.legend()
# plt.title('Wykres')
# plt.show()

# Zerówka 21

# Zadanie 1
# x = ['Maj', 'Maj', 'Czerwiec']
# y1 = [3.79, 3.83, 3.95]
# y2 = [3.59, 3.75, 3.72]
# X_axis = np.arange(len(x))
#
# plt.bar(X_axis - 0.2, y1, 0.4)
# plt.bar(X_axis + 0.2, y2, 0.4)
# plt.xticks(X_axis, x)
# plt.ylim(3.0, 4.0)
# plt.legend(labels=['Ryż', 'Marchew'], loc='upper left')
# plt.title('Ceny wybranych produktów w 2019 roku')
# plt.show()

# Zadanie 2
# df = pd.read_excel(pd.ExcelFile('ceny21.xlsx'), header=0)
# print(df)
# df.plot()
# plt.text(-0.5, 2030, 'Numer indeksu', fontsize=10)
# plt.show()

# Zadanie 3
# df = pd.read_csv('sport21.csv', header=0, sep=';')
# # print(df)
# zapytanie = df[['Gry zespołowe', 'Wartość']] [df['Nazwa'] == 'WARMIŃSKO-MAZURSKIE']
# plt.pie(x=zapytanie['Wartość'], labels=zapytanie['Gry zespołowe'], autopct='%.2f %%')
# plt.title('Wykres')
# plt.legend()
# plt.show()

# Zerówka 22

# Zadanie 1
# x = [40, 29, 16, 1, 6, 8]
# y = ['Piłka nożna', 'Koszykówka', 'Siatkówka', 'Golf', 'Lekkoatletyka', 'Inne']
# explode = [0.1, 0, 0, 0, 0, 0]
#
# plt.pie(x=x, labels=y, autopct='%.f%%', explode=explode)
# plt.title('Wykres popularności sportów')
# plt.text(-1, 1, '12345', fontsize=10)
# plt.show()

# Zadanie 2
# df = pd.read_excel(pd.ExcelFile('ceny22.xlsx'), header=0)
# print(df)
#
# df.plot.bar()
# plt.show()

# Zadanie 3
# df = pd.read_csv('sport22.csv', header=0, sep=';')
# print(df)
# zapytanie = df[['Gry zespołowe', 'Wartość']] [df['Nazwa'] == 'MAŁOPOLSKIE']
# print(zapytanie)
# plt.bar(zapytanie['Gry zespołowe'], zapytanie['Wartość'], color=['green', 'blue', 'red', 'cyan'])
# plt.title('Wykres')
# plt.xlabel('Sporty')
# plt.ylabel('Wartości')
# plt.show()

# Zerówka 23

# Zadanie 1
# x = [73.9, 22.1, 4]
# y = ['Jowisz', 'Saturn', 'Neptun']
#
# plt.pie(x=x, labels=y, autopct='%.1f%%', colors=['yellow', 'orange', 'red'])
# plt.title('Masa planet')
# plt.text(-1, -1, '12345', fontsize=10)
# plt.show()

# Zadanie 2
# df = pd.read_excel(pd.ExcelFile('odpady23.xlsx'), header=0)
# print(df)
# df.plot.bar()
# plt.text(3.5, 1, 'Numer indeksu', fontsize=10)
# plt.show()

# Zadanie 3
# df = pd.read_csv('apteki23.csv', header=0, sep=';')
# print(df)
# zapytanie = df[['Rok', 'Wartosc']] [df['Nazwa'] == 'POMORSKIE']
# print(zapytanie)
# plt.plot(zapytanie['Rok'], zapytanie['Wartosc'])
# plt.show()

# Zerówka 24

# Zadanie 1
# x = np.arange(2, 31, 1)
# y = [0.167, 0.1672, 0.1673, 0.1674, 0.1675, 0.1675, 0.1677, 0.1676, 0.1674, 0.1673, 0.1672, 0.1672, 0.1675, 0.1684, 0.1685, 0.1687, 0.16873, 0.16875, 0.1689, 0.1693, 0.1687, 0.1692, 0.1691, 0.16915, 0.1692, 0.16925, 0.1694, 0.1696, 0.1695]
# plt.plot(x, y, 'r--')
# plt.ylim(0.165, 0.170)
# plt.xlim(-0.5, 32)
# plt.title('Wykres w sierpniu 2019')
# plt.text(27, 0.1686, 'CZK', fontsize=10)
# plt.grid()
# plt.show()

# Zadanie 2
# df = pd.read_excel(pd.ExcelFile('odpady24.xlsx'), header=0)
# print(df)
# plt.pie(x=df['Wartość'], labels=df['Rodzaje odpadów'], autopct='%.2f%%')
# plt.text(1.1, -1.1, 'Numer indeksu', fontsize=10)
# plt.show()

# Zadanie 3
# df = pd.read_csv('apteki24.csv', header=0, sep=';')
# print(df)
# zapytanie = df[['Nazwa', 'Wartosc']] [df['Rok'] == 2017]
# print(zapytanie)
# plt.bar(zapytanie.Nazwa, zapytanie.Wartosc)
# plt.show()

# Zerówka 31

# Zadanie 1
# x = ['Hipermarkety', 'Supermarkety', 'Domy handlowe']
# y1 = [6, 33, 1]
# y2 = [8, 28, 3]
# X_axis = np.arange(len(x))
#
# plt.bar(X_axis - 0.2, y1, 0.4)
# plt.bar(X_axis + 0.2, y2, 0.4)
# plt.xticks(X_axis, x)
# plt.title('Informacje o sklepach')
# plt.legend(labels=['Rok 2016', 'Rok 2017'])
# plt.show()

# Zadanie 2
# df = pd.read_excel(pd.ExcelFile('motocykle31.xlsx'), header=0)
# print(df)
# df.plot()
# plt.text(8, 1660000, 'Numer indeksu', fontsize=10)
# plt.show()

# Zadanie 3
# df = pd.read_excel(pd.ExcelFile('wyn31.xlsx'), header=0)
# print(df)
# zapytanie = df[['Nazwa', 'Wartosc']] [df.Rok == 2017]
# print(zapytanie)
# plt.bar(zapytanie.Nazwa, zapytanie.Wartosc)
# plt.show()