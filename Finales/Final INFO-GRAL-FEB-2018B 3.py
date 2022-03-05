"""def ingresar():
    num=int(input("Ingrese un numero impar, multiplo de 3 pero no de 7: "))
    while not(num%2!=0 and num%3==0 and num%7!=0):
        print("Error")
        num=int(input("Ingrese un numero impar, multiplo de 3 pero no de 7: "))
    return num
print(ingresar())"""
"""def foo(a,b):
    lst = []
    for i in range(len(a)):
        if not a[i] in b:
            lst.append(a[i])
    for i in range(len(b)):
        if not b[i] in a:
            lst.append(b[i])
    return lst
print(foo([1,2,3,4],[2,4,5,6]))"""
"""def foo(miStr,num):
    miStr[num]='x'
    y=num-1
    return miStr[num-y]
foo("abcd",len("abcd")-1)"""
"""import random
def aleatorio():
    lst=[]
    for i in range(0,5):
        x=(random.randint(0,20)%5)*2
        lst.append(x)
    return lst
print(aleatorio())"""
"""lst=[10,20,30,40,50]
tam=len(lst)
i=1
suma=0
while i<=tam:
    suma+=lst[i]
    i+=1
print(suma)"""
"""def foo():
    suma='0'
    for x in "0123":
        if not(x=='0'and x=='1')==(not x=='0' or not x=='1'):
            suma=suma+x
    return suma
print(foo())"""
def buscarS(xs,s):
    tup=(-1,-1)
    band=False
    for i in range(len(xs)):
        if xs[i:len(s)+i]==s and band==False:
            tup=(i,len(s)+i-1)
            band=True
    return tup
def listaIndice(xs,s):
    lstTup=[]
    tupla=buscarS(xs,s)
    if tupla!=(-1,-1):
        lstTup.append(tupla)
        ini=tupla[0]+1
        fin=tupla[1]+1
        xs=xs[fin:]
        while len(xs)>0:
            tupla=buscarS(xs,s)
            if tupla!=(-1,-1):
                lstTup.append((ini+tupla[0],fin+tupla[1]))
                ini+=tupla[0]
                fin+=tupla[1]
                xs=xs[fin:]
            else:
                xs=""
    else:
        lstTup=[]
    return lstTup
def main():
    archXS=open("info.txt","r")
    xs=""
    for linea in archXS.readlines():
        xs+=linea
    s=str(input("Ingrese el str a buscar: "))
    archXS.close
    print(listaIndice(xs,s))
main()
