# -*- coding: utf-8 -*-
import random
'''
class PierwszaKlasa:
    a=1
    b="witaj w klasie"
    
    def __init__(self, x, y):
        self.x = x
        self.y = y    
        self.dodaj()
        self.odejmowanie()
    def dodaj(self, x, y):
        self.wynik_d = self.x + self.y
    def odejmowanie(self):
        self.wynik_0 = self.x - self.y
        return self.wynik_o
    def __str__(self):
        return ("wynik dodawania wynosi: "+(str(self.wynik_d+))+", a odejmowania: "+str(self.wynik_o))
    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    def __ge__(self, other):
        return self.wynik>other.wynik_d

obiekt1 = PierwszaKlasa()
obiekt1.witaj()
print(objekt1)

obiekt2 = PierwszaKlasa()
print(obiekt2.a)
print (obiekt2.b)
obiekt2.witaj()
'''

#p75
'''
class BMI:
    def __init__(self, imie, nazwisko, waga, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.waga = waga
        self.wzrost =wzrost
        self.obliczBMI()
    def obliczBMI(self):
        self.bmi = round(self.waga/((self.wzrost/100)**2))
    def __str__(self):
        return "BMI dla:"+self.imie+" "+self.nazwisko+" wynosi: "+str(self.bmi)

z1 =BMI("Aneta", "Gie", 77, 161)
print(z1)
'''

class Sklep:
    def __init__(self, towar, cena, ilosc):
        self.towar_klasa=towar
        self.cena_klasa=cena
        self.ilosc_klasa=ilosc
    def zaplata(self):
        self.dozaplaty=self.cena_klasa*self.ilosc_klasa
#-------------------------
zakup1=Sklep("chleb", 3.99, 4)
print(zakup1.ilosc_klasa)
print(zakup1.cena_klasa)
print(zakup1.towar_klasa)

zakup1.ilosc_klasa=5
print(zakup1.ilosc_klasa)
zakup1.zaplata()
print(zakup1.dozaplaty)


'''
class Lotto:
    def __init__(self):
        print(random.sample(range(1,50),6))
        
los1= Lotto()
los2= Lotto()
los3= Lotto()
los4= Lotto()

'''