import numpy as np

# Zadanie 1
# a = np.array([0, 1, 2])
# b = np.array([7, 8, 9])
# print(np.dot(a, b))

# Zadanie 2
# a = np.arange(9).reshape((3, 3))
# b = np.arange(16).reshape((4, 4))
# print(a)
# print('Najniższe wartości dla kolumn macierzy 3x3: ', a.min(axis=0))
# print('Najniższe wartości dla rzędów macierzy 3x3: ', a.min(axis=1))
# print(b)
# print('Najniższe wartości dla kolumn macierzy 4x4: ', b.min(axis=0))
# print('Najniższe wartości dla rzędów macierzy 4x4: ', b.min(axis=1))

# Zadanie 3
# a = np.array([0, 1, 2])
# b = np.array([7, 8, 9])
# print(a.dot(b))

# Zadanie 4
# a = np.array([-1, 9, 20])
# b = np.array([1/2, np.pi, np.sqrt(2)])
# print(np.dot(a, b))

# Zadanie 5
# d = np.arange(6).reshape((2, 3))
# print(d)
# a = [np.sin(x) for x in d.flat]
# print(a)

# Zadanie 6
# c = np.arange(6, 12).reshape((2, 3))
# print(c)
# b = [np.cos(x) for x in c.flat]
# print(b)

# Zadanie 7
# wynik = np.asarray(a) + np.asarray(b)
# print(wynik)

# Zadanie 8
# a = np.arange(9).reshape((3, 3))
# print(a)
# for x in a:
#     print(x)

# Zadanie 9
# a = np.arange(9).reshape((3, 3))
# print(a)
# for x in a.flat:
#     print(x)

# Zadanie 10
# a = np.arange(81).reshape((9, 9))
# print(a)
# b = a.reshape((27, 3))
# print(b)
# c = a.reshape((3, 27))
# print(c)
# d = a.reshape((3, 3, 3, 3))
# print(d)

# Zadanie 11
# a = np.arange(12)
# print(a)
# b = a.reshape((3, 4))
# print(b)
# c = a.reshape((4, 3))
# print(c)
# d = a.reshape((2, 6))
# print(d)
#
# b1 = b.ravel()
# print(b1)
# c1 = c.ravel()
# print(c1)
# d1 = d.ravel()
# print(d1)