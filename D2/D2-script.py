# -*- coding: utf-8 -*-
import random
#dzień 2
'''literki = {'a':'A' , 'b':'B' , 'c':'C'}
print(literki)
print(len(literki))
print(literki['a'], literki['b'])

literki['c']="napis"
print(literki ['c'])
print(literki.keys(), literki.values())
literki ['d']='D'
del literki ['c']
print(literki)
literki [2] = "abc"
print (literki)
to_str = str(literki)
print(to_str[0], to_str[1])'''
#p44
'''key1=input('Podaj liczbę(1-5) zapispaną słownie: ')
to_dec={ 'jeden':1, 'dwa': 2, 'trzy':3, 'cztery':4, 'pięć':5, 'piec':5}
print (key1.capitalize() + " w postaci liczby dziesiętnej to: "+str(to_dec[key1]))


key1=input('Podaj liczbę(1-5) zamispaną słownie: ')
to_rom={ 'jeden': "I", 'dwa': "II", 'trzy':"III", 'cztery':"IV", 'pięć':"V", 'piec':'V'}
print (key1.capitalize()+"w postaci liczby rzymskiej to:"+(to_rom[key1]))'''

#pkolejne
'''key1=input('Podaj liczbę(1-5) zapispaną słownie: ')
to_dec={ 'jeden':1, 'dwa': 2, 'trzy':3, 'cztery':4, 'pięć':5, 'piec':5}
to_rom={ 1: "I", 2: "II", 3:"III", 4:"IV", 5:"V"}

print (key1.capitalize() + " w postaci liczby dziesiętnej to: "+str(to_dec[key1])+",a w postaci rzymskiej: "+str(to_rom[to_dec[key1]]))
'''
#p48
'''nazwa= input("Jaki produkt chcesz zamówić? (chleb, bułki, bagietka):")
ilosc=int(input("podaj ilość wybranego produktu:"))
nazwa_t = {'chleb':'0x1', 'bułki':'0x2', 'bagietka':'0x3'}
cena_n = {"0x1":1.99, "0x2":3.99, "0x3":5.99}

print("Do zapłaty: "+str(round(cena_n[nazwa_t[nazwa]]*ilosc,2)) +" zł (" +str(round((cena_n[nazwa_t[nazwa]]*ilosc)*1.23,2)) + "zł brutto.)")'''

#kolejne

'''kształty=set(['kolo', 'kwadrat', 'trójkąt'])
kształty.add('okrag')
kształty.discard('kolo')
print(kształty)
okragle=set(['okrag'])
print(len(kształty), len(okragle))

print(kształty.issubset(okragle))
print(kształty.issuperset(okragle))

"#operacje na zbiorach
print (kształty)
print (okragle)
print (kształty | okragle)
print (kształty & okragle)
print (kształty - okragle)
print (kształty ^ okragle)'''

'''los1=random.randint(1,49)

print(los1)

S = set()

S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))

L=list(S)
print (L[:6])
'''
# instrukcja warunkowa if

'''a= int(input("podaj liczbę: "))
if(a%2==0):
    print("liczba "+str(a)+' jest parzysta')
    if (a>=10):
        print('liczba '+str(a)+' jest większa równa 10')
    else:
        print('liczba '+str(a)+' jest mniejsza od 10')
     
else:
    print('liczba '+str(a)+' jest nieparzysta')
    
print ("jestem już za instrukcją if")'''

      
'''elif(a>10): 
print ("liczba "+str(a)+' jest wieksza od zera')'''


# p53

'''    print(bool(0)
if (bool(1)):
    print(bool(1)
if (bool(2)):
    print(bool(2)
if (bool(3)):
    print(bool(3)
if (bool(4)):
print (bool(4))'''

#P54
'''lista =[1,2,3,4,5,6,7,8,9]
index = int(input("Podaj który element chcesz wyświetlić: "))
             
if(index >=0 and index <=(len(lista)-1)):
    print('index is ok')
    print (lista[index])
else:
    print ('out of rage')
if (lista[0]>0 and lista[1]>0):
    print ("oba elementy większe od zera")
elif (lista[0]>0 and lista[1]<0):
    print ("pierwszy element większy od zera a drugi mniejszy od zera")
elif (lista[0]<0 and lista[1]>0):
    print ("pierwszy element mniejszy od zera a drugi większy od zera")    
else:
    print ("oba elementy są mniejsze od zera") '''    

'''A=set([1,2,3,4,])
B= set([1,2,5,4])
        
if (A==B):
    print ("zbiory są równe")
elif (A.issubset(B)):
    print("A jest podzbiorem B")
elif (A.issuperset(B)):
    print("B jest podzbiorem A")
else:
    print("zbiory są różne")'''

'''
lista =[1,2,3,4,5,6,7,8,9]

i=len(lista)-1
while (i>=0):
        if(lista[i]%2==0):
                print ("index: "+str(i)+"\t Wartosć: "+str(lista[i]))
        i-=1
else:
        print("jestem w else")
print ('poza pętlą')

#która z liczb jest większa i o ile? wyrażenie trójargumentowe

a = 20
b=15
print(" a jest większe od b o: "+str(a-b)) if (a >=b) else print("b jest większe od a o: "+str(b-a))
'''
'''
lista =[1,2,3,4,5,6,7,8,9]
for var in lista:
        print("Wartość: "+str(var))
        
lista.append(15)

for index in enumerate(lista):
        print("Index: "+str(index) + "\t Wartość: "+str(var))
'''

