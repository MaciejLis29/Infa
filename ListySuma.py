print("podaj ilość elementów pierwszej listy")
i=int(input())
lista1=[]
print("podaj ilość elementów drugiej listy")
i2=int(input())
lista2=[]
for a in range(0,i):
    print(f"Podaj {a+1} element pierwszej listy")
    lista1.append(int(input()))
for a in range(0,i2):
    print(f"Podaj {a+1} element drugiej listy")
    lista2.append(int(input()))
if i>i2:
    temp=lista2
    for a in range(0,i2):
        b=lista1[a]
        c= b in lista2
        if c==True:
            temp.remove(b)
    print(f"Suma zbiorów to: {temp+lista1}")
elif i2>i:
    temp=lista1
    for a in range(0,i):
        b=lista2[a]
        c=b in lista1
        if c==True:
            temp.remove(b)
    print(f"Suma zbiorów to: {temp+lista2}")
else:
    temp=lista1
    for a in range(0, i):
        b = lista2[a]
        c = b in lista1
        if c == True:
            temp.remove(b)
    print(f"Suma zbiorów to: {temp+lista2}")
