"""def ordenar (A):
    i=0;j=0;aux=0
    while i<len(A):
        j=i+1
        while j<len(A):
            if A[i]>A[j]:
                aux = A[j]
                A[j]=A[i]
                A[i]= aux
            j+=1
        i+=1
    print(A)
ordenar([2,7,3,8,1,9,6,5])"""
"""def foo(n):
    for i in range(1,n):
        if i%2==0:
            salida='x'
        else:
            salida='y'
        print(salida*i,end="")
foo(3)"""
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
    suma=0
    for x in miS:
        suma=suma+miS[x]
    print(sum)
numS="0123"
foo(numS)"""

def buscarS(xs,s):
    band=False
    tup=(-1,-1)
    for i in range(len(xs)):
        if xs[i:i+len(s)]==s and band==False:
            tup=(i,i+len(s)-1)
            band=True
    return tup
def indicesTXT(xs,s):
    lst=[]
    tup=buscarS(xs,s)
    if tup!=(-1,-1):
        lst.append(tup)
        ini=tup[0]
        fin=tup[1]+1
        xs=xs[fin:]
        while len(xs)>0:
            tup=buscarS(xs,s)
            if tup!=(-1,-1):
                fin+=tup[1]
                ini=fin-len(s)+1
                xs=xs[tup[1]+1:]
                lst.append((ini,fin))
            else:
                xs=""
    return lst
def main():
    arch=open("info.txt","r")
    xs=""
    for i in arch.readlines():
        xs+=i
    s=str(input("Ingrese str a buscar: "))
    print("{}\n".format(buscarS(xs,s)))
    print(indicesTXT(xs,s))
    arch.close
main()