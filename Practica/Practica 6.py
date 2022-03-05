"""
#Ej. 1: Desarrollar la función estaEnLista qué recibe por parámetro un número entero num y
#una lista de enteros lst . La función debe retornar True si num se encuentra dentro de
#lst , caso contrario deberá retornar False.
#estaEnLista deberá ser desarrollada (y probada) de tres formas distintas, según el
#siguiente criterio:
#1.1. estaEnLista1 Utilizando sólo el operador IN para verificar si se encuentra un
#elemento en la lista.
#1.2. estaEnLista2 Recorriendo la lista con un ciclo for y realizando comparaciones
#elemento a elemento para verificar si se encuentra un elemento en la lista.
#1.3. estaEnLista3 Recorriendo la lista con un ciclo while y realizando
#comparaciones elemento a elemento para verificar si se encuentra un elemento
#en la lista.
def estaEnLista(num,lst):
    if (num in lst)==True:
        result=True
    else:
        result=False
    return result
def estaEnLista2(num,lst):
    bandera=False
    for i in range(len(lst)):
        if num==lst[i]:
            bandera=True
    return bandera
def estaEnLista3(num,lst):
    bandera=False
    band_len=0
    while band_len<len(lst):
        if lst[band_len]==num:
            bandera=True
        band_len+=1
    return bandera
def main():
    print(estaEnLista(23,[1,23,3,4]))
    print(estaEnLista2(23,[1,23,3,4]))
    print(estaEnLista3(23,[1,23,3,4]))
main()
"""
"""
#Ej. 2: Desarrollar la función cargarLista , que retorna una lista la cual será cargada desde el
#teclado con números enteros positivos ( lo cual deberá ser validado ) hasta que el
#usuario ingrese 0 (cero). Además, no se permitirá al usuario cargar dos veces el mismo
#valor. En caso de verificar un error de validación ( por repetido o por NO positivo ) se
#deberá mostrar un mensaje con el error que corresponda, permitiendo luego continuar
#con la carga de los siguientes números. Para determinar si un número se encuentra
#dentro de la lista se deberá verificar invocando a la función estaEnLista ( alguna de las
#realizadas del ejercicio anterior ).
#Los elementos dentro de la lista deben estar almacenados como números enteros y
#deberán ser tratados como tal.
#Desde el programa principal invocar a la función cargarLista , luego imprimir
#directamente el contenido de la lista en consola; como se indica en el ejemplo.
def cargarLista1():
    lst=[]
    print("Ingresar numeros,o 0 (cero ) para terminar:")
    num=int(input(""))
    while num!=0:
        lst.append(num)
        num1=int(input(""))
        while num1<0 or num1 in lst:
            if num1<0:
                num1=int(input("ERROR, el numero es menor a 0:"))
            elif num1 in lst:
                num1=int(input("ERROR, el numero es repetido:"))
        num=num1
    print (lst)
cargarLista1()
"""
"""
#Ej. 3:
def cargar_lista(lst):
    print("Ingresar numeros positivos, cortar con 0:")
    num=int(input(""))
    while num!=0:
        while num<0 or num in lst:
            if num<0:
                num=int(input("ERROR, ingrese numero positivo:"))
            elif num in lst:
                num=int(input("ERROR, Es igual:"))
        lst.append(num)
        num=int(input(""))

def cargar_conjuntos(lst1,lst2):
    cargar_lista(lst1)
    cargar_lista(lst2)

def union(lista1,lista2):
    lst_nueva=[]
    for i in range(len(lista1)):
        lst_nueva.append(lista1[i])
    for i in range(len(lista2)):
        if not lista2[i] in lst_nueva:
            lst_nueva.append(lista2[i])
    return lst_nueva
def interseccion(lista1,lista2):
    lst_interseccion=[]
    for i in range(len(lista1)):
        for j in range (len(lista2)):
            if lista1[i]==lista2[j]:
                lst_interseccion.append(lista2[j])
    return lst_interseccion
def diferencia(lista1,lista2):
    lst_diferencia=[]
    for i in range(len(lista1)):
        if not lista1[i] in lista2:
            lst_diferencia.append(lista1[i])
    return lst_diferencia
def diferencia_simetrica(lista1,lista2):
    lst_diferencia_simetrica=[]
    for i in range(len(lista1)):
        if not lista1[i] in lista2:
            lst_diferencia_simetrica.append(lista1[i])
    for i in range(len(lista2)):
        if not lista2[i] in lista1:
            lst_diferencia_simetrica.append(lista2[i])
    return lst_diferencia_simetrica
def main():
    print(" 1. CARGAR CONJUNTOS \n 2. UNION \n 3. INTERSECCION \n 4. DIFERENCIA (A-B) \n 5. DIFERENCIA SIMÉTRICA \n 6. SALIR\n")
    opcion=int(input("Ingrese el valor de la opción(para cerrar el programa 0): "))
    lst1=[]
    lst2=[]
    while opcion!=6:
        if opcion==1:
            cargar_conjuntos(lst1,lst2)
        elif opcion==2:
            print(union(lst1,lst2))
        elif opcion==3:
            print(interseccion(lst1,lst2))
        elif opcion==4:
            print(diferencia(lst1,lst2))
        elif opcion==5:
            print(diferencia_simetrica(lst1,lst2))
        elif opcion<1 or opcion>6:
            print("ERROR, NUMERO EQUIVOCADO")
        print(" 1. CARGAR CONJUNTOS \n 2. UNION \n 3. INTERSECCION \n 4. DIFERENCIA (A-B) \n 5. DIFERENCIA SIMÉTRICA \n 6. SALIR\n")
        opcion=int(input(""))
        if opcion==6:
            print("Su programa se ha cerrado.")
main()
"""
"""
#Ej.4
import random
def cargaListaAleat(mini,maxi,can):
    lista_aleatoria=[]
    while len(lista_aleatoria)<can:
        i=random.randint(mini,maxi)
        if i>0:
            lista_aleatoria.append(i)
    return ("La lista aleatoria es: {}, el minimo es: {} y el maximo es: {}".format(lista_aleatoria,minVal(lista_aleatoria),maxVal(lista_aleatoria)))
def minVal(lst):
    mini=""
    for i in range(len(lst)):
        if mini=="":
            mini=lst[i]
        elif mini>lst[i]:
            mini=lst[i]
    if len(lst)==0:
        mini= "NONE"
    return mini
def maxVal(lst):
    maxi=""
    for i in range(len(lst)):
        if maxi=="":
            maxi=lst[i]
        elif maxi<lst[i]:
            maxi=lst[i]
    if len(lst)==0:
        maxi= "NONE"
    return maxi
def main():
    ext1=int(input("Ingrese el primer extremo:"))
    ext2=int(input("Ingrese el segundo extremo: "))
    can=int(input("Ingrese la cant de numero generados: "))
    if ext1>ext2:
        maxi=ext1
        mini=ext2
    else:
        maxi=ext2
        mini=ext1
    print(cargaListaAleat(mini,maxi,can))
main()
"""
"""
#Ej.5
import random
def cargaLista(lst):
    n=int(input("Ingrese un numero(Cierra con 0)"))
    while n!=0:
        lst.append(n)
        n=int(input("Ingrese un numero(Cierra con 0)"))
    return lst
def listaModificada(ext1,ext2,lst):
    lista_nueva=[]
    for i in range(len(lst)):
        if ext1>lst[i] or lst[i]>ext2:
            n=random.randint(ext1,ext2)
            while ext1>n or n>ext2:
                n=random.randint(ext1,ext2)
            lista_nueva.append(n)
        else:
            lista_nueva.append(lst[i])
    return lista_nueva
def main():
    lst=[]
    n_lst= cargaLista(lst)
    print(n_lst)
    ext1=int(input("Ingresar el extremo menor: "))
    ext2=int(input("Ingresar el extremo mayor: "))
    print(listaModificada(ext1,ext2,n_lst))
main()
"""
"""
#Ej.6
def ordenarLST(lst):
    lst_nueva=[]
    for i in range(len(lst)):
        for x in range(0,len(lst)):
            if lst[i]<lst[x]:
                aux=lst[i]
                lst[i]=lst[x]
                lst[x]=aux
    return lst
def main():
    lst=[]
    print("Ingrese una lista(finalice con 0")
    num=int(input(""))
    while num!=0:
        lst.append(num)
        num=int(input(""))
    print("Lista generada {}".format(lst))
    print("Lista ordenada {}".format(ordenarLST(lst)))
main()
"""
"""
#Ej.7
def ingresarLst(lst):
    print("Ingresar lista(Terminar con 0)")
    num=int(input(""))
    while num!=0:
        lst.append(num)
        num=int(input(""))
    return lst
def imprimirLst(lst):
    print("Lista generada: \n{}".format(lst))
def inserOrd(lst,num):
    for i in range(len(lst)):
        if lst[i]>num:
            lst.insert(i,num)
            return lst               
def main():
    lst=[]
    lista=ingresarLst(lst)
    imprimirLst(lista)
    num=int(input("Ingrese valor a insertar: "))
    print(inserOrd(lista,num))
main()
"""
"""
#ej.8
def inserOrd(lst,num):
    for i in range(len(lst)):
        if lst[i]>num:
            lst.insert(i,num)
            return lst
    lst.append(num)
    return lst
def cargaLst(lst):
    num=int(input("Ingrese una lista(finalice con cero):\n"))
    while num!=0:
        inserOrd(lst,num)
        num=int(input(""))
    return lst
def main():
    lst=[]
    print(cargaLst(lst))
main()
"""
"""
#Ej.9
def cargarLstAlu(lst):
    lst_alu=[]
    numero=int(input("Ingrese 1 (para agregar a la lista) o Ingrese 0(para finalizarla):"))
    while numero!=0:
        while numero !=1:
            numero:int(input("ESE NUMERO ES INCORRECTO:"))
        dni=int(input("Ingrese el dni: "))
        lst_alu.append(dni)
        nombre=str(input("Ingrese nombre: "))
        lst_alu.append(nombre)
        edad=int(input("Ingrese la edad"))
        lst_alu.append(edad)
        lst.append(lst_alu)
        lst_alu=[]
        numero=int(input("Ingrese 1 (para agregar a la lista) o Ingrese 0(para finalizarla):"))
    return lst
def ordenarAluXDNI(lst):
    for i in range(len(lst)):
        for x in range(i+1,len(lst)):
            if lst[i][0]>lst[x][0]:
                aux=lst[i]
                lst[i]=lst[x]
                lst[x]=aux
    return lst
def main():
    lst=[]
    lst_n=cargarLstAlu(lst)
    print(lst_n)
    print(ordenarAluXDNI(lst_n))
main()
"""
"""
#Ej.10
import random
def cargarListaAleat(ext1,ext2,can):
    lst=[]
    while len(lst)<can:
        lst.append(random.randint(ext1,ext2))
    return lst
def atributoTriple(lst):
    cont=0
    i=0
    while i<len(lst)-2:
        if lst[i]==lst[i+1] and lst[i]==lst[i+2]:
            cont+=1
        i+=1
        
    if cont==1:
        result="Un triple"
    elif cont==2:
        result="Dos triples"
    elif cont>=3:
        result="+Triples"
    else:
        result="nada"
    return result
def main():
    lst_n=cargarListaAleat(1,3,15)
    print(lst_n)
    atributoTriple(lst_n)
    print(atributoTriple(lst_n))
main()
"""
"""
#Ej.11
import random
def ruleta():
    lst=[]
    num=int(input("Ingrese un numero positivo:"))
    while len(lst)<num:
        lst.append(random.randint(0,36))
    return lst
def porcentaje(lst):
    cont=0
    lstX=[]

    for i in range(len(lst)):
        if not lst[i] in lstX:
            lstX.append(lst[i])
    
    for j in range(len(lstX)):
        for k in range(len(lst)):
            if lstX[j]==lst[k]:
                cont+=1
        porcen=int((cont*100)/len(lst))
        print("El número {} salió {} vez ({}%).".format(lstX[j],cont,porcen))
        cont=0
            
def main():
    lista= ruleta()
    print(lista)
    porcentaje(lista)
main()
"""
"""
#Ej.12
def operaciones(a,b):       
    suma=a+b
    resta=a-b
    producto=a*b
    if b==0:
        division="none"
    else:
        division=a/b
    tupla=(suma,resta,producto,division)
    return tupla
def main():
    print(operaciones(54,0))
main()
"""
"""
#Ej.13
def agregarDicEle(dic):
    clave=int(input("Ingrese un numero clave (0 para cerrar): "))
    while clave!=0:
        valor=str(input("Ingrese el numero clave en letras: "))
        dic[clave]="{}".format(valor)
        clave=int(input("Ingrese un numero clave (0 para cerrar): "))
    return dic
def main():
    dic={}
    dic=agregarDicEle(dic)
    num=int(input("Ingresar número a traducir o cero para salir: "))
    while num!=0:
        print("{} -> {}".format(num,dic[num]))
        num=int(input("Ingresar número a traducir o cero para salir: "))
    print(dic)
main()
"""
"""
#Ej.14
def agregarDicEle2(dic):
    clave=int(input("Ingrese un numero clave (0 para cerrar): "))
    while clave!=0:
        valorSP=str(input("Ingrese el numero clave en letras(español): "))
        valorEN=str(input("Ingrese el numero clave en letras(ingles): "))
        valorDE=str(input("Ingrese el numero clave en letras(aleman): "))
        dic[clave]=(valorSP,valorEN,valorDE)
        clave=int(input("Ingrese un numero clave (0 para cerrar): "))
    return dic
def main():
    print("Ingrese un diccionario")
    dic={}
    dic=agregarDicEle2(dic)
    print(dic)
    num=int(input("Ingrese el numero que quiere traducir(0 para cerrar): "))
    while num!=0:
        pos=str(input("Ingrese el idioma que quiere(SP,EN,DE): "))
        if pos=="SP":
            print(dic[num][0])
        elif pos=="EN":
            print(dic[num][1])
        elif pos=="DE":
            print(dic[num][2])
        num=int(input("Ingrese el numero que quiere traducir(0 para cerrar): "))
main()
"""
"""
#Ej.15
def agregarDicEle3():
    dic={}
    clave=int(input("Ingrese el dni como clave: "))
    while clave!=0:
        nombre=str(input("Ingrese el nombre: "))
        apellido=str(input("Ingrese el apellido: "))
        notas=int(input("ingrese las notas finalice con 0: "))
        lst_nota=[]
        while notas!=0:
            lst_nota.append(notas)
            notas=int(input("Ingrese las notas, finalice con 0: "))
        dic[clave]=[[nombre,apellido],lst_nota]
        clave=int(input("Ingrese el dni como clave: "))
    return dic
def impirmirDic(dic):
    print(dic)
def imprimirDicOrd(dic):
    lstclaves=list(dic.keys())
    for i in range(len(lstclaves)-1):
        for j in range(i+1,len(lstclaves)):
            if lstclaves[i]>lstclaves[j]:
                aux=lstclaves[i]
                lstclaves[i]=lstclaves[j]
                lstclaves[j]=aux
    for i in lstclaves:
        print(i,":",dic[i],end=" ")
def main():
    dic=agregarDicEle3()
    impirmirDic(dic)
    imprimirDicOrd(dic)
main()
"""