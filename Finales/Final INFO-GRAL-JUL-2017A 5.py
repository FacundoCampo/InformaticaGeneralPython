"""def ordenar (A):
    i=0;j=0;aux=0
    while i<len(A):
        j=0
        while j+i<len(A):
            if A[i]>A[j+i]:
                aux = A[i]
                A[i]=A[i+j]
                A[i+j]= aux
            j+=1
        i+=1
    return A
print(ordenar([2,7,3,8,1,9,9999,0,88]))"""

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
def buscarS(xs,s):
    tupla=(-1,-1)
    band=False
    for i in range(len(xs)):
        if xs[i:len(s)+i]==s and band==False:
            band=True
            tupla=(i,len(s)+i-1)
    return tupla
def indicesTXT(xs,s):
    lst=[]
    tupla=buscarS(xs,s)
    if tupla!=(-1,-1):
        lst.append(tupla)
        ini=tupla[0]
        fin=tupla[1]
        xs=xs[fin+1:]
        while len(xs)>0:
            tupla=buscarS(xs,s)
            if tupla!=(-1,-1):
                ini+=tupla[0]+1
                fin+=tupla[1]+1
                lst.append((ini,fin))
                xs=xs[fin:]
            else:
                xs=""
    return lst
def main():
    arch=open("info.txt","r")
    xs=""
    for i in arch.readlines():
        xs+=i
    arch.close
    s=str(input("Ingrese un string a buscar: "))
    print(buscarS(xs,s))
    print(indicesTXT(xs,s))
main()