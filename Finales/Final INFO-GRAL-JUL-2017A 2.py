"""def ordenar (a):
    i=0;j=0;aux=0
    while i<len(a):
        j=i+1
        while j<=len(a)-1:
            if a[i]>a[j]:
                aux = a[i]
                a[i]=a[j]
                a[j]= aux
            j+=1
        i+=1
    return a
print(ordenar([2,7,3,8,1]))
"""
def foo(n):
    for i in range(1,n):
        if i%2==0:
            salida='x'
        else:
            salida='y'
        print(salida*i,end="")
foo(6)
"""
x = 2
cc = ['2', '4', '3']
y = cc[0] * x**0 + cc[1] * x**1 + cc[2] * x**2
print(y)"""
"""
def foo(A,B):
    lst = [] + A
    for x in B:
        if (x not in A):
            lst.append(x)
        else:
            lst.remove(x)
    return lst
print(1,foo([2,3,11,10],[11,102,3,2]))"""
"""
def foo(lst):
    for j in range(len(lst)-1,0,-1):
        for i in range(j):
            if lst[i]<lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
lista = [14,46,21,18]
foo(lista)
print(lista)"""
"""
def foo(miS):
    sum=0
    for x in miS:
        sum=sum+miS[x]
    print(sum)
numS="0123"
foo(numS)
"""
"""def buscarS(xs,s):
    tupla=(-1,-1)
    j=len(s)
    band=False
    for i in range(len(xs)):
        if xs[i:j+i]==s and band==False:
            tupla=(i,j+i)
            band=True
    return tupla
def indicesTXT(xs,s):
    lst_tupla=[]
    tupla=buscarS(xs,s)
    if tupla!=(-1,-1):
        ini=tupla[0]
        fin=tupla[1]
        lst_tupla.append(tupla)
        xs=xs[fin:]
        while len(xs)>0:
            tupla=buscarS(xs,s)
            if tupla!=(-1,-1):
                lst_tupla.append((tupla[0]+ini,tupla[1]+fin))
                ini=tupla[0]
                fin=tupla[1]
                xs=xs[fin:]
            else:
                xs=""
    return lst_tupla
def main():
    arch=open("info.txt","r")
    s=str(input("Ingrese string a comparar: "))
    xs=""
    for linea in arch.readline():
        xs+=linea
    arch.close
    print(indicesTXT(xs,s))
main()"""