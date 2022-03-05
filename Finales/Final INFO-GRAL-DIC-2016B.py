"""
ERROR
def promLst(lst):
    i=0
    prom=[]
    for sl in range(len(lst)):
        suma=0
        cuenta=0
        for i in range(len(lst[sl])):
            suma+=lst[sl][i]

        prom.append("{.:2f}".format(suma/cuenta))
    return prom
def main():
    lst=[[],[4,5,6],[1,1,2,2]]
    print(promLst(lst))
main()
"""
"""
def ingresar():
    num=int(input("Ingrese numeros impares, multiplos de 3 pero no de 7: "))
    while not (num%2!=0 and num%3==0 and num%7!=0):
        print("Error")
        num=int(input("Ingrese numeros impares, multiplos de 3 pero no de 7: "))
    return num
def main():
    print(ingresar())
main()
"""
"""
def main():
    x = input()
    if x>='0' or x<='9':
        print("Correcto")
    else:
        print("Incorrecto")
main()
"""
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
print(x,"",end="")
"""
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
#Ej. 3.1
def factura(ID_abonado):
    archAbonado=open("Abonados.txt","r")
    lstAbon=[]
    for linea in archAbonado.readlines():
        lstAbon.append(linea[:-1].split(","))
    archAbonado.close
    archCategoria=open("Categoria.txt","r")
    lstCat=[]
    for linea in archCategoria.readlines():
        lstCat.append(linea[:-1].split(","))
    archCategoria.close
    archConex=open("Conexiones.txt","r")
    lstConex=[]
    for linea in archConex.readlines():
        lstConex.append(linea[:-1].split(","))
    archConex.close
    for i in range (len(lstAbon)):
        if int(lstAbon[i][0])==ID_abonado:
            print("Nombre: {}".format(lstAbon[i][1]))
            print("Domicilio: {}".format(lstAbon[i][2]))
            i2=i
    for i in range (len(lstCat)):
        if int(lstCat[i][0])==int(lstAbon[i2][3]):
            print("Abono: {}".format(lstCat[i][1]))
            i3=i
    suma=0
    for i in range(len(lstConex)):
        if int(lstAbon[i2][0])==int(lstConex[i][0]):
            suma+=int(lstConex[i][1])
    print("Importe: {}".format(suma*(float(lstCat[i3][2]))))
    print("Total: {}".format(float(lstCat[i3][1])+suma*(float(lstCat[i3][2]))))
def main():
    factura(3)
main()
"""
"""
#ERROR
#Ej. 3.2
def duracionMaxima():
    archAbon=open("Abonados.txt","r")
    lstAbon=[]
    for linea in archAbon.readlines():
        lstAbon.append(linea[:-1].split(","))
    archAbon.close
    archCat=open("Categoria.txt","r")
    lstCat=[]
    for linea in archCat.readlines():
        lstCat.append(linea[:-1].split(","))
    archCat.close
    archCon=open("Conexiones.txt","r")
    lstCon=[]
    for linea in archCon.readlines():
        lstCon.append(linea[:-1].split(","))
    archCon.close
    total=int()
    lstG=[]
    for i in range(len(lstCon)):
        if not lstCon[i][0] in lstG:
            lstG.append(lstCon[i])
        elif lstCon[i][0] in lstG:
            for j in range(len(lstG)):
                if int(lstCon[i][0])==int(lst[j][0]):
                    lstG[j][1]= int(lstG[j][1])+int(lstCon[i][1])
    for i in range(len(lstG)):
        if total<int(lstG[i][1]):
            total=int(lstG[i][1])
            i2=i
    print("ID_Abonado: {}".format(lstG[i2][0]))
    for i in range (len(lstAbon)):
        if int(lstAbon[i][0])==int(lstG[i2][0]):
            print("Nombre: {}".format(lstAbon[i][1]))
            i3=i
    print("Categoria: {}".format(lstAbon[i3][3]))
    print("Total de duracion: {}".format(total))
def main():
    duracionMaxima()
main()
"""