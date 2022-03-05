"""def ordenar (a):
    i=0;j=0;aux=0
    while i< int(len(a)):
        j=0
        while j<int(len(a)):
            if int(a[i]) < int(a[j]):
                aux = a[i]
                a[i]=a[j]
                a[j]= aux
            j+=1
        i+=1
    print(a)
ordenar([2,7,3,8,1])"""

"""def foo(n):
    for i in range(1,n):
        if i%2==0:
            salida='x'
        else:
            salida='y'
        print(salida*i,end="")
foo(4)"""
"""x = 2
cc = ['2', '4', '3']
y = cc[0] * x**0 + cc[1] * x**1 + cc[2] * x**2
print(y)"""
"""def foo(A,B):
    lst = [] + A
    for x in B:
        if (x not in A):
            lst.append(x)
        else:
            lst.remove(x)
    return lst
print(1,foo([2,3,11,10],[11,102,3,2]))"""
"""def foo(lst):
    for j in range(len(lst)-1,0,-1):
        for i in range(j):
            if lst[i]<lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
lista = [14,46,21,18]
foo(lista)
print(lista)"""
"""def foo(miS):
    sum=0
    for x in miS:
        sum=sum+miS[x]
    print(sum)
numS="0123"
foo(numS)"""
def buscarS(xs,s):
    tupla=(-1,-1);band=False
    for i in range(len(xs)):
        if xs[i:i+len(s)]==s and band==False:
            tupla=(i,i+len(s)-1)
            band=True
    return tupla
def indicesTxT(xs,s):
    lst_tupla=[]
    tupla=buscarS(xs,s)
    if tupla== (-1,-1):
        lst_tupla=[]
    elif tupla!=(-1,-1):
        lst_tupla.append(tupla)
        ini=tupla[0]+1
        fin=tupla[1]+1
        xs=xs[fin:]
        while len(xs)>len(s):
            tupla=buscarS(xs,s)
            if tupla==(-1,-1):
                xs=""
            elif tupla!=(-1,-1):
                lst_tupla.append((ini+int(tupla[0]),fin+int(tupla[1])))
                ini+=int(tupla[0])
                fin+=int(tupla[1])
                xs=xs[fin:]
    return lst_tupla
def main():
    arch=open("Info.txt","r")
    xs=""
    for linea in arch.readline():
        xs+=linea
    s=str(input("Ingrese string a buscar: "))
    print(indicesTxT(xs,s))
main()