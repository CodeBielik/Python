import math
import sys
# Lab 1
# Zadanie 1

# a = 10
# b = 4
# c = 77.7
# d = 20.0009
# e = 4 + 10j
# f = 900 - 0.1j
# g = 'test'
# h = 'a'
# print(a, b, c, d, e, f, g, h)
# Zadanie 2

# a = input('Podaj pierwszą liczbę: ')
# b = input('Podaj drugą liczbę: ')
# a = int(a)
# b = int(b)
#
# dodawanie = a + b
# odejmowanie = a - b
# mnozenie = a * b
# dzielenie = a / b
# dzielenie_calkowite = a // b
# reszta = a % b
# potega = a ** b
#
# print(dodawanie, odejmowanie, mnozenie, dzielenie, dzielenie_calkowite, reszta, potega)
# Zadanie 3

# a = 5
# a += 1
# a -= 1
# a *= 2
# a /= 2
# a **= 2
# a %= 9
#
# print(a)
# Zadanie 4

# a = math.e ** 10
# b = math.pow(math.log(5 + math.pow(math.sin(8), 2)), 1/6)
# c = math.floor(3.55)
# d = math.ceil(4.80)
# print(a, b, c, d)
# Zadanie 5

# imie = 'KRYSTIAN'
# nazwisko = 'BIELECKI'
# print(imie.capitalize(), nazwisko.capitalize())
# Zadanie 6

# tekst = 'I am the passenger la-la-la-la-la-la-la-la la-la-la-la-la-la-la-la la-la-la-la-la-la-la-la la-la-la-la-la-la-la-la'
# print(tekst.count('la'))
# Zadanie 7

# tekst = 'programista'
# print(tekst[1], tekst[10])
# Zadanie 8

# tekst = 'I am the passenger la-la-la-la-la-la-la-la la-la-la-la-la-la-la-la la-la-la-la-la-la-la-la la-la-la-la-la-la-la-la'
# print(tekst.split(' '))
# Zadanie 9

# a = 'tekst'
# b = 18.2
# c = 55
# print('{0:s}, {1:.2f}, {2:#x}'.format(a, b, c))


# Lab 2
# Zadanie 1

# sporty = ['skoki narciarskie', 'formuła 1', 'tenis stołowy']
# sporty.reverse()
# sporty.extend(('koszykówka', 'hokej', 'golf'))
# print(sporty)

# Zadanie 2

# slownik = {'art.':'artykuł', 'ust.':'ustęp', 'pkt':'punkt', 'lit.':'litera', 'tir.':'tiret', 'nr':'numer'}
# print(slownik)
# Zadanie 3

# gry_komputerowe = {'FPS':'Battlefield 3', 'RPG':'Wiedźmin 3', 'RTS':'World of Warcraft', 'Sports':'Fifa 14', 'Racing': 'Forza Horizon 5'}
# print(gry_komputerowe)
# Zadanie 4

# zdanie = input('Podaj zdanie: ')
# print(zdanie.count('a'))
# Zadanie 5

# sys.stdout.write('Podaj pierwszą liczbę całkowitą: ')
# a = int(sys.stdin.readline())
# sys.stdout.write('Podaj drugą liczbę całkowitą: ')
# b = int(sys.stdin.readline())
# sys.stdout.write('Podaj trzecią liczbę całkowitą: ')
# c = int(sys.stdin.readline())
# sys.stdout.write(str(a ** b + c))
# Zadanie 6

# a = int(input('Podaj pierwszą liczbę całkowitą: '))
# b = int(input('Podaj drugą liczbę całkowitą: '))
# c = int(input('Podaj trzecią liczbę całkowitą: '))
#
# if a > b:
#     if a > c:
#         print('Liczba', a, 'jest największa')
#     else:
#         print('Liczba', c, 'jest największa')
# elif b > a:
#     if b > c:
#         print('Liczba', b, 'jest największa')
#     else:
#         print('Liczba', c, 'jest największa')
# elif a == b:
#     if a & b > c:
#         print('Liczba', a, 'jest największa')
#     else:
#         print('Liczba', c, 'jest największa')
# else:
#     print('Podane liczby są równe sobie')
# Zadanie 7

# lista = [2, 5, 6, 7.5, 8.2, 9.9]
# wynik = []
# for a in lista:
#     wynik.append(a ** 2)
# print(wynik)
# Zadanie 8

# lista = []
# i = 0
# while i < 10:
#     a = int(input('Podaj ' + str(i + 1) + ' liczbę: '))
#     if a % 2 == 0:
#         lista.append(a)
#     i += 1
# print(lista)
# Zadanie 9

# try:
#     a = int(input('Podaj liczbę: '))
#     print(math.sqrt(a))
# except ValueError:
#     print('Błąd')