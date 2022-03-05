"""
def ingresar():
    num=int(input("Ingrese un numero impar, multiplo de 3 y no de 7: "))
    while not (num%2!=0 and num%3==0 and num%7!=0):
        print("ERROR")
        num=int(input("Ingrese un numero impar, multiplo de 3 y no de 7: "))
    return num
def main():
    print(ingresar())
main()


def foo(a,b):
    lst=[]
    for i in range(len(a)):
        if a[i] not in b:
            lst.append(a[i])
    for i in range(len(b)):
        if b[i] not in a:
            lst.append(b[i])
    return lst
def main():
    a=[1,2,3,4,5]
    b=[2,4,6,7,8]
    print(foo(a,b))
main()
"""
"""
def foo(miStr,num):
    miStr[num]="X"
    y=num-1
    return miStr[num-y]
def main():
    print(foo("abcd",len("abcd")-1))
main()
"""
"""
import random
def aleatorio():
    lst=[]
    for i in range(0,5):
        x=(random.randint(0,20)%5)*2
        lst.append(x)
    return lst
def main():
    print(aleatorio())
main()
"""
"""
lst=[10,20,30,40,50]
tam=len(lst)
i=1
suma=0
while i<=tam:
    suma+=lst[i]
    i+=1
print(suma)
"""
"""
def foo():
    suma='0'
    for x in "0123":
        if not(x=='0'and x=='1')==(not x=='0' or not x=='1'):
            suma=suma+x
    return suma
def main():
    print(foo())
main()
"""

def buscarS(xs,s):
    band=0
    tupla=(-1,-1)
    i2=0
    for i in range(len(s),len(xs)-1):
        if xs[i2:i]==s and band==0:
            band=1
            ini=i2
            fin=i
            tupla=(ini,fin)
        i2+=1
    return tupla
def indicesTXT(xs,s):
    lista=[]
    band=False
    t=buscarS(xs,s)
    if t!=(-1,-1):
        inicio=t[0]
        fin=t[1]
        lista.append(t)
        while band==False:
            xs=xs[t[1]+1:]
            t=buscarS(xs,s)
            if t!=(-1,-1):
                inicio=fin+t[0]+1
                fin=inicio+len(s)
                t=(inicio,fin)
                lista.append(t)
            else:
                band=True
    return lista
def main():
    s=str(input("Ingrese un string: "))
    arch=open("info.txt","r")
    for linea in arch.readlines():
        lineas=linea
    print(indicesTXT(lineas,s))
    arch.close
main()
