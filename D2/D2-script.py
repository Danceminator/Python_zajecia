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





