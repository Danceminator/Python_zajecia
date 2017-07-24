# -*- coding: utf-8 -*-
# komentarz jednowierszowy
zmienna1 = 5
zmienna2 = 5.3
'''
poczatek komentarza blokowego
tekst = "to jest moj tekst"
tekst2 = 'to jest inny tekst'
literki = 'a'
''' 
witaj = "I'm Aneta"
zmienna3 = 2 + 5

Zmienna3 = 'liczba'
nowa_zmienna = zmienna3 + 5

print (zmienna1)
print (zmienna1, zmienna2)
print (witaj)
print (zmienna3, Zmienna3)
print (nowa_zmienna)
print ("hi, " + witaj)
print ("hi, " + witaj + " - nice to meet you!")


print ("przed zmiana", Zmienna3)

Zmienna3 = 3.14
print ("po zmianie", Zmienna3)

del zmienna1
# print (zmienna1) (pokazuje ze blad)

#P1
a=1
b=2.4
c='w1'
print (a, b, c)

#p2


a=2.1
b="abc"
c='0'
print (a, b, c)

#P3
'''Imie = input("podaj imię ")
Nazwisko = input("podaj nazwisko ")
Rok_urodzenia = input("podaj rok urodzenia ")
Stanowisko = input("podaj stanowisko ")
Placa = input("podaj placę brutto ")

print (Imie, Nazwisko, Rok_urodzenia, Stanowisko, Placa)'''


#P4

'''pi=3.14
#int() - rzutuje na integer
# input() - czyta wartość z klawiatury - string!

promien = int(input ("podaj promien kola "))
pole_kola=pi*promien*promien

#podstawa **wykladnik
print (pole_kola, pi*(promien**2))

# zwraca typ wartości zmiennej

print (type(pole_kola))'''
print(type(21j))

dluga = 3147483647
print(type(dluga))
'''dluga2 = 32L (do sprawdzenia komenda)
print(type(dluga2))'''

print(3/2, 3//2)

#(round zaokrągla matematycznie)

print(round(3/2, 3))

print(round(1.3), round(1.5), round(1.6))

print(round(-1.3), round(-1.5), round(-1.6))

# int() rzutuje na dół
print(int(1.3), int(1.5), int(1.6))

print(int(-1.3), int(-1.5), int(1.6))
