"""def promlst(lst):
    i=0
    prom=[]
    for sl in range(len(lst)):
        suma=0
        for i in range(len(lst[sl])):
            suma+=int(lst[sl][i])
        prom.append(suma/(len(lst[sl])))
    return prom
def main():
    lst=[[1,3],[4,16],[5,5,10,20]]
    print(promlst(lst))
main()"""
"""def ingresar():
    num=int(input("Ingrese numero impar, multiplo de 3 y no de 7"))
    while num%2==0 or num%3!=0 or num%7==0:
        print("Error")
        num=int(input("Ingrese un numero"))
    return num
def main():
    print(ingresar())
main()"""
"""
x = input()
if x>='0' or x<='9':
    print("Correcto")
else:
    print("Incorrecto")"""
"""
def f2(x):
    x-=5
    print(x,"",end="")
def f1():
    x=5
    f2(x)
    print(x,"",end="")
x = 1
f1()
print(x,"",end="")"""
"""
def cambiar(miStr,num):
    miStr[num]='x'
    y=num
    num+=1
    return miStr[num-y]
cad="abcd"
n=3
letra=cambiar(cad,3)
print("{:s}–{:s}-{:d}".format(cad,letra,n))
"""
"""
xn=['1','2','3','4']
n="1234".split()
a=('1' in xn)
b=('2' in n)
print(a, b)
"""
"""
def factura(id_Abonado):
    arch_Abonados=open("Abonados.txt","r")
    lst_Abonados=[]
    for linea in arch_Abonados.readlines():
        lst_Abonados.append(linea[:-1].split(","))
    arch_Abonados.close
    arch_Categorias=open("Categoria.txt","r")
    lst_Categorias=[]
    for linea in arch_Categorias.readlines():
        lst_Categorias.append(linea[:-1].split(","))
    arch_Categorias.close
    arch_Conexiones=open("Conexiones.txt","r")
    lst_Conexiones=[]
    for linea in arch_Conexiones.readlines():
        lst_Conexiones.append(linea[:-1].split(","))
    arch_Conexiones.close
    for i in range(len(lst_Abonados)):
        if id_Abonado==int(lst_Abonados[i][0]):
            print("Nombre: {}".format(lst_Abonados[i][1]))
            print("Domicilio: {}".format(lst_Abonados[i][2]))
            i2=i
    for i in range(len(lst_Categorias)):
        if int(lst_Abonados[i2][3])==int(lst_Categorias[i][0]):
            print("Abono: {}".format(lst_Categorias[i][1]))
            i3=i
    cant_minutos=0
    for i in range(len(lst_Conexiones)):
        if int(lst_Conexiones[i][0])==int(lst_Abonados[i2][0]):
            cant_minutos+=int(lst_Conexiones[i][1])
    print("Importe: {}".format(int(cant_minutos)*float(lst_Categorias[i3][2])))
    print("Total: {}".format(float(lst_Categorias[i3][1])+int(cant_minutos)*float(lst_Categorias[i3][2])))
factura(3)
"""
"""
def duracionMaxima():
    arch_Abonados=open("Abonados.txt","r")
    lst_Abonados=[]
    for linea in arch_Abonados.readlines():
        lst_Abonados.append(linea[:-1].split(","))
    arch_Abonados.close
    arch_Categorias=open("Categoria.txt","r")
    lst_Categorias=[]
    for linea in arch_Categorias.readlines():
        lst_Categorias.append(linea[:-1].split(","))
    arch_Categorias.close
    arch_Conexiones=open("Conexiones.txt","r")
    lst_Conexiones=[]
    for linea in arch_Conexiones.readlines():
        lst_Conexiones.append(linea[:-1].split(","))
    arch_Conexiones.close
    lst_Duracion=[]
    lst_Keys=[]
    for i in range(len(lst_Conexiones)):
        if lst_Duracion==[]:
            lst_Duracion.append(lst_Conexiones[i])
            lst_Keys.append(lst_Conexiones[i][0])
        elif not lst_Conexiones[i][0] in lst_Keys:
                lst_Duracion.append(lst_Conexiones[i])
                lst_Keys.append(lst_Conexiones[i][0])
        elif lst_Conexiones[i][0] in lst_Keys:
                for x in range(len(lst_Duracion)):
                    if lst_Conexiones[i][0]==lst_Duracion[x][0]:
                        lst_Duracion[x][1]=str(int(lst_Duracion[x][1])+int(lst_Conexiones[i][1]))
    iD=""
    maxi=int()
    for i in range(len(lst_Duracion)):
        if int(lst_Duracion[i][1])>maxi:
            maxi=int(lst_Duracion[i][1])
            iD=lst_Duracion[i][0]
    print("ID_Abonado: {}".format(iD))
    for i in range(len(lst_Abonados)):
        if iD==lst_Abonados[i][0]:
            print("Nombre: {}".format(lst_Abonados[i][1]))
            print("Categoria: {}".format(lst_Abonados[i][3]))
    print("Duracion total en minutos: {}".format(maxi))
duracionMaxima()
"""