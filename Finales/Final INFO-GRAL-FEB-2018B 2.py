"""def buscarS(xs,s):
    bandera=False
    for i in range(len(xs)):
        if xs[i:(len(s))+i]==s and bandera==False:
            result=(i,len(s)+i-1)
            bandera=True
    if bandera==False:
        result=(-1,-1)
    return result
def listaIndice(xs,s):
    lst=[]
    tupla=buscarS(xs,s)
    ini=tupla[0]
    fin=tupla[1]
    if tupla!=(-1,-1):
        lst.append(tupla)
        xs=xs[tupla[1]+1:]
        while len(xs)>0:
            tupla=buscarS(xs,s)
            if tupla!=(-1,-1):
                ini+=tupla[0]
                fin+=tupla[1]
                lst.append([ini,fin])
                xs=xs[tupla[1]+1:]
            elif tupla==(-1,-1):
                xs=""
    elif str(tupla)=="(-1,-1)":
        lst.append([])
    return lst
                
            
def main():
    s=str(input("Ingrese string a buscar: "))
    xs=""
    arch=open("info.txt","r")
    for linea in arch.readline():
        xs+=linea
    arch.close
    print(listaIndice(xs,s))
main()"""
"""
def ingresar():
    num=int(input("Ingresar numero impar, multiplo de 3 y no de 7: "))
    while not (num%2==1 and num%3==0 and num%7!=0):
        print("Error")
        num=int(input("Ingresar...:"))
    return num
print(ingresar())"""
"""def foo(a,b):
    lst=[]
    for i in range (len(a)):
        if a[i] not in b:
            lst.append(a[i])
    for z in range (len(b)):
        if b[z] not in a:
            lst.append(b[z])
    return lst
a=[1,2,3,4,5,6,7,8,9]
b=[1,1.5,10,5,95]
print(foo(a,b))"""
"""
def foo(miStr,num):
    miStr[num]='x'
    y=num-1
    print(miStr[num-y])
foo("abcd",len("abcd")-1)"""
"""
import random
def aleatorio():
    lst=[]
    for i in range(0,5):
        x=(random.randint(0,20)%5)*2
        lst.append(x)
    return lst
print(aleatorio())
"""
"""
lst=[10,20,30,40,50]
tam=len(lst)
i=1
suma=0
while i<=tam:
    suma+=lst[i]
    i+=1
print(suma)"""
def foo():
    suma='0'
    for x in "0123":
        if not(x=='0'and x=='1')==(not x=='0' or not x=='1'):
            suma=suma+x
    return suma
print(foo())