"""
#Ej.1
def informe(arch):
    lst=[]
    maxi=""
    mini=""
    prom=""
    cant=0
    cuenta=0
    for linea in arch.readlines():
        lineaAux=int(linea[:len(linea)-1])
        cant+=1
        cuenta+=lineaAux
        if maxi=="" and mini=="":
            maxi=lineaAux
            mini=lineaAux
        else:
            if lineaAux>maxi:
                maxi=lineaAux
            elif lineaAux<mini:
                mini=lineaAux
    prom=int(cuenta)/cant
    lst.append(maxi)
    lst.append(mini)
    lst.append(prom)
    lst.append(cant)
    return lst
def main():
    archivo=open("Ej_1.txt","r")
    print(informe(archivo))
    archivo.closed
main()
"""
"""
#Ej.2
def agregarMedia(nombre):
    arch=open(nombre,"r")
    lista=arch.readlines()
    promedio=[]
    for linea in lista:
        l=linea.split(",")
        cant=len(l)
        cuenta=0
        for num in l:
            cuenta+=(int(num))
        prom=cuenta/cant
        promedio.append(prom)
    arch.closed()
    arch2=open(nombre,"w")
    i=0
    for linea in lista:
        arch2.write(linea)
        arch2.write(str(promedio[i])+"\n")
        i+=1
    arch2.closed()
def main():
    agregarMedia("Practica 7 Ej_2.txt")
main()
"""
"""
#Ej.4
def cabecera(arch,cant,pmin,pmax):
    pal=""
    cuenta=0
    j=0
    for i in arch.readlines():
        while cant>cuenta and j<len(i):
            if (i[j]>="a" and i[j]<="z") or (i[j]>="A" and i[j]>="Z"):
                pal+=i[j]
            elif not (i[j]>="a" and i[j]<="z") or (i[j]>="A" and i[j]>="Z"):
                if len(pal)>=pmin and len(pal)<=pmax:
                    print(pal)
                    cuenta+=1
                pal=""
            j+=1
        j=0
def main():
    arch=open("Practica 7 Ej_4.txt", "r")
    cant=int(input("Ingrese cantidad de palabras a buscar: "))
    if cant<0:
        cant=int(input("Error! Ingrese cantidad de palabras a buscar: "))
    pmin=int(input("Ingrese longitud de palabra mas corta: "))
    if pmin<0:
        pmin=int(input("Error!Ingrese longitud de palabra mas corta: "))
    pmax=int(input("Ingrese longitud de palabra mas larga: "))
    if pmax<pmin:
        pmax=int(input("Error!Ingrese longitud de palabra mas larga: "))
    cabecera(arch,cant,pmin,pmax)
    
main()
"""
"""
#Ej.5
def cabecera2(arch,cant,pmin,pmax):
    arch2=open("resultado.txt","w")
    pal=""
    i=0
    cuenta=0
    lst=[]
    for linea in arch.readlines():
        while cant>cuenta and i<len(linea):
            if (linea[i]>"a" and linea[i]<"z") or (linea[i]>"A" and linea[i]<"Z"):
                pal+=linea[i]
            elif not (linea[i]>"a" and linea[i]<"z") or (linea[i]>"A" and linea[i]<"Z"):
                if len(pal)>pmin and len(pal)<pmax and not pal in lst:
                    lst.append(pal)
                    arch2.write(pal)
                    arch2.write("\n")
                    cuenta+=1
                pal=""
            i+=1
        i=0
    arch.close
    arch2.close
def main():
    arch=open("Practica 7 Ej_4,2.txt", "r")
    cant=int(input("Ingrese cantidad de palabras a buscar: "))
    if cant<0:
        cant=int(input("Error! Ingrese cantidad de palabras a buscar: "))
    pmin=int(input("Ingrese longitud de palabra mas corta: "))
    if pmin<0:
        pmin=int(input("Error!Ingrese longitud de palabra mas corta: "))
    pmax=int(input("Ingrese longitud de palabra mas larga: "))
    if pmax<pmin:
        pmax=int(input("Error!Ingrese longitud de palabra mas larga: "))
    cabecera2(arch,cant,pmin,pmax)
    
main()
"""
"""
#Ej.6
import random
def generadora(ori,dest,cant):
    archOri=open(ori,"r")
    archDest=open(dest,"w")
    totLinea=0
    lstPal=[]
    for linea in archOri.readlines():
        lstPal.append(linea)
        totLinea+=1
    lstNum=[]
    num=random.randint(0,totLinea-1)
    while len(lstNum)<cant:
        if num not in lstNum:
            lstNum.append(num)
            aux=lstPal[num]
            archDest.write(aux)
        num=random.randint(0,totLinea-1)
    archOri.close
    archDest.close
        
def main():
    origen="Practica 7 Ej_5.txt"
    destino="Destino.txt"
    cantidad=9
    generadora(origen,destino,cantidad)
main()
"""

#Ej.7
def agregarRegistro(nombreArch):
    arch=open(nombreArch,"r")
    lst=[]
    
    pal=""
    for linea in arch.readlines():
        for j in range(len(linea)):
            if linea[j]>="0" and linea[j]<="9":
                pal+=linea[j]
            elif not linea[j]>"0" and linea[j]<"9":
                if pal!="":
                    lst.append(pal)
                pal=""
    arch.close
    arch=open(nombreArch,"a")
    
    nombre=str(input("Ingrese el nombre: "))
    apellido=str(input("Ingrese el apellido: "))
    dni=str(input("Ingrese el dni: "))
    while dni in lst:
        dni=int(input("ERROR, no se puede repetir mismo dni: "))
    arch.write("{},{},{}\n".format(nombre,apellido,dni))
    arch.close
    lst=[]
def eliminarRegistro(nombreArch):
    arch=open(nombreArch,"r")
    lst=[]
    pal=""
    for linea in arch.readlines():
        lst.append(linea[:-1].split(","))
    arch.close
    band=0
    dni=int(input("Ingrese el dni que se quiere eliminar"))
    while band==0:
        for i in range (len(lst)):
            if int(lst[i][2])==dni:
                i2=i
                band=1
        if band==0:
            dni=int(input("Ese dni no existe: "))
    lst.remove(lst[i2])
    arch=open(nombreArch,"w")
    for linea in range(len(lst)):
        lst[linea][2]=str(lst[linea][2])
        arch.write(",".join(lst[linea])+"\n")
    arch.close
def buscarRegistro(nombreArch):
    opcion=int(input("Ingrese 0 si quieres buscar por apellido o 1 si quiere buscar por dni: "))
    while opcion!=0 and opcion!=1:
        opcion=int(input("ERROR, Ingrese 0 si quieres buscar por apellido o 1 si quiere buscar por dni: "))
    arch=open(nombreArch,"r")
    lst=[]
    for linea in arch.readlines():
        lst.append(linea[:-1].split(","))
    if opcion==0:
        apellido=str(input("Ingrese el apellido: "))
        band=0
        while band==0:
            for i in range (len(lst)):
                if lst[i][1]==apellido:
                    print(lst[i])
                    band=1
            if band==0:
                apellido=str(input("No existe ese apellido: "))
    if opcion==1:
        dni=str(input("Ingrese el dni: "))
        band=0
        while band==0:
            for i in range (len(lst)):
                if lst[i][2]==dni:
                    print(lst[i])
                    band=1
            if band==0:
                dni=str(input("No existe ese dni: "))
                


def ordenarArchivo(nombreArch):
    opcion=int(input("Ingrese 1 para ordenar por nombre, 2 para apellido o 3 para dni: "))
    lstOp=[1,2,3]
    while opcion not in lstOp:
        opcion=int(input("ERROR Ingrese 1 para ordenar por nombre, 2 para apellido o 3 para dni: "))
    arch=open(nombreArch,"r")
    lst=[]
    for linea in arch.readlines():
        lst.append(linea[:-1].split(","))
    arch.close
    arch=open(nombreArch,"w")
    if opcion==1:
        for i in range(len(lst)):
            for j in range (i+1,len(lst)):
                if lst[i][0]<lst[j][0]:
                    aux=lst[i]
                    lst[i]=lst[j]
                    lst[j]=aux
    elif opcion==2:
        for i in range(len(lst)):
            for j in range (i+1,len(lst)):
                if lst[i][1]<lst[j][1]:
                    aux=lst[i]
                    lst[i]=lst[j]
                    lst[j]=aux
    elif opcion==3:
        for i in range(len(lst)):
            for j in range (i+1,len(lst)):
                if int(lst[i][2])<int(lst[j][2]):
                    aux=lst[i]
                    lst[i]=lst[j]
                    lst[j]=aux
    for i in range(len(lst)):
        arch.write(",".join(lst[i])+"\n")
    arch.close
def mostrarArchivo(nombreArch):
    arch=open(nombreArch,"r")
    lst=[]
    for linea in arch.readlines():
        lst.append(linea[:-1].split(","))
    arch.close
    print(lst)
def main():
    print("1. AGREGAR REGISTRO\n2. ELIMINAR REGISTRO\n3. BUSCAR REGISTRO\n4. ORDENAR ARCHIVO POR\n5. MOSTRAR ARCHIVO\n6. SALIR")
    num=int(input("Ingrese el valor de la opción: "))
    nombreArch="Practica 7 Ej_7.txt"
    while num!=6:
        while num<1 or num>6:
            num=int(input("ERROR, numero invalido, ingrese numero: "))
        if num==1:
            agregarRegistro(nombreArch)
        elif num==2:
            eliminarRegistro(nombreArch)
        elif num==3:
            buscarRegistro(nombreArch)
        elif num==4:
            ordenarArchivo(nombreArch)
        elif num==5:
            mostrarArchivo(nombreArch)
        print("1. AGREGAR REGISTRO\n2. ELIMINAR REGISTRO\n3. BUSCAR REGISTRO\n4. ORDENAR ARCHIVO POR\n5. MOSTRAR ARCHIVO\n6. SALIR")
        num=int(input("Ingrese el valor de la opción: ")) 
main()

"""
#Ej.8
def poblacion(idProv):
    archProv=open("Practica 7 Ej 8 Provincias.txt","r")
    archLoc=open("Practica 7 Ej 8 Localidades.txt","r")
    lstProv=[]
    lstLoc=[]
    cantHab=0
    for linea in archProv.readlines():
        lstProv.append(linea[:-1].split(","))
    for linea in archLoc.readlines():
        lstLoc.append(linea[:-1].split(","))
    for i in range(len(lstProv)):
        if int(lstProv[i][0])==idProv:
            nombreCiudad=lstProv[i][1]
    for i in range(len(lstLoc)):
        if int(lstLoc[i][2])==idProv:
            cantHab+=int(lstLoc[i][4])
    print("{}: {} Habitantes".format(nombreCiudad,cantHab))
    archProv.close
    archLoc.close
def localidadMaxima():
    archProv=open("Practica 7 Ej 8 Provincias.txt","r")
    archLoc=open("Practica 7 Ej 8 Localidades.txt","r")
    archPais=open("Practica 7 Ej 8 Paises.txt","r")
    lstProv=[]
    lstLoc=[]
    lstPais=[]
    habMax=int()
    for linea in archProv.readlines():
        lstProv.append(linea[:-1].split(","))
    for linea in archLoc.readlines():
        lstLoc.append(linea[:-1].split(","))
    for linea in archPais.readlines():
        lstPais.append(linea[:-1].split(","))
    archProv.close
    archLoc.close
    archPais.close
    for i in range (len(lstLoc)):
        if int(lstLoc[i][4])>habMax:
            habMax=int(lstLoc[i][4])
            i2=i
    print("Poblacion: {}".format(habMax))
    print("Localidad: {}".format(lstLoc[i2][1]))
    for i in range (len(lstProv)):
        if lstProv[i][0]==lstLoc[i2][2]:
            print("Provincia: {}".format(lstProv[i][1]))
            i3=i
    for i in range(len(lstPais)):
        if lstPais[i][0]==lstProv[i3][2]:
            print("Pais: {}".format(lstPais[i][1]))
def main():
    poblacion(1)
    localidadMaxima()
main()
"""