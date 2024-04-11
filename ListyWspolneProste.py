lista1=[2,5,8,9,3,4,15,12]
lista2=[3,7,15,14,13]
i=len(lista1)
temp=[]
for a in range(0,i):
    b=lista1[a]
    c= b in lista2
    if c==True:
        temp.append(b)
print(f"Część wspólna list to: {temp}")