'''
SL={'a':1, 'b':2, 'c':3}
for k in SL:
        if (SL[k] >=1):
                print( k, SL[k])
                
s1=range(100)
print (s1)
for i in s1:
        print(i)
for j in range(15, 25):
        print(j)

for k in range(0,20,2):
        print ("wynik: %-4i%-6i%-8i" % (k, k**2, k**3))
        
for x in range(5, 100, 10):
        print("pierwiastkiem liczby %2i jest %5.3f" % (x, x**0.5, ))
'''


#p57 DO POPRAWY!!!!!

'''sklep_produkty ={"monitor":1, "klawiatura":2, "mysz": 3}
produkty_cena={1:1500, 2:400, 3: 200}
produkty_dost={1:5, 2:5, 3:15}
suma =0
i="t"
while (i=="t"):
    zamowienie= input("wybierz towar: ")
    zam_ilość=int(input("podaj liczbę zamaiwianego produktu: "))     
    for k in sklep_produkty:
        if(zamowienie in sklep_produkty.keys()):
            if(zamowienie == k and produkty_dost[sklep_produkty[k]]>= zamowienie_ilosc):
                print ("produkt dostępny: " +k)
                print ("zamawiasz: " +str(zam_ilość) +"szt")
                suma +=zam_ilość*produkty_cena[sklep_produkty[k]]
            elif(zamowienie == k and produkty_dost [sklep_produkty[k]] <zam_ilość):
                print ("produkt dostępny: " +k)
                print ("zamawiasz: " +str(produkty_dost)[sklep_produkty[k]] +"szt")
        else:
            print ("brak produktu w sklepie")
            break
        i=input("czy chcesz zamawiać dalej? t/n)")
    print("do zapłaty: "+str(suma))
'''

#P57 od Michała

'''
sklep_produkty = {"monitor": 1, "klawiatura": 2, "mysz": 3}
produkty_cena = {1: 1500, 2: 400, 3: 200}
produkty_dostepnosc = {1: 5, 2: 5, 3: 15}
suma = 0
i = "t"
while(i == "t"):
    zamowienie = input("Wybierz towar: ")
    zamowienie_ilosc = int(input("Podaj ilosc zamawianego produktu: "))
    if (zamowienie in sklep_produkty.keys()):
        if(produkty_dostepnosc[sklep_produkty[zamowienie]] >= zamowienie_ilosc):
            print("Produkt dostępny: " + zamowienie)
            print("Zamawiasz: " + str(zamowienie_ilosc) + ' szt')
            suma += zamowienie_ilosc* produkty_cena[sklep_produkty[zamowienie]]    
        elif(produkty_dostepnosc[sklep_produkty[k]] < zamowienie_ilosc):
            print("Produkt dostępny: " + zamowienie)
            print("Jest dostępne tylko: " + str(produkty_dostepnosc[sklep_produkty[k]]) + ' szt')   	 
    else:
        print("Brak produktu w sklepie")
    i = input("czy chcesz zamawiać dalej? (t/n)")
print("Do zapłaty: "+ str(suma))
'''
'''
ciag= list(input("wprowadź ciąg dowolnych znaków: "))
print(ciag)
res=[]
i=0
print(len(ciag))
to_dec={"0":"zero", "1":"jeden", "2":"dwa", "3":"trzy", "4":"cztery", "5":"pięć", "6":"sześć", "7":"siedem", "8":"osiem", "9":"dziewiec"}
while (i >= len(ciag)):
        t = ciag[i]
        if (ord(t) <= 9):
                res.append(to_dec[ord(t)])
        else:
                i = i+1
print (res)
'''
'''
#poprawione od Michała 

ciag= input("wprowadź ciąg dowolnych znaków: ")
res=[]
i=0
to_dec={"0":"zero", "1":"jeden", "2":"dwa", "3":"trzy", "4":"cztery", "5":"pięć", "6":"sześć", "7":"siedem", "8":"osiem", "9":"dziewiec"}
while (i < len(ciag)):
    if (ciag[i].isdigit()):
        res.append(to_dec[ciag[i]])
    i = i+1
for i in res:
    print(i,end="")
            
           
''' 
'''
print(ord('a'))
ciag= list(input("wprowadź ciąg dowolnych znaków: "))
print(ord(ciag[0]))
'''
#zadanie p61
'''
line = range(1,6)
n = 1
print("   %3i%3i%3i%3i%3i" % (1,2,3,4,5))
print("==================")
while(n<=5):
    print(str(n)+" |", end="")
    print("%3i%3i%3i%3i%3i" % (n*line[0], n*line[1], n*line[2], n*line[3], n*line[4]))
    n +=1
 ''' 

'''
np = range(1,10,2)
i=len(np) - 1
while(i >= 0):
    if(i == 0):
        print(np[i]**2)
    else:
        print(np[i]**2, end=", ")
    i -=1

'''
