# -*- coding: utf-8 -*-
'''napis="zawartość"
print(napis.capitalize())

print(napis.count("a"))

print(napis.islower())
print(napis.index("a"))
print(napis.replace("a", "i"))
print(napis.replace("zawa", "otwa"))



tab=[]
tab.append(1)
tab.append("abc")
tab.append("A")
tab.append(napis)

print(tab[0], tab[1], tab[3])


oceny = []
a=input("podaj ocenę: ")
oceny.append(a)
oceny.append(input("podaj drugą ocenę: "))
print(oceny[0], oceny[1])
oceny[0]='5'
print(oceny[0], oceny[1])
'''
'''oceny2=[2,4,5, 5, 6, 8, 9, 10]
print(oceny2[0], oceny2[1])

listalista=[[1,3,6], ["nocny", [0,1,2]]]

print(listalista[1][1][2])

print(oceny2[3:5])
# co któryś podwójny dwukropek

print(oceny2[3::2])
print(oceny2[3:])

print(len(oceny2))

tekst= "aneta"
lista=list(tekst)
print(lista)
lista[2]= 't'
print(lista)

print(lista.pop(2))
print(lista)
print(lista[2], len (lista))


jedzenie=['mleko', 'chleb', 'parówki', 'masło', 'jabłka']
ceny=[3, 4, 2, 6, 2]'''
'''print (jedzenie+ceny)

print([jedzenie],[ceny])'''

'''print( "nazwa\t\tcena")
print( jedzenie[0], "\t\t", ceny[0])
print( jedzenie[1], "\t\t", ceny[1])
print( jedzenie[2], "\t\t", ceny[2])
print( jedzenie[3], "\t\t", ceny[3])
print( jedzenie[4], "\t\t", ceny[4])


krotka = ("a", 2, 13.5)
krotka2="a","b","c"
print (krotka)
print (krotka2)

data=(("mleko", "chleb", "cukierki"), ("01-02-2018", "03-03-2018", "01-05-2018" ))
print(data)
print(data[0][0] + "\t\t"+(data[1][0]))
print(data[0][1] + "\t\t"+(data[1][1]))
print(data[0][2] + "\t"+(data[1][2]))'''

tabelka=[("Kowal",("Nowak", "-COS")), ("1987-02-15", "1985-02-14"), ["dev", "dev"]]
tabelka[2][0]="admin"
print(tabelka[0][0], tabelka[1][0], tabelka[2][0])
print(tabelka[0][1][0] + tabelka[0][1][1], tabelka[1][1], tabelka[2][1])