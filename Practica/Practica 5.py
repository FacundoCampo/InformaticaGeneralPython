"""
#Ej. 1: Desarrollar una función que reciba una palabra como parámetro y retorne otra palabra
#conformada por tres copias de los últimos dos caracteres de la palabra recibida. La
#palabra que recibida por parámetro debe tener un largo mínimo de dos caracteres en
#caso contrario deberá retornar una palabra vacía. Desde el programa principal ingresar
#por teclado una palabra, invocar a la función y mostrar por pantalla el resultado que
#retorna la función tal como se ilustra en los siguientes ejemplos:
def pal(t):
    nueva_pal=(t[-2:])*3
    return nueva_pal
def main():
    texto=str(input("Ingrese texto: "))
    if (len(texto)>2):
        print("La funcion ha retornado: {}".format(pal(texto)))
    else:
        print("La funcion ha retornado una palabra vacia")
main()
"""
"""
#Ej. 2: Dado un string de dos caracteres denominado “extremos” (por ejemplo “<>” o “$$”) y
#otro string que contiene una palabra, desarrollar una función que reciba ambos strings
#como parámetros y que retorne un nuevo string donde la palabra se encuentre en el
#medio de los caracteres “extremos”. En caso de qué “extremos” no contenga dos
#elementos o en caso de qué “palabra” sea vacío, la función deberá retornar un string
#vacío. Desde el programa principal ingresar por teclado los extremos y la palabra,
#invocar a la función y mostrar por pantalla el resultado que retorna la función tal como se
#ilustra en los siguientes ejemplos
def funcion(ext,pal):
    if (len(ext)==2):
        nueva_pal=(ext[0]+pal+ext[1])
    if (len(ext)!=2):
        nueva_pal="La funcion ha retornado una palabra vacia"
    return nueva_pal
def main():
    extremos=str(input("Ingrese dos extremos: "))
    palabra=str(input("Ingrese una palabra: "))
    print(funcion(extremos,palabra))
main()
"""
"""
#Ej. 3: Desarrollar la función primeraMitad que reciba una palabra de longitud par como
#parámetro, y que genere y retorne un string que contenga la primera mitad de dicha
#palabra. Desde el programa principal ingresar por teclado la palabra, invocar a la función
#y mostrar por pantalla el resultado que retorna la función. Para el caso que el texto
#ingresado no sea una palabra (o sea contenga otros caracteres que no sean letras) o
#que no sea de longitud par, se deberá pedir al usuario que realice el ingreso
#nuevamente, dándole al mismo todas las oportunidades que sean necesarias (validación
#del ingreso).
def es_letra(pal):
    bandera=True
    if bandera==True:
        for l in range(0,len(pal)):
            if not ("a"<=pal[l] and pal[l]<="z") or ("A"<=pal[l] and pal[l]<="Z"):
                bandera=False
    return bandera
def primera_mitad(pal):

    nueva_pal=pal[0:int(len(pal)/2)]
    return nueva_pal
def main():
    p=str(input("Ingrese una palabra: "))
    while (es_letra(p)==False) or ((len(p))%2!=0):
        p=str(input("Ingrese una palabra: "))
    print(primera_mitad(p))
main()
"""
"""
#Ej. 4: Desarrollar una función booleana principioFin que reciba como parámetro un texto y
#detecte si la primera palabra del texto es exactamente igual a la última.
#Por Ejemplo:
#“Barón!, urgente ya ha nacido! Es un varón!” → False
#“Entre que ya se vienen los hombres de enfrente” → False
#“Hombre de poca fe, he dicho! Vamos, vamos hombre!” → True
#Desde el programa principal ingresar por teclado un texto, invocar a la función y mostrar
#por pantalla un mensaje que indique si cumple o no con la condición. Ejemplo:
def es_letra(l):
    bandera=True
    if bandera==True:
        if (("a"<=l and l<="z") or ("A"<=l and l<="Z") or l=="á" or l=="é" or l=="í" or l=="ó" or l=="ú" or l=="Á" or l=="É" or l=="Í" or l=="Ó" or l=="Ú"):
            bandera=True
        else:
            bandera=False
    return bandera
def principio_fin(texto):
    primera_pal=""
    ultima_pal=""
    band_prim_pal=True
    band_ult_pal=True
    for l in range(0,len(texto)):
        if es_letra(texto[l])==True and band_prim_pal==True:
            if ("A"<=texto[l] and "Z">=texto[l]):
                primera_pal+=chr(ord(texto[l])+32)
            else:
                primera_pal+=texto[l]
        if es_letra(texto[l])!=True and primera_pal!="":
            band_prim_pal=False
        l+=1
    for l_ult in range(1,(len(texto))-1):
        if es_letra(texto[l_ult*-1])==True and band_ult_pal==True:
            if ("A"<=texto[l_ult] and "Z">=texto[l_ult]):
                ultima_pal+=chr(ord(texto[l_ult*-1])+32)
            else:
                ultima_pal+=texto[l_ult*-1]
        if es_letra(texto[l_ult*-1])!=True and ultima_pal!="":
            band_ult_pal=False
        l_ult+=1
    if primera_pal == ultima_pal[::-1]:
        result=True
    else:
        result=False
    return result
def main():
    t=str(input("Ingresar un texto: "))
    print(principio_fin(t))
main()
"""
"""
#Ej. 5: Desarrollar la función rotacion que a partir de un string pasado como parámetro
#genere y retorne un nuevo string en donde la primera mitad del string cambia con la
#segunda mitad. Desde el programa principal ingresar por teclado un texto, invocar a la
#función y mostrar por pantalla el resultado que retorna la función. Para el caso que el
#texto ingresado no sea de longitud par y mayor a dos, se deberá pedir al usuario que
#realice el ingreso nuevamente, dándole al mismo todas las oportunidades que sean
#necesarias (validación del ingreso).
def rotacion(texto):
    cont_texto= int(len(texto))
    primera_parte=texto[0:int(cont_texto/2)]
    segunda_parte=texto[int(cont_texto/2):cont_texto]
    result=(segunda_parte+primera_parte)
    return result
def main():
    t=str(input("Ingrese palabra: "))
    while len(t)%2!=0 or len(t)<2:
        t=str(input("ERROR, ingrese palabra: "))
    print(rotacion(t))
main()
"""
"""
#Ej. 6: Desarrollar una función booleana que retorne verdadero ( True ) en el caso de que una
#frase recibida como parámetro sea palíndroma y falso ( False ) si no lo es. Una frase es
#palíndroma cuando leída al derecho o al revés dice lo mismo. Desde el programa
#principal ingresar por teclado una frase, invocar a la función y mostrar por pantalla un
#mensaje que indique si la frase es o no es palíndroma.
def es_letra(l):
    if ("a"<=l and "z">=l) or ("A"<=l and "Z">=l) or l=="á" or l=="é" or l=="í" or l=="ó" or l=="ú" or l=="Á" or l=="É" or l=="Í" or l=="Ó" or l=="Ú":
        result=True
    else:
        result=False
    return result
def palindroma(texto):
    nueva_pal=""
    for letra in range(0,len(texto)):
        if es_letra(texto[letra])==True:
            if texto[letra]=="á" or texto[letra]=="Á":
                nueva_pal+="a"
            elif texto[letra]=="é" or texto[letra]=="É":
                nueva_pal+="e"
            elif texto[letra]=="í" or texto[letra]=="Í":
                nueva_pal+="i"
            elif texto[letra]=="ó" or texto[letra]=="Ó":
                nueva_pal+="o"
            elif texto[letra]=="ú" or texto[letra]=="Ú":
                nueva_pal+="u"
            elif "A"<=texto[letra] and texto[letra]<="Z":
                nueva_pal+=chr(ord(texto[letra])+32)
            else:
                nueva_pal+=texto[letra]
        letra+=1
    if nueva_pal==nueva_pal[::-1]:
        result="Es palindroma"
    else:
        result="NO es palindroma"
    return result
def main():
    t=str(input("Ingrese un texto: "))
    print(palindroma(t))
main()
"""
"""
#Ej. 7: Desarrollar una función que reciba por parámetros dos textos: uno “largo” y otro “corto” y
#retorne la cantidad de veces que se encuentra repetido el texto “corto” dentro del texto
#“largo”. Desde el programa principal ingresar por teclado el texto largo y el texto corto a
#buscar, luego invocar a la función y mostrar por pantalla el resultado que retorna.
def largo(texto_largo,texto_corto):
    contador=0
    for largo in range(0,len(texto_largo)):
        if (texto_largo[largo:len(texto_corto)+largo])== texto_corto:
            contador+=1
        largo+=1
    return contador
def main():
    tl=str(input("Ingrese texto largo: "))
    tc=str(input("Ingrese texto corto: "))
    print("El texto corto se encontro {} veces en el texto largo".format(largo(tl,tc)))
main()
"""
"""
#Ej. 8: Desarrollar una función que reciba por parámetro un texto (string) y retorne un nuevo
#texto (string), con el mismo texto, con todas sus palabras con la primera letra en
#mayúscula.
#Desde el programa principal ingresar por teclado un texto, invocar a la función y mostrar
#por pantalla el resultado que retorna la función.
def es_letra(l):
    if ("a"<=l and "z">=l) or ("A"<=l and "Z">=l) or l=="á" or l=="é" or l=="í" or l=="ó" or l=="ú" or l=="Á" or l=="É" or l=="Í" or l=="Ó" or l=="Ú":
        result=True
    else:
        result=False
    return result
def primera_letra_mayuscula(texto):
    nueva_pal=""
    pal=""
    for l in range(0,len(texto)):
        if es_letra(texto[l])==True:
            nueva_pal+=texto[l] 
        if es_letra(texto[l])!=True:
            if "a"<=nueva_pal[0] and nueva_pal[0]<="z":
                pal+=(chr(ord(nueva_pal[0])-32) + nueva_pal[1:len(nueva_pal)])
            if "A"<=nueva_pal[0] and nueva_pal[0]<="Z":
                pal+=nueva_pal
            pal+=texto[l]
            nueva_pal=""
        l+=1
    return pal
def main():
    t=str(input("Ingrese texto: "))
    print(primera_letra_mayuscula(t+" "))
main()
"""
"""
#Ej. 9: Escribir un programa que permita ingresar un texto de longitud indefinida e informe por
#pantalla:
#a – La cantidad de palabras que contiene el texto
#b – La palabra de mayor longitud
#c – La palabra de menor longitud
#Para cada uno de los puntos anteriores desarrollar una función que recibe el texto como
#parámetro y retorna lo correspondiente al punto. Estas tres funciones deben ser
#utilizadas por el programa principal el cual informará los resultados.
def es_letra(l):
    if ("a"<=l and "z">=l) or ("A"<=l and "Z">=l) or l=="á" or l=="é" or l=="í" or l=="ó" or l=="ú" or l=="Á" or l=="É" or l=="Í" or l=="Ó" or l=="Ú":
        result=True
    else:
        result=False
    return result
def pal(texto):
    cont_pal=0
    pal=""
    for p in range(0,len(texto)):
        if es_letra(texto[p])==True:
            pal+=texto[p]
        elif es_letra(texto[p])!=True and pal!="":
            cont_pal+=1
            pal=""
    return cont_pal
def maximo(texto):
    bandera_maximo=""
    pal=""
    for p in range(0,len(texto)):
        if es_letra(texto[p])==True:
            pal+=texto[p]
        if es_letra(texto[p])!=True and pal!="":
            if bandera_maximo=="":
                bandera_maximo=pal
            elif len(bandera_maximo)<len(pal):
                bandera_maximo=pal
            pal=""
    return bandera_maximo
def menor(texto):
    bandera_minimo=""
    pal=""
    for p in range(0,len(texto)):
        if es_letra(texto[p])==True:
            pal+=texto[p]
        if es_letra(texto[p])!=True and pal!="":
            if bandera_minimo=="":
                bandera_minimo=pal
            elif len(bandera_minimo)>len(pal):
                bandera_minimo=pal
            pal=""
    return bandera_minimo
def main():
    t=str(input("Ingrese un texto: "))
    print("El texto tiene {} palabras, la de mayor longitud es ´{}´y la de menor longitud es de ´{}´".format(pal(t+" "),maximo(t+" "),menor(t+" ")))
main()
"""
#Ej. 10: Desarrollar una función que reciba un texto t y una palabra p como parámetros, y
#retorne verdadero si encuentra al menos una palabra en t conformada exactamente
#con los mismos caracteres que conforman p sin importar el orden de los mismos en la
#palabra. Desde el programa principal ingresar por teclado el texto y la palabra, invocar a
#la función y mostrar por pantalla un mensaje que indique si cumple o no con la
#condición.
