'''
from pakiet.modul1 import *

print (a)
info()
a=Nowa()
a.witaj()
# albo do poszczegolnych komend jezeli zaimportujemy przez "import pakiet.modul1

'''

F = open("plik.txt", "w")

print(F.closed, F.mode, F.name)

F.write("poczatek pliku")
F.write("Kolejny napis")
F.writelines (["\n linia", "\n4 linia", "\n5 linia"])

F.close()
print(F.closed, F.mode, F.name)

G = open("plik.txt","r")
print(G.read())

