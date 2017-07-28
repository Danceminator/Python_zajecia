# -*- coding: utf-8 -*-
import random
import pymysql

'''
class Szkolenia:
    def __init__(self, nazwa, termin, cena, il_os):
        self.nazwa = nazwa
        self.termin = termin
        self.cena_n = cena_n
        self.il_os = il_os
    def obliczCalk(self):
        self.Suma_b = elf.cena_n * self.il_os)*1.23
        return self.suma_b
        
class Technologie:
    
    def __init__(self, technologia, poziom):
        super().__init__(self, nazwa, termin, cena, il_os)
        self.technologia = technologia
        self.poziom = poziom

class Trenerzy(Technologie):
    def __init__ (self, nazwa, termin, cena_n, il_os, technologia, ppoziom, imie, nazwisko, pensja):
        super().init(nazwa, termin, cena_n, il_os, technologia poziom)
        self.imie=imie
        self.nazwisko = nazwisko
        self.pensja = pensja
    def obliczCalkTrener(self):
        return self.obliczCalc() - (self.pensja*1,23)
    
    
s1= Techjnologie("Kurs Python dla dzieci", '', 2000-02-20, 20, 2000, 20, "Python 3.6", "python")
print(s1.obliczCalk())  
s2=Trenerzy("Python dla dzieci", 2000-02-20, 2000, 20, "Python 3.6", "python", "Michał", "Kruczkowski", 1000)
'''
    
    
'''szkolenie1 = Szkolenia("Kurs Python dla dzieci", '', 2000-02-20, 20, 2000, 20)
szkolenie1.obliczcalk()
szkolenie1 = Technologie ("Python", "podstawowy")
szkolenie1
szkolenie1.obliczCalk()'''

class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
    def __str__(self):
        return "Produkt: "+self.nazwa + " "+ str(self.cena)

class Oprogramowanie(Produkt):
    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__(nazwa, cena)
        self.jezyk = jezyk
        self.system = system
    def __str__(self): 
        return super().__str__()+ " "+ self.jezyk + " " + self.system
class Szkolenie(Oprogramowanie):
    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin
    def __str__(self):
        return super().__str__()+" "+self.termin
sk1 =Szkolenie("witaj Python", 1000, "Python2.8", "MacOS", "2012-02-20")
print (sk1)


class RGBKOLOR:
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B
    def __str__(self):
        return "Twój kolor: "+str(self.R)+","+str(self.G) + ", " + str(self.B) +"]"
    def __add__(self, other):
        return (self.R+other.R)/2, (self.G+other.G)/2, (self.B+other.B)/3
    
kolor1 = RGBKOLOR(100, 100, 100)
kolor2 = RGBKOLOR(100, 150, 50)
kolor3 = kolor1 + kolor2
print(kolor3)
    

class Pracownik:
    def __init__(self, imie, nazwisko, etat="Staz", pensja=500):
        self.imie = imie
        self.nazwisko = nazwisko
        self.etat = etat
        self.pensja = pensja
    def przelicz(self):
        self.pensja_b=self.pensja*1.23
        return self.pensja_b, self.pensja

class Kontrakt(Pracownik):
    def __init__(self, imie, nazwisko, etat="Staz", pensja=500):
        super().__init__(imie, nazwisko, etat, pensja)
    def zmienKontrakt(self, etat, pensja):
        self.etat =etat
        self.pensja =pensja
    def dodajNadgodziny(self, liczba):
        self.liczba  =liczba
        self.pensja = self.pensja +((self.pensja/(20*8)) *self.liczba)
    def __str__(self):
        return 'pensja pracownika '+self.imie+' ' +self.nazwisko+' wynosi z nadgodzinami: ' +str(self.pensja*1.23)+' zł brutto'
        
p1=Kontrakt("Adam", "Kowalski")
print(p1.przelicz())
p1.zmienKontrakt("Dev", 5000)
print(p1.przelicz())
p1.dodajNadgodziny(50)
print(p1.przelicz())
print(p1)