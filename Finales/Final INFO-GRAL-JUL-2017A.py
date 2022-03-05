"""
x = 2
cc = ['2', '4', '3']
y = cc[0] * x**0 + cc[1] * x**1 + cc[2] * x**2
print(y)
"""
"""
def foo(A,B):
    lst = [] + A
    for x in B:
        if (x not in A):
            lst.append(x)
        else:
            lst.remove(x)
    return lst
print(1,foo([2,3,11,10],[11,102,3,2]))
"""
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
print(lista)
"""
"""
def foo(miS):
    suma=0
    for x in miS:
        suma=suma+miS[x]
    print(sum)
numS="0123"
foo(numS)
"""
"""
def foo(n):
    for i in range(1,n):
        if i%2==0:
            salida='x'
        else:
            salida='y'
        print(salida*i,end="")
foo(2)
"""