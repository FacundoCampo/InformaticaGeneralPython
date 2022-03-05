"""def promLst(lst):
    i=0
    prom=[]
    for sl in range(len(lst)):
        suma=0
        for i in range(len(lst[sl])):
            suma+=lst[sl][i]
        prom.append(suma/len(lst[sl]))
    return prom
print(promLst([[1,3],[4,16],[5,5,10,20]]))"""
"""def ingresar():
    num=int(input("Ingrese numero impar, multiplo de 3 pero no de 7: "))
    while not (num%2!=0 and num%3==0 and num%7!=0):
        print("Error")
        num=int(input("Ingrese numero impar, multiplo de 3 pero no de 7: "))
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
    
    archCon=open("conexiones.txt","r")
    lstCon=[]
    for linea in archCon.readlines():
        lstCon.append(linea[:-1].split(","))
    archCon.close
    
    id_abonado=str(id_abonado)
    for i in range(len(lstAb)):
        if lstAb[i][0]==id_abonado:
            print("Nombre: {}".format(lstAb[i][1]))
            print("Domicilio: {}".format(lstAb[i][2]))
            id_cat=lstAb[i][3]
    for i in range(len(lstCat)):
        if lstCat[i][0]==id_cat:
            i2=i
            print("Abono: {}".format(lstCat[i][1]))
            impXmin=float(lstCat[i][2])
    cant=0
    for i in range(len(lstCon)):
        if lstCon[i][0]==id_abonado:
            cant+=int(lstCon[i][1])
    print("Importe: {}".format(cant*impXmin))
    print("Total: {}".format(cant*impXmin+float(lstCat[i2][1])))
factura(3)"""
def duracionMaxima():
    archAb=open("abonados.txt","r")
    lstAb=[]
    for linea in archAb.readlines():
        lstAb.append(linea[:-1].split(","))
    archAb.close
    
    archCon=open("conexiones.txt","r")
    lstCon=[]
    for linea in archCon.readlines():
        lstCon.append(linea[:-1].split(","))
    archCon.close
    
    maxi=0;cant=0;lst=[]
    for i in range(len(lstCon)):
        if not lstCon[i][0] in lst:
            lst.append(lstCon[i][0])
            
    for i in range(len(lst)):
        cant=0
        for z in range(len(lstCon)):
            if lst[i]==lstCon[z][0]:
                cant+=int(lstCon[z][1])
        if cant>maxi:
            maxi=cant
            iD=lst[i]
    for i in range(len(lstAb)):
        if lstAb[i][0]==iD:
            print("Id_abonado: {}".format(iD))
            print("Nombre: {}".format(lstAb[i][1]))
            print("Categoria: {}".format(lstAb[i][3]))
            print("Duracion: {}".format(maxi))
duracionMaxima()
            
            