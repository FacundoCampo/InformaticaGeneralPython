"""def promLst(lst):
    i=0
    prom=[]
    for sl in range(len(lst)):
        suma=0
        for i in range(len(lst[sl])):
            suma+=int(lst[sl][i])
        prom.append(suma/len(lst[sl]))
    return prom
print(promLst([[1,3],[4,16],[5,5,10,20]]))"""
"""def ingresar():
    num=int(input("Ingrese un numero impar, multiplo de 3 pero no de 7: "))
    while not(num%2!=0 and num%3==0 and num%7!=0):
        print("Error")
        num=int(input("Ingrese un numero impar, multiplo de 3 pero no de 7: "))
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
"""def factura(id_Abonado):
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
    
    id_Abonado=str(id_Abonado)
    for i in range(len(lstAb)):
        if lstAb[i][0]==id_Abonado:
            print("Nombre: {}".format(lstAb[i][1]))
            print("Domicilio: {}".format(lstAb[i][2]))
            id_cat=lstAb[i][3]
    for z in range(len(lstCat)):
        if lstCat[z][0]==id_cat:
            print("Abono: {}".format(lstCat[z][1]))
            z2=z
    cant=0
    for x in range(len(lstCon)):
        if lstCon[x][0]==id_Abonado:
            cant+=int(lstCon[x][1])
    print("Importe: {}".format(cant*float(lstCat[z2][2])))
    print("Total: {}".format(cant*float(lstCat[z2][2])+float(lstCat[z2][1])))
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
    lst_id=[]
    for i in range(len(lstAb)):
        if not lstAb[i][0] in lst_id:
            lst_id.append(lstAb[i][0])
    maxi=0
    for z in range(len(lst_id)):
        cant=0
        for x in range(len(lstCon)):
            if lst_id[z]==lstCon[x][0]:
                cant+=int(lstCon[x][1])
        if cant>maxi:
            maxi=cant
            z2=z
    print("id abonado: {}".format(lst_id[z2]))
    for i in range(len(lstAb)):
        if lstAb[i][0]==lst_id[z2]:
            print("Nombre: {}".format(lstAb[i][1]))
            print("Categoria: {}".format(lstAb[i][3]))
    print("Duracion total: {}".format(maxi))
duracionMaxima()