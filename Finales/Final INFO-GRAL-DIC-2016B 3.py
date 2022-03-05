"""def promLst(lst):
    i=0
    prom=[]
    for sl in range(len(lst)):
        suma=0
        for i in range(len(lst[sl])):
            suma+=int(lst[sl][i])
        prom.append(suma/int(len(lst[sl])))
    return prom
print(promLst([[1,3],[4,16],[5,5,10,20]]))"""
"""def ingresar():
    num=int(input("Ingrese numero impar, divisible por 3 pero no por 7: "))
    while not(num%2!=0 and num%3==0 and num%7!=0):
        print("Error")
        num=int(input("Ingrese numero impar, divisible por 3 pero no por 7: "))
    return num
print(ingresar())"""
"""x = input()
if x>='0' or x<='9':
    print("Correcto")
else:
    print("Incorrecto")"""
"""def f2(x):
    x-=5
    print(x,"",end="")
def f1():
    x=5
    f2(x)
    print(x,"",end="")
x = 1
f1()
print(x,"",end="")"""
"""def cambiar(miStr,num):
    miStr[num]='x'
    y=num
    num+=1
    return miStr[num-y]
cad="abcd"
n=3
letra=cambiar(cad,3)
print("{:s}–{:s}-{:d}".format(cad,letra,n))"""
"""xn=['1','2','3','4']
n="1234".split()
a=('1' in xn)
b=('2' in n)
print(a, b)"""

"""def factura(id_abonado):
    archAbonados=open("abonados.txt","r")
    lstAbonados=[]
    for linea in archAbonados.readlines():
        lstAbonados.append(linea[:-1].split(","))
    archAbonados.close
    archCat=open("categoria.txt","r")
    lstCat=[]
    for linea in archCat.readlines():
        lstCat.append(linea[:-1].split(","))
    archCat.close
    archCon=open("conexiones.txt","r")
    lstCon=[]
    for linea in archCon.readlines():
        lstCon.append(linea[:-1].split(","))
    archCon.close
    for i in range(len(lstAbonados)):
        if int(lstAbonados[i][0])==id_abonado:
            print("Nombre: {}".format(lstAbonados[i][1]))
            print("Domicilio: {}".format(lstAbonados[i][2]))
            i2=i
    for z in range(len(lstCat)):
        if lstCat[z][0]==lstAbonados[i2][3]:
            print("Abono: {}".format(lstCat[z][1]))
            z2=z
    tot=0
    for y in range(len(lstCon)):
        if lstCon[y][0]== lstAbonados[i2][0]:
            tot+=int(lstCon[y][1])
    print("Importe: {}".format(tot*float(lstCat[z2][2])))
    print("Total: {}".format(tot*float(lstCat[z2][2])+float(lstCat[z2][1])))
factura(3)"""

def duracionMaxima():
    archAb=open("abonados.txt","r")
    lstAb=[]
    for linea in archAb.readlines():
        lstAb.append(linea[:-1].split(","))
    archAb.close
    archCat=open("categoria.txt","r")
    lstCat=[]
    for linea in archCat.readlines():
        lstCat.append(linea[:-1].split(","))
    archCat.close
    archConex=open("conexiones.txt","r")
    lstConex=[]
    for linea in archConex.readlines():
        lstConex.append(linea[:-1].split(","))
    archConex.close
    maxi=int();suma=0;lstID=[]
    for i in range(len(lstConex)):
        if not lstConex[i][0] in lstID:
            lstID.append(lstConex[i][0])
    for i in range(len(lstID)):
        for z in range(len(lstConex)):
            if lstID[i]==lstConex[z][0]:
                suma+=int(lstConex[z][1])
        if suma>maxi:
            maxi=suma
            i2=i
        suma=0
    print("Id_Abonado: {}".format(lstID[i2]))
    for j in range(len(lstAb)):
        if lstID[i2]==lstAb[j][0]:
            print("Nombre: {}".format(lstAb[j][1]))
            print("Categoria: {}".format(lstAb[j][3]))
    print("Duracion total en minutos: {}".format(maxi))
duracionMaxima()