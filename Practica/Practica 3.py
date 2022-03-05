"""
#Ej. 1: Desarrollar una función que reciba como parámetros dos números y un string con alguno
#de los cuatro caracteres (+,-,*,/) y retorne el resultado de la operación. Desde el
#programa principal el usuario ingresará los datos que serán pasados como parámetros a
#la función y mostrará el resultado retornado por la misma.
def cuenta(num1,num2,oper):
    if oper == "+":
        tot = num1 + num2
    elif oper == "-":
        tot = num1 - num2
    elif oper == "/":
        tot = num1/num2
    elif oper == "*":
        tot = num1*num2
    return tot
def main():
    n1=int(input("Ingrese el primer número: "))
    n2=int(input("Ingrese el segundo número: "))
    op=str(input("Ingrese la operación (+, -, *, /): "))
    print("{} {} {} = {}".format(n1,op,n2,cuenta(n1,n2,op)))
main()
"""
"""
#REHACER
#Ej. 2: Desarrollar una función que reciba tres números como parámetros, e imprima en
#pantalla los números pasados por parámetro de forma ordenada ascendentemente . La
#función debe ser invocada desde un programa que solicite el ingreso por teclado de los
#números.
def orden(a,b,c):
    if (c < b) and (b < a):
        result= ("{}\n{}\n{}\n".format(c,b,a))
    elif (c < a) and (a < b):
        result= ("{}\n{}\n{}\n".format(c,a,b))
    elif (a < b) and (b < c):
        result= ("{}\n{}\n{}\n".format(a,b,c))
    elif (a < c) and (c < b):
        result= ("{}\n{}\n{}\n".format(a,c,b))
    elif (b < a) and (a < c):
        result= ("{}\n{}\n{}\n".format(b,a,c))
    elif (b < c) and (c < a):
        result= ("{}\n{}\n{}\n".format(b,c,a)) 
    return result
def main():
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    n3=int(input("Ingrese el tercer numero: "))
    print("Los números ordenados en forma ascendente son:\n{}".format(orden(n1,n2,n3)))
main()
"""
"""
#Ej. 3: Desarrollar una función que reciba un número real como parámetro y que retorne un
#mensaje si el número es “positivo”, “negativo” o “cero” . Adicionalmente deberá
#desarrollar otra función, que retorne otro mensaje, si el número recibido es “entero
#natural”, “entero” o “real” . El programa principal deberá efectuar el ingreso de
#un número real e imprimir por pantalla los mensajes retornados por las funciones.
def positiv(nR):
    if nR == 0:
        resultP= "cero"
    elif nR > 0:
        resultP= "positivo"
    elif nR < 0:
        resultP= "negativo"
    return resultP
def ent(nReal):
    if int(nReal) == nReal:
        if (nReal > 0):
            resultE= "Entero natural"
        if (nReal <= 0):
            resultE= "Entero"
    if int(nReal) != nReal:
        resultE= "Real"
    return resultE
def main():
    a=float(input("Ingrese un número: "))
    print("El número es {} y {}.".format(positiv(a),ent(a)))
main()
"""
"""
#Ej. 4: Desarrollar una función booleana que reciba como parámetro dos números enteros ( que
#no están en orden ) y valide si la resta entre el número mayor y el número menor es un
#valor que se encuentra entre ambos números ( es decir, la diferencia es mayor e igual que el
#más chico y menor e igual que el más grande de los valores recibidos ). Escribir un programa
#que ingrese por teclado los dos valores, invoque a la función y muestre por pantalla si
#cumplen o no con la condición.
def bol(n1,n2):
    if n1>=n2:
        maxi=n1
        mini=n2
        val= maxi-mini
        if mini<=val and val<=maxi:
            ret= "Si"
        else:
            ret= "No"
    elif n2>=n1:
        maxi=n2
        mini=n1
        val= maxi-mini
        if mini<=val and val<=maxi:
            ret= "Si"
        else:
            ret= "No"
    return ret
    
def main():
    a=int(input("Ingrese un número A: "))
    b=int(input("Ingrese un numero B: "))
    print("{} cumple la condicion.".format(bol(a,b)))
main()
"""
"""
#Ej. 5: Desarrollar una función booleana que reciba como parámetros tres números enteros
#positivos que representan el día, el mes y el año de una fecha. La función deberá
#retornar verdadero ( True ) si la fecha es válida caso contrario deberá retornar falso
#( False ).
#Desde el programa principal ingresar por teclado el día, mes y año por separado, invocar
#a la función y mostrar por pantalla un mensaje indicando si la fecha es correcta o no.
#Ayuda : Un año es bisiesto si es múltiplo de 4 y no de 100, o es múltiplo de 400. Por
#ejemplo el año 2000 es bisiesto pero el 1800 no lo es.
def fecha(d,m,a):
    if m==2 and d==29 and ((((a%4) == 0) and ((a%100) != 0)) or (a%400) == 0):
        result= "Es correcta"
    elif ((m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and d<=31 and d>0):
        result= "Es correcta"
    elif ((m==4 or m==6 or m==9 or m==11) and d<=30 and d>0) or (m==2 and 28>=d and d>0):
        result= "Es correcta"
    else:
        result= "No es correcta"
    return result
def main():
    dia=int(input("Ingrese el día: "))
    mes=int(input("Ingrese el mes: "))
    año=int(input("Ingrese el año: "))
    print("La fecha es: {}".format(fecha(dia,mes,año)))
main()
"""
"""
# Ej. 6: Desarrollar una función booleana que reciba como parámetro un número entero positivo.
# Si el número recibido es par solicitará que se ingrese un número menor, y si es impar se
# solicitará que se ingrese mayor. La función deberá verificar si el ingreso es correcto
# retornando verdadero ( True ) o incorrecto retornando falso ( False ).
# Desde el programa principal ingresar por teclado el número entero positivo, invocar a la
# función e imprimir un mensaje indicando si es “ Correcto!” o “ Incorrecto!” según el
# resultado que retorna por la función.
def booleana(n1):
    if (n1%2)==0 and n1>0:
        nMenor=int(input("Ingrese un numero menor: "))
        if nMenor<n1:
            result="True"
        else:
            result="False"
    if (n1%2)!=0 and n1>0:
        nMayor=int(input("Ingrese un numero mayor:"))
        if nMayor>n1:
            result="True"
        else:
            result="False"
    return result
def main():
    a=int(input("Ingrese un número entero positivo: "))
    print(booleana(a))
main()
"""
"""
# Ej. 7: Desarrollar una función booleana que reciba como parámetros tres números enteros sin
# un orden en particular. Luego debe verificar si el promedio entre el mayor y el menor es
# exactamente igual al número restante, ( es decir: los extremos están igualmente
# distanciados del intermedio ), retornando verdadero ( True ) si cumple la condición o falso
# ( False ) en caso contrario.
# Desde el programa principal ingresar por teclado tres números enteros, invocar a la
# función e imprimir un mensaje indicando si los tres valores “ Están igualmente
# distanciados!” o “ NO Están igualmente distanciados!” según el resultado retornado
# por la función.

def booleana(n1,n2,n3):
    if n1<n2<n3:
        nMax=n3
        nMin=n1
        nMedio=n2
        if (nMax-nMedio)==(nMedio-nMin):
            result= "True"
        else:
            result="False"
    elif n1<n3<n2:
        nMax=n2
        nMin=n1
        nMedio=n3
        if (nMax-nMedio)==(nMedio-nMin):
            result= "True"
        else:
            result="False"
    elif n2<n3<n1:
        nMax=n1
        nMin=n2
        nMedio=n3
        if (nMax-nMedio)==(nMedio-nMin):
            result= "True"
        else:
            result="False"
    elif n2<n1<n3:
        nMax=n3
        nMin=n2
        nMedio=n1
        if (nMax-nMedio)==(nMedio-nMin):
            result= "True"
        else:
            result="False"
    elif n3<n1<n2:
        nMax=n2
        nMin=n3
        nMedio=n1
        if (nMax-nMedio)==(nMedio-nMin):
            result= "True"
        else:
            result="False"
    elif n3<n2<n1:
        nMax=n1
        nMin=n3
        nMedio=n2
        if (nMax-nMedio)==(nMedio-nMin):
            result= "True"
        else:
            result="False"
    else:
        result="False"
    return result
def main():
    n1=int(input("Ingresar el primer numero:"))
    n2=int(input("Ingresar el segundo numero:"))
    n3=int(input("Ingresar el tercer numero:"))
    print(booleana(n1,n2,n3))
main()
"""
"""
# Ej. 8: Realizar un programa que solicite 3 notas de parciales obtenidas por un alumno. A
# continuación se mostrará por pantalla un mensaje que indique la situación del alumno:
# ● Si el alumno aprobó los 3 parciales (nota 4 o más) y su promedio es mayor a 7,
# promociona la materia con la nota promedio.
# ● Si el alumno aprobó los 3 parciales pero su promedio no supera los 7 puntos,
# debe rendir examen final.
# ● Si el alumno no aprobó uno o más parciales, se solicitará que se ingrese la nota
# de un recuperatorio. Si éste hubiera sido aprobado, se informará el promedio
# general ( 3 parciales + el recuperatorio ) y su condición de aprobado ( aún cuando
# el promedio no supere los 4 puntos ). Si no hubiera aprobado el recuperatorio se
# informará que el alumno fue aplazado.
# Desarrollar dos funciones: una que reciba como parámetro las tres notas de los
# parciales, y calcule y retorne el valor del promedio. Y otra que reciba las tres notas de
# parciales y la nota del recuperatorio, y retorne el promedio general (de las cuatro notas).

def prom(n1,n2,n3):
    promedio=(n1+n2+n3)/3
    if promedio>=7:
        result=("{}\nPromociona".format(promedio))
    else:
        result=("{}\nDebe ir a final".format(promedio))
    return result
    
def promGeneral(n1,n2,n3,n4):
    promedioG=(n1+n2+n3+n4)/4
    if n4>=4:
        result=("{}\nDebe ir a final".format(promedioG))
    else:
        result=("{}\nFue aplazado".format(promedioG))
    return result
def main():
    n1=int(input("Ingrese la nota del primer parcial:")) 
    n2=int(input("Ingrese la nota del segundo parcial:")) 
    n3=int(input("Ingrese la nota del tercer parcial:"))
    if (n1>=4 and n2>=4 and n3>=4):
        print(prom(n1,n2,n3))
    elif (n1<4 or n2<4 or n3<4):
        
        n4=int(input("Ingrese la nota del recuperatorio:"))
        
        print(promGeneral(n1,n2,n3,n4))
main()
"""
"""
#Ej. 9: Una empresa necesita calcular el sueldo total que dará a sus empleados a fin de este
#año. Para ello se sigue el siguiente criterio:
#● Si el sueldo base supera los $2000, el bono será del 15%. De lo contrario, el
#bono será del 20%.
#● Además, recibirá un plus , de acuerdo al siguiente criterio:
#○ Si el empleado tiene hijos se suma un plus del 5% del sueldo.
#○ Si el empleado pertenece a la categoría 1, 2 ó 3, recibe un 10% del sueldo.
#Si pertenece a la categoría 4, 5 ó 6, recibe un 12% del sueldo. Si es de la
#categoría 7, 8 ó 9, recibe un 20% del sueldo pero no cobra el plus por tener
#hijos.
#Realizar un programa que solicite al usuario la información necesaria ( sueldo base,
#hijos(s/n) y categorí a) para luego calcular el sueldo total . Para el cálculo del sueldo total
#se deberá resolver invocando a las siguientes funciones:
#● La primer función: bono recibe por parámetro el sueldo base, luego calcula y
#retorna el valor del bono.
#● La segunda función: plus recibe por parámetro el sueldo base y si tiene hijos o
#no (boolena) y la categoría. Esta función debe retornar la suma del plus por hijo
#más el plus por categoría. Para resolver al plus por hijo, deberá invocar a plusH
#y para resolver el plus por categoría deberá invocar a plusC .
#● La tercera función: plusH recibe dos parámetros; el sueldo base y otra variable
#(boolena) que indica si tiene hijos(True) o no tiene hijos (False). Luego calcula y
#retorna el plus por hijos
#● La cuarta función: plusC recibe por parámetro el sueldo base y el número de
#categoría, luego calcula y retorna el plus por categoría.
#Desde el programa principal solicitar al usuario el ingreso de los datos, luego invocar a
#las funciones que correspondan, y por último mostrar por pantalla el total a pagar al
#empleado.
def bono(sueldo):
    if sueldo>=2000:
        result=sueldo*0.15
    else:
        result=sueldo*0.20
    return result
def plus(sueldo,hijo,cat):
    if (cat==1) or (cat==2) or (cat==3) or (cat==4) or (cat==5) or (cat==6):
        result= plusH(sueldo,hijo) + plusC(sueldo,cat)
    else:
        result=plusC(sueldo,cat)
    return result 
def plusH(sueldo,hijo):
    if hijo=="s":
        plusHijo=sueldo*0.05
    else:
        plusHijo=0
    return plusHijo
def plusC(sueldo,categoria):
    if (categoria==1) or (categoria==2) or (categoria==3):
        plusCat=sueldo*0.10
    elif (categoria==4) or (categoria==5) or (categoria==6):
        plusCat=sueldo*0.12
    elif (categoria==7) or (categoria==8) or (categoria==9):
        plusCat=sueldo*0.20
    return plusCat
def main():
    s=int(input("Ingrese el sueldo Base: "))
    h=str(input("Tiene hijos (s/n)?: "))
    c=int(input("Ingrese categoría (1 - 9): "))
    total= int(s) + int(bono(s)) + int(plus(s,h,c))
    print("El sueldo total será de: {}".format(total))

main()
"""
"""
#Ej. 10: Según las normas de tránsito, un vehículo no puede superar la velocidad máxima ni
#circular a menos que la velocidad mínima ( que es la mitad de la velocidad máxima ). Por
#una cuestión de errores de medición ( tanto en el automóvil como en los dispositivos de
#control ) hay un 15% de tolerancia. Sin embargo, se permite que los vehículos en
#emergencia ( ambulancias, patrulleros, etc. ) superen la velocidad máxima ( no así,
#circular a menos que la velocidad mínima ).
#Hacer un programa que solicite al usuario el ingreso de la velocidad a la que circula un
#vehículo, la velocidad máxima permitida, y si se trata o no de un vehículo de emergencia
#( contestando con “S” o “N” en mayúscula o minúscula ). Luego de invocar a la función
#multa , imprimir en pantalla el mensaje que la retorna función el cual indicará si recibe o
#no multa.
#Función multa : Recibe tres parámetro (velocidad del vehículo, velocidad máxima
#permitida, y un booleano que indica si el vehículo es o no de emergencia). Luego la
#función retornará un mensaje de acuerdo al siguiente criterio:
#● Si la velocidad del vehículo está entre la máxima y la mínima (ambas inclusive), el
#mensaje deberá ser : “No recibe multa” .
#● Si la velocidad está dentro de la tolerancia máxima (superando la máxima hasta
#el 15%, ( por ejemplo, para máxima de 60 km/h la tolerancia llega hasta 69 km/h );
#el mensaje deberá ser : “Advertencia” .
#Aclaración : No se aplica si es un vehículo en emergencia que, en cuyo caso el
#mensaje deberá se r: “No recibe multa” ..
#● Si la velocidad del vehículo está dentro de la tolerancia mínima ( hasta 15% por
#debajo de la velocidad mínima ), el mensaje deberá se r: “Advertencia” .
#Aclaración : Este caso es independiente del tipo de vehículo.
#● Si la velocidad del vehículo supera la velocidad máxima y el límite de tolerancia,
#el mensaje deberá se r: “Recibe multa por exceso de velocidad” .
#Aclaración : No se aplica si es un vehículo en emergencia qué, en cuyo caso el
#mensaje deberá se r: “No recibe multa” .
#● Si la velocidad del vehículo no exceda la tolerancia de velocidad mínima, el
#mensaje deberá se r: “Recibe multa por entorpecer el tránsito” .
#Aclaración : Este caso es independiente del tipo de vehículo.
def multa(vV,vM,vE):
    if ((vM/2) <= vV) and (vV <= vM):
        result="No recibe multa"
    elif ((vM<vV) and (vV<vM*1.15) and (vE=="n")):
        result="Advertencia"
    elif ((vM/2)*1.15)<=vV and (vV<=(vM/2)):
        result="Advertencia"
    elif (vM*1.15)<vV and not (vE=="s"):
        result="Recibe multa por exceso de velocidad"
    elif ((vM/2)*1.15)<vV and not (vE=="n"):
        result="No recibe multa"
    elif (vM/2)>vV:
        result="Recibe multa por entorpecer el tránsito"
    return result
def main():
    vV=int(input("Velocidad del vehículo: "))
    vM=int(input("Velocidad máxima: "))
    vE=str(input("Emergencia (s/n): "))
    print(multa(vV,vM,vE))
main()
 """
#Ej. 11: Una empresa se dedica a vender cañerías de gas y dispone únicamente de dos
#longitudes de caños que pueden empalmarse en línea recta pero no pueden cortarse.
#Las longitudes disponibles son 1 metro y 5 metros.
#Desarrollar un programa que solicite el ingreso por teclado de la cantidad disponible de
#caños de 1 metro, la cantidad disponible de caños de 5 metros y la longitud total de
#tendido ( entero positivo expresado en metros ). El programa debe informar por pantalla si
#es posible cubrir exactamente la necesidad ( sin pasarse ) y sugerir una posible
#combinación de caños para alcanzar el total. Para determinar el mensaje, desde el
#programa principal se deberá invocar a la función mensaje .
#Función mensaje : Recibe como parámetros los datos ingresados en el programa
#principal, y verifica dicho parámetros. Luego retorna un mensaje donde indicará si es
#posible o no cubrir el tendido. Y para el caso de ser posible agrega al mensaje
#sugerencias con la combinación posible de caños.


hacer despues






