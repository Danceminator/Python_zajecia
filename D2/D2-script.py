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
to_rom={ '1': "I", '2': "II", '3':"III", '4':"IV", '5':"V"}

print (key1.capitalize() + " w postaci liczby dziesiętnej to: "+str(to_dec[key1])+",a w postaci rzymskiej: "+str(to_rom[to_dec[key1]]))'''

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

los1=random.randint(1,49)

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
      
