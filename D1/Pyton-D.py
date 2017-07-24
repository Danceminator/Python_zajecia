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

#p10

'''kwota_br = float(input("podaj kwotę brutto, którą chcesz przeliczyć "))
stawka=int(input("podaj stawkę VAT "))
kwota_net = kwota_br/(1+(stawka/100))

print("kwota netto przy stawce", str(stawka)+"%", "wynosi:", round(kwota_net, 2), "zł")'''

#p11
'''
nazwa_p1 = "chleb"
nazwa_p2 = "mleko"
nazwa_p3 = "cukierek"

cena_p1 = 1.99
cena_p2=4.15
cena_p3=15.99

zamówienie_p1 = int(input("liczba chlebów: "))
zamówienie_p2= float(input("litry mleka: "))
zamówienie_p3=int(input("waga cukierków (g): "))

suma= round((cena_p1*zamówienie_p1)+(cena_p2*zamówienie_p2)+((cena_p3/1000)*(zamówienie_p3)),2)
print("Twoje zamówienie")
print("=================")
print("chleb:", zamówienie_p1, "szt.")
print("mleko:", zamówienie_p2, "l")
print("cukierki:", zamówienie_p3, "gram")
print("=================")
print("do zapłaty:", suma, "zł")
'''


a=12 +0j
b=1+(-1j)
print (a*b)

log1=True
print(type(log1))

print(bool(""), bool (0), bool("ALA"))

a = """
autor
data
wersja
"""
print(a)

#\n znak przejścia do nowej linii
b="autor\ndata\nwersja"

print(b)



#cwiczenie dodatkowe

'''imie=input("podaj imię: ")
krotnosc= int(input("podaj ile razy ma być powtórzone Twoje imię: "))

print((imie + ", ")*(krotnosc - 1)+imie+".")'''

#P22

Imie = input("podaj imię: ")
Nazwisko = input("podaj nazwisko: ")
wiek = input("podaj swój wiek: ")
Stanowisko = input("podaj stanowisko ")
Placa = input("podaj placę brutto: ")

print ((Imie +" "+Nazwisko+" (wiek: "+ wiek+ " lat) pracuje na stanowisku: "+ Stanowisko+" (pensja: "+ Placa+ " brutto).\n")*10 )