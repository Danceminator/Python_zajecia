# -*- coding: utf-8 -*-
import random
'''
def powitanie(imie):
    witaj="witaj "+imie+"!"
    return witaj
L=[]
for i in range(1,4):
    L.append(powitanie(input("Podaj imie do listy: ")))
print(L)
'''
'''
def dodawanie(a,b, imie="Anonim"):
    wynik = a + b
    print(a, b)
    print (imie)
    return wynik
res = dodawanie (a=14, b=24)
print(res)
'''
'''
n=int(input("wpisz podstawę silni: "))

def silniaele(n):
    res=1 
    i=1
    L= []
    while(i <=n):
        res *= i
        L.append(res)
        i +=1
    return L

#zamiast powtarzać print lista jakaś tam i zamieniać na listę możemy zamienić 
#print("elementy ciągu silnia:", silniaele(n))

def wyswietl(lista):
    for i in lista:
        print(i, end=" ")
        
wyswietl(silniaele(n))

'''

F=[0,1]
n= int(input("wprowadź ile elementów ciągu Fibonacciego chcesz zobaczyć: "))
i =2
fib =2

for n in F:
    fib =F[i-2] + F[i-1]
    F.append(fib)
    i +=1
    
print(F)

'''
def zdania(a=5):
    wyrazy=["ciąg", "Fibonacciego", "liczb", "naturalnych", "sposób", "następujący"]
    i=0
    Zdanie = []
    while (i<a):
        Zdanie.append(wyrazy[random.randint(0, len(wyrazy)-1)])
        i+=1
    return Zdanie
def format(zdanie):
    for i, v in enumerate(zdanie):
        if(i ==0):
            print(v.capitalize(), end=" ")
        elif(i == len(zdanie)-1):
            print(v, end=".")
        else:
            print(v, end=" ")

format(zdania())
'''