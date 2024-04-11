print("podaj ilość elementów 1 listy")
i=int(input())
lista1=[]
print("podaj ilość elementów 2 listy")
i2=int(input())
lista2=[]
print("podaj elementy 1 listy")
for a in range(0,i):
    lista1.append(int(input()))
print("podaj elementy 2 listy")
for a in range(0,i2):
    lista2.append(int(input()))
temp=[]
if i>i2:
    for a in range(0,i2):
        b=lista1[a]
        c= b in lista2
        if c==True:
            temp.append(b)
elif i2>i:
    for a in range(0,i):
        b=lista2[a]
        c=b in lista1
        if c==True:
            temp.append(b)
else:
    for a in range(0, i):
        b = lista2[a]
        c = b in lista1
        if c == True:
            temp.append(b)
print("Część wspólna zbiorów: ")
print(temp)

