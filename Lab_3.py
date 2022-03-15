import random
import math
import ciagi.arytmetyczne
import ciagi.geometryczne
# Zadanie 1
# a =[1 - x for x in range(1, 11)]
# print(a)
# b = [4 ** x for x in range(8)]
# print(b)
# c = [x for x in b if x % 2 == 0]
# print(c)

# Zadanie 2
# lista1 = [random.randint(40, 100) for x in range(10)]
# print(lista1)
# lista2 = [x for x in lista1 if x % 2 == 0]
# print(lista2)

# Zadanie 3
# produkty = {'Bułki':'sztuki', 'Cukier':'kg', 'Pączki':'sztuki', 'Kawa':'kg', 'Mleko':'l'}
# print(produkty)
# sztuki = [x for x, y in produkty.items() if y == 'sztuki' ]
# print(sztuki)

# Zadanie 4
# def trojkat_prostokatny(a, b, c):
#     lista = [a, b, c]
#     lista.sort()
#
#     if math.pow(lista[0], 2) + math.pow(lista[1], 2) == math.pow(lista[2], 2):
#         return 'Jest to trójkąt prostokątny'
#     else:
#         return 'To nie jest trójkąt prostokątny'
# print(trojkat_prostokatny(5, 3, 4))

# Zadanie 5
# def pole_trapezu(a = 1, b = 1, h = 1):
#     if a & b & h == 0:
#         return 'Nieprawidłowe dane.'
#     else:
#         return (a + b) * h / 2
# print(pole_trapezu())

# Zadanie 6
# def iloczyn_ciagu(a = 1, b = 4, ile = 10):
#     if ile == 1:
#         return a
#     else:
#         return a * math.pow(b, ile - 1)
# print(iloczyn_ciagu())

# Zadanie 7
# def iloczyn_ciagu(* liczby):
#     if len(liczby) > 3:
#         return 'Za dużo podanych liczb'
#     elif len(liczby) == 0:
#         a = 1
#         b = 4
#         ile = 10
#         return a * math.pow(b, ile - 1)
#     else:
#         return liczby[0] * math.pow(liczby[1], liczby[2] - 1)
# print(iloczyn_ciagu())

# Zadanie 8
# def zakupy(** produkty):
#     suma = 0
#     for x in produkty:
#         suma += produkty[x]
#     return len(produkty), suma
# print(zakupy(chleb = 3.50, maslo = 13, papryka = 6.50, ziemniaki = 2.98))

# Zadanie 9
# Funkcje z pliku arytmetyczne.py
# def wartosc_n_tego_wyrazu(a, n, r):
#     return a + (n - 1) * r
# def suma_ciagu_ar(a, n, r):
#     return ((2 * a + (n - 1) * r) / 2) * n
# Funkcje z pliku geometryczne.py
# def wartosc_n_tego_wyrazu(a, n, q):
#     return a * (q ** (n - 1))
# def suma_ciagu_geo(a, n, q):
#     if q != 1:
#         return a * ((1 - (q ** n)) / (1 - q))
#     else:
#         return a * n
# print(ciagi.arytmetyczne.wartosc_n_tego_wyrazu(1, 10, 2))
# print(ciagi.arytmetyczne.suma_ciagu_ar(1, 10, 2))
# print(ciagi.geometryczne.wartosc_n_tego_wyrazu(1, 10, 2))
# print(ciagi.geometryczne.suma_ciagu_geo(1, 10, 2))

# Zadanie 10
# plik = open('liczby.txt', 'w')
# for x in range(1, 101):
#     if x % 4 == 0:
#         plik.write(str(x) + ' ')
# plik.close()

# Zadanie 11
# plik = open('liczby.txt', 'r')
# print(plik.readline())
# plik.close()