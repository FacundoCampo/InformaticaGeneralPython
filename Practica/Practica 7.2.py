def agregarRegistro():
    archPers=open("Practica 7 Ej_7.txt","r")
    lstPers=[]
    for linea in archPers.readlines():
        lstPers.append(linea[:-1].split(","))
    archPers.close
    archPers2=open("Practica 7 Ej_7.txt","a")
    lstdni=[]
    for i in range(len(lstPers)):
        if not int(lstPers[i][2]) in lstdni:
            lstdni.append(int(lstPers[i][2]))
    dni=int(input("Ingrese el dni:"))
    while dni in lstdni:
        dni=int(input("Ingrese el dni:"))
    lstdni.append(dni)
    lstagr=[]
    nombre=str(input("Ingrese nombre: "))
    apellido=str(input("Ingrese apellido: "))
    archPers2.write("{},{},{}\n".format(nombre,apellido,dni))
    archPers2.close
def eliminarRegistro():
    arc=open("Practica 7 Ej_7.txt","r")
    lst=[]
    for linea in arc.readlines():
        lst.append(linea[:-1].split(","))
    arc.close
    arch=open("Practica 7 Ej_7.txt","w")
    lstDni=[]
    for i in range(len(lst)):
        lstDni.append(str(lst[i][2]))
    dni=str(input("Ingrese dni a borrar: "))
    while not dni in lstDni:
        dni=str(input("Ingrese dni a borrar: "))
    for i in range(len(lst)):
        if dni==lst[i][2]:
            lstDni.remove(lst[i][2])
    for i in range(len(lst)):
        if lst[i][2] in lstDni:
            arch.write(",".join(lst[i])+"\n")
    arch.close
def buscarRegistro():
    arch=open("Practica 7 Ej_7.txt","r")
    lst=[]
    for linea in arch.readlines():
        lst.append(linea[:-1].split(","))
    lstDni=[]
    lstApellido=[]
    for i in range(len(lst)):
        lstDni.append(lst[i][2])
        lstApellido.append(lst[i][1])
    num=int(input("Ingrese 0 para dni o 1 para apellido: "))
    while not (num>=0 and num<=1):
        num=int(input("ERROR, Ingrese 0 para dni o 1 para apellido: "))
    if num==0:
        dni=str(input("Ingrese dni a buscar: "))
        while not dni in lstDni:
            dni=str(input("Ingrese dni a buscar: "))
        for i in range(len(lst)):
            if lst[i][2]==dni:
                print(lst[i])
    if num==1:
        ap=str(input("Ingrese apellido a buscar: "))
        while not ap in lstApellido:
            ap=str(input("Ingrese apellido a buscar: "))
        for i in range(len(lst)):
            if lst[i][1]==ap:
                print(lst[i])
    arch.close
def ordenarArchivoPor():
    arch=open("Practica 7 Ej_7.txt","r")
    lst=[]
    for linea in arch.readlines():
        lst.append(linea[:-1].split(","))
    arch.close
    num=int(input("Ingrese 0 (nombre), 1 (apellido) o 2 (dni): "))
    while not (num>=0 and num<=2):
        num=int(input("ERROR, Ingrese 0 (nombre), 1 (apellido) o 2 (dni): "))
    arch=open("Practica 7 Ej_7.txt","w")
    if num==0:
        for i in range(len(lst)):
            for z in range(i+1,len(lst)):
                if lst[i][0]>lst[z][0]:
                    aux=lst[i]
                    lst[i]=lst[z]
                    lst[z]=aux
    elif num==1:
        for i in range(len(lst)):
            for z in range(i+1,len(lst)):
                if lst[i][1]>lst[z][1]:
                    aux=lst[i]
                    lst[i]=lst[z]
                    lst[z]=aux
    elif num==2:
        for i in range(len(lst)):
            for z in range(i+1,len(lst)):
                if int(lst[i][2])>int(lst[z][2]):
                    aux=lst[i]
                    lst[i]=lst[z]
                    lst[z]=aux
    for i in range(len(lst)):
        arch.write(",".join(lst[i])+"\n")
def main():
    print("1. AGREGAR REGISTRO\n2. ELIMINAR REGISTRO\n3. BUSCAR REGISTRO\n4. ORDENAR ARCHIVO POR\n5. MOSTRAR ARCHIVO\n6. SALIR")
    n=int(input("Ingrese el valor de la opción:"))
    while not (n>=1 and n<=6):
        print("1. AGREGAR REGISTRO\n2. ELIMINAR REGISTRO\n3. BUSCAR REGISTRO\n4. ORDENAR ARCHIVO POR\n5. MOSTRAR ARCHIVO\n6. SALIR")
        n=int(input("Ingrese el valor de la opción:"))
    if n==1:
        agregarRegistro()
    elif n==2:
        eliminarRegistro()
    elif n==3:
        buscarRegistro()
    elif n==4:
        ordenarArchivoPor()
    elif n==5:
        mostrarArchivo()
    elif n==6:
        print("Fin.")
main()