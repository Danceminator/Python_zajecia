# -*- coding: utf-8 -*-
import random

'''
x=int(input("Wpisz dowolną liczbę, króra ma być potęgowana: "))
y=int(input("Wpisz potęgę, do której chcesz podnieść liczbę: "))
i=1
res=1
while (i <= y):
    res *= x
    i+=1
print(res)
print("wynik potęgowania to: "+str(res))

'''
'''
n=int(input("Wpisz liczbę wyrazów ciągu (całkowita): "))
a1=float(input("Wpisz a1: "))
q=float(input("Wpisz q: "))
i=0
S=0
L=[]
while(i < n):
    S += a1*(q**i)
    L.append(a1*(pow(q, i)))
    i+=1

print("%10s %15.2f" % ("Suma:",S))
#s - string, f - float  w nawiasie po procencie jest to co ma być zawartością i przechowuje inta itd.
print("%10s %10s" %("Składowe:",""), end="")
# zarazerwowane 10 miejsc na string spacja 10 miejsc na string po procencie w nawiasie 

# do zaprezentowania składników - rodzaj wyświetlenia:
for v in L:
    print("%-5.2f" % (v), end=" ")
    

print("dodatkowe")
print("suma wynosi: ", S)
print(a1*(pow(q, n-1)))
print(L)
'''   
'''    
ciag=input("Wpisz ciąg znaków: ")
szuk=input("Wpisz znak, który mam znaleźć: ")
i=0
licznik=0
while (i<len(ciag)):
    if(ciag[i]==szuk):
        print("na miejscu:", i+1, "znajduje się litera",ciag[i])
        licznik += 1
    i +=1
print("szukany znak znaleziono", licznik, "razy")
'''
'''    
ciag=input("Wpisz ciąg znaków: ")
szuk=input("Wpisz ciąg, który mam znaleźć: ")
i=0
licznik=0
while (i<len(ciag)):
    if(ciag[i: i+len(szuk)]==szuk):
        print("na miejscu:", i+1, "znajduje się wyrażenie",szuk)
        licznik +=1
    i +=1
print("szukany ciąg znaleziono: ", licznik, "razy")
'''
'''
ciag=input("Wpisz ciąg znaków: ")
szuk=input("Wpisz ciąg, który mam znaleźć: ")
i=0
licznik=0
while (i<len(ciag)):
    if(ciag[i: i+len(szuk)]==szuk):
        print("na miejscu:", i+1, "znajduje się wyrażenie",szuk)
        licznik +=1
        i=i+len(szuk)
    else:
        i +=1
print("szukany ciąg znaleziono: ", licznik, "razy")
'''
'''
dol=int(input("wprowadź dolny zakres temperatury w stopniach F: "))
gor=int(input("wprowadź górny zakres temperatury w stopniach F: "))
step=int(input("wprowadź skok skali temperatury w liczbach naturalnych: "))
C=range(dol, gor, step)
i=len(C)-1
print("%7s | %7s" % ("C","F"))
while(i >=0):
    if(C[i]==0):
        print("-------------------------------------")
        print("%7i | %+7.1f" % (C[i], (C[i]*1.8)+32))
        print("-------------------------------------")
    else:
        print("%+7i | %+7.1f" % (C[i], (C[i]*1.8)+32))
    i -=1

'''
'''
start=int(input("wprowadź dolny zakres temperatury w stopniach F: "))
stop=int(input("wprowadź górny zakres temperatury w stopniach F: "))
step=int(input("wprowadź skok skali temperatury w liczbach naturalnych: "))
if((stop-start) % step==0):
   C=range(start, stop+step, step)
else:
   C=range(start, stop, step)
i=len(C)-1
print("%7s | %7s" % ("C","F"))
while(i >=0):
   if(C[i]==0):
      print("-------------------------------------")
      print("%7i | %+7.1f" % (C[i], (C[i]*1.8)+32))
      print("-------------------------------------")
   else:
      print("%+7i | %+7.1f" % (C[i], (C[i]*1.8)+32))
   i -=1
   '''

# p68

D=['3','3.5','4','4.5','5']
i="a"
O=[]
while (i !=""):
    i=input("wprowadź ocenę: ")
    if (i in D):
        O.append(float(i))
    elif(i ==""):
        print("wprowadzanie ocen zakończone")
        print ("oceny:",O)
    else:
        print("ocena nieoprawna")
sr=0
if (len(O) !=0):
    for i in O:
        sr += i
    print("Średnia ocen", round(sr/len(O),2))
else:
    print("nie wprowadzono żadnych ocen!")

 