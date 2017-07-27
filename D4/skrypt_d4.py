# -*- coding: utf-8 -*-
import random

#75
'''
def srednia(*arg):
    suma=0
    sr=0
    for v in arg:
        suma += v
        sr =suma/len(arg)
    return sr
print("srednia wynosi:", srednia(5, 6, 3.5, 3))
'''
'''
znak = input("podaj znak do wykresu: ")

def wykr(znak ="*"):
        L=[]
        D=["0", "1", "2", "3", "4", "5", "6", "7", "8","9"]
        i= "a"
        decyzja = input("czy chcesz zeby wartości wykresu były typowane losowo (t/n): ")
        x= input("podaj liczbę linijek wykresu: ")
        if (decyzja == "t"):
                i=0
                while (i <int(x)):
                        L.append(random.randint(0,10))
                        i +=1
        else:
                while(i !=""):
                        i=input("wprowadź dowolną cyfrę do wykresu: ")
                        if (i in D):
                                L.append(int(i))
                        elif(i ==""):
                                print("wprowadzanie liczb zakończone")
                        else:
                                print("wprowadzony znak nie jest cyfrą")
                
        for v in L:
                print(v, v*znak)

wykr(znak ="*")
'''

'''
def wykres(d, znak = "*", ilosc = 10):
	i = 0
	Wartosci = []
	if (d == "M"):
    	while(i < ilosc):
        	Wartosci.append(int(input("Podaj kolenjną wartość: ")))
        	i += 1       	 
	elif (d == "A"):
    	while(i < ilosc):
        	Wartosci.append(random.randint(0,9))
        	i += 1	 
	for v in Wartosci:
    	print(znak * v)
          	 
def menu():
	znak_menu = input("podaj znak: ")
	ilosc_menu = input("podaj ilosc: ")  	 
	decyzja = input("Wybierz opcję: (A)-auto, (M)-manual")
	if (znak == "" and ilosc != ""):
    	wykres(d=decyzja, ilosc = int(ilosc_menu))
	elif(znak != "" and ilosc == ""):
    	wykres(d=decyzja, znak = znak_menu)
	elif (znak != "" and ilosc != ""):
    	wykres(decyzja,znak_menu,int(ilosc_menu))
	else:
    	wykres(d=decyzja)

menu()
'''

'''
def HTML_export(napis="napis", color="black", size ="12px", weight = "5"):
    return '<span style ="color: '+color+' ;font-size:'+size+'; font-weight:'+weight+'">'+napis+'</span>'
print(HTML_export("witaj w HTML"))
'''
'''
kolor="black"
licznik =0
licznikb =0
licznikw =0
def naprzemian():
    global kolor
    global licznik
    global licznikb
    global licznikw
    licznik +=1
    if(kolor == "white"):
        kolor="black"
        licznikb +=1
    elif(kolor == "black"):
        kolor = "white"
        licznikw +=1
    return kolor

print (naprzemian())
print (naprzemian())
print (naprzemian())
print (naprzemian())
print (naprzemian())

print(licznik)
print("black wystąpił", licznikb, "razy")
print("white wystąpił", licznikw, "razy")
'''
'''
def dodawanie(a,b):
    return a+b
def odejmowanie(x,y):
    return x-y

def pytanie():
    decyzja=input("dodawanie - podaj d, odejmowanie - podaj o, wyjście - w: ")
    while (decyzja != "w"):
        if(decyzja =="d"):
            print(dodawanie(float(input("wprowadź liczbę do dodania: ")), float(input("wprowadź liczbę do dodania: "))))
            decyzja = 'c'
        elif(decyzja =="o"):
            print(odejmowanie(float(input("wprowadź odjemną: ")), float(input("wprowadź odjemnik: "))))
            decyzja = "c"
        else:
            decyzja=input("dodawanie - podaj d, odejmowanie - podaj o, wyjście - w: ")

pytanie()

'''

def wprowadz():
    Tab=[]
    i="t"
    print("wprowadź elementy *eter)- koniec wprowadzania")
    while (i !=""):
        i=input(" ")
        if(i != ""):
            while True:
                try:
                    i=float(i)
                    break
                except ValueError:
                    print("błąd podaj liczbę")
                    i=input(" ")
            Tab.append(i)
        elif(i ==""):
            print("wprowadzanie zakończone")
            return Tab
        
def wypiszpow5(limit, lista):
    print("firlruję elementy większe od", limit)
    suma=0
    for v in lista:
        if(v >limit):
            print(v,end=" ")
            suma +=v
    print ("Suma: ", suma)
    
wypiszpow5(int(input("podaj imit odcięcia: ")), wprowadz())

