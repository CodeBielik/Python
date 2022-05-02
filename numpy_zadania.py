import numpy as np

# Zadanie 1
# a = np.arange(0, 3 * 15, 3)
# print(a)

# Zadanie 2
# lista = np.array([1.1, 4.6, 7.7])
# c = lista.astype('int64')
# print(c)

# Zadanie 3
# def funkcja(n):
#     return np.arange(1, (n * n) + 1).reshape((n, n))
# print(funkcja(3))

# Zadanie 4
# def generuj(podstawa, ilosc):
#     return np.logspace(1, ilosc, num = ilosc, base = podstawa, dtype='int64')
# print(generuj(2, 4))

# Zadanie 5
# def funkcja(dlugosc):
#     return np.diag(np.array(np.flipud([x for x in range(dlugosc)])))
# print(funkcja(5))

# Zadanie 6
# macierz = np.empty((8, 8), dtype = 'U1')
# miasto3 = np.array(list('WARSZAWA'))
# np.fill_diagonal(macierz, miasto3)
# macierz[7, 0] = 'G'
# macierz[6, 0] = 'D'
# macierz[5, 0] = 'A'
# macierz[4, 0] = 'Ń'
# macierz[3, 0] = 'S'
# macierz[2, 0] = 'K'
# macierz[0, 2] = 'R'
# macierz[0, 3] = 'A'
# macierz[0, 4] = 'D'
# macierz[0, 5] = 'O'
# macierz[0, 6] = 'M'
# print(macierz)

# Zadanie 7
# def funkcja(n):
#     lista1 = [x for x in range(-n + 1, 0)]
#     lista1.reverse()
#     lista2 = [x for x in range(1, n)]
#     a = 2 * np.eye(n, dtype='int64')
#     suma = a
#     for x, i in zip(lista1, range(2, n + 1)):
#         suma += (2 * i) * np.eye(n, k=x, dtype='int64')
#     for x, i in zip(lista2, range(2, n + 1)):
#         suma += (2 * i) * np.eye(n, k=x, dtype='int64')
#     return suma
# print(funkcja(4))

# Zadanie 8
# def funkcja(tablica, kierunek):
#     if(kierunek == 'horizontal'):
#         try:
#             return np.hsplit(tablica, 2)
#         except ValueError:
#             return 'Liczba kolumn nie pozwala na wykonanie operacji'
#     elif(kierunek == 'vertical'):
#         try:
#             return np.vsplit(tablica, 2)
#         except ValueError:
#             return 'Liczba wierszy nie pozwala na wykonanie operacji'
#     else:
#         return 'Dostępne kierunki to: \nhorizontal,\nvertical'
# print(funkcja(np.array([[1, 2, 3], [4, 5, 6], [3, 5, 7], [6, 7, 0]]), 'vertical'))

# Zadanie 9
# a = np.arange(25).reshape(5, 5)
# poprzedni = 0
# kolejny = 1
# for x in range(2, 25):
#     obecny = poprzedni + kolejny
#     a[x // 5][x % 5] = obecny
#     poprzedni = kolejny
#     kolejny = obecny
# print(a)