"""
#Ej. 1: Desarrollar un programa en el que se ingrese por teclado números enteros hasta que
#se hayan ingresado 5 números pares e informar por pantalla si alguno de ellos es
#también múltiplo de cuatro

def main():
    totNP=0
    while totNP<5:
        num=int(input("Ingrese numero entero: "))
        if ((num%2)==0) and not ((num%4)==0):
            totNP+=1
            print("Numero Par. Total de numeros pares ingresados: {}".format(totNP))
        if ((num%2)==0) and ((num%4)==0):
            totNP+=1
            print("Numero Par. Numero multiplo de 4. Total de numeros pares ingresados: {}".format(totNP))
    
    if totNP==5:
        print("FIN")
main()
"""
"""
#Ej. 2: Desarrollar un programa en el que se ingresen por teclado una cantidad indefinida de
#números enteros positivos hasta que se ingrese 0. A continuación el programa debe
#indicar por pantalla cuál fue el mayor y cuál el menor.
def main():
    n=int(input("Ingrese numeros enteros positivos (finalice con 0): "))
    numMax=n
    numMin=n
    while n!=0:
        if numMin>=n:
            numMin=n
        if numMax<=n:
            numMax=n
        n=int(input("Ingrese numeros enteros positivos (finalice con 0): "))
    if n==0:
        print("el numero maximo es {} y el numero minimo es {}".format(numMax,numMin))
main()
"""
"""
#Ej. 3: Desarrollar una función que reciba como parámetro un valor numérico y determine si
#dicho número es primo o no, retornando verdadero (True) o falso (False)
#respectivamente. Luego utilizar la función en un programa que solicite al usuario el
#ingreso de una cantidad cant (número natural) y que muestre por pantalla dos listados:
#primero un listado de los números primos comprendidos entre 1 y cant y luego otro
#listado con los primeros cant números primos. Ambos listados se deben imprimir por
#pantalla a 10 columnas, alineando como se muestra en el ejemplo

def primo(num):
    primo=True
    for i in range (2,num):
        if num%i==0:
            primo=False
    return primo
def main():
    cant=int(input("ingreso de una cantidad cant (número natural): "))
    print("\nPrimos entre 1 y {}: ".format(cant))
    for t in range(1,cant):
        if primo(t)==True:
            print(t,end=" ")
    print("\nPrimeros {} primos: ".format(cant))
    control=0
    n=2
    while control<=cant:
        if primo(n)==True:
            print(n,end=" ")
            control+=1
        n+=1
main()
 """
"""
# Ej. 4: Desarrollar una función booleana que reciba como parámetro un número entero positivo
# y retorne verdadero ( True ) o falso ( False ) según sea el número perfecto o no. Luego
# utilizarla en un programa que encuentre y muestre por pantalla los primeros cuatro
# números perfectos.
# Definición : Un número perfecto es un entero positivo, que es igual a la suma de todos
# los enteros positivos (excluido él mismo) que son divisores del número. Por ejemplo, el
# primer número perfecto es 6, ya que los divisores de 6 son 1, 2, 3 y 1 + 2 + 3 = 6.

def perfecto(num):
    bandera=False
    divisores=0
    for i in range(1,num):
        if num%i==0:
            divisores+=i
        i+=1
    if divisores==num:
        bandera=True

    return bandera
        
def main():
    cont=0
    a=10000000000
    while cont<4:
        for i in range(1,a):
            if perfecto(i)==True:
                print(i)
        cont+=1
main()
"""
"""
#Ej. 5: Desarrollar una función booleana que reciba como parámetro un número entero de
#cuatro cifras y determine si el número cumple la condición de que la suma de las
#unidades y las centenas es igual a la suma de las decenas y las unidades de mil. Luego
#realizar un programa que encuentre e imprima un listado con todos los números de 4
#cifras que cumplan la condición anteriormente citada. Por ejemplo, el número 7821
#cumple esta condición ya que 1 + 8 = 2 + 7.

def cifras(num):
    num_nuevo=num
    uni=num%10
    dec=num//10%10
    cent=num//100%10
    mil=num//1000%10
    bandera=False
    if uni+cent == dec+mil:
        bandera=True
    return bandera
def main():
    for i in range(1000,10000):
        if cifras(i)==True:
            print(i,end=" ")
        i+=1
main()
"""
"""
#Ej. 7: Desarrollar un programa que permita ingresar las notas de una cantidad indefinida de
#alumnos. Considerar notas enteras en el rango de 1 a 10 e ignorar las notas no válidas
#(fuera el rango) ingresadas. La carga finaliza cuando la nota ingresada es 0. A
#continuación el programa deberá mostrar la cantidad de alumnos aplazados (nota menor
#a 4), la cantidad de alumnos aprobados (nota entre 4 y 7 inclusive) y la cantidad de
#alumnos que promocionan la materia (nota superior a 7). En cada caso, se mostrará el
#porcentaje del total de notas válidas cargadas que cada caso representa y el promedio
#general de todas las notas. Ejemplo:
#Ingrese nota: 5
#Ingrese nota: 4
#Ingrese nota: 4
#Ingrese nota: 11
#Ingrese nota: 2
#Ingrese nota: 8
#Ingrese nota: 8
#Ingrese nota: 2
#Ingrese nota: 7
#Ingrese nota: 9
#Ingrese nota: 0
#Cantidad de aplazos: 2 (22.22%)
#Cantidad de aprobados: 4 (44.44%)
#Cantidad de promocionados: 3 (33.33%)
#Promedio general: 5.44

def main():
    aplazos=0
    aprobados=0
    promociones=0
    cont_notas=0
    total=0
    nota=int(input("Ingrese nota: "))
    while nota!=0:
        while nota>0 and nota<=10:
            if nota<4:
                aplazos+=1
            if nota>=4 and nota<=7:
                aprobados+=1
            if nota>7:
                promociones+=1
            total+=nota
            cont_notas+=1
            nota=int(input("Ingrese nota: "))
        while nota<0 or nota>10:
            nota=int(input("Ingrese nota: "))
    print("Cantidad de aplazos: {} ({} %) ".format(aplazos,(aplazos/cont_notas)))
    print("Cantidad de aprobados: {} ({} %) ".format(aprobados,aprobados/cont_notas))
    print("Cantidad de promocionados: {} ({} %) ".format(promociones,promociones/cont_notas))
    print("Promedio general: {}".format(total/cont_notas))
main()            
"""
"""
#Ej. 6: Desarrollar la función aBinario que recibe como parámetro un número decimal (base
#10, no mayor a 1000) y retorna el número expresado en binario (base 2). Desarrollar un
#programa que ingrese por teclado un entero en base 10, invoque a la función aBinario
#y muestre por pantalla el resultado retornado por la función. 
def aBinario(n):
    numNuevo=n
    numBin=0
    exp=0
    while numNuevo>0:
        numBin+=(numNuevo%2)*10**exp
        numNuevo=numNuevo//2
        exp+=1
    return numBin
def main():
    a=234
    print(aBinario(a))
main()
"""
"""
#Ej. 8: La operación factorial de un número entero no negativo n (expresado como n!) es el
#producto que resulta de multiplicar n por todos los enteros inferiores a él hasta el uno (0!
#= 1 por definición). Ejemplo:
#5! = 5 * 4 * 3 * 2 * 1 = 120
#10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800
#n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1 = ………….
#Desarrollar un programa que solicite el ingreso de un número entero, verifique si se trata
#de un número mayor o igual a 0 y calcule su factorial. Para el cálculo del factorial se
#debe desarrollar una función que reciba como parámetro el número, realice la operatoria
#y retorne el resultado. En caso de que el usuario ingrese un número negativo, imprimir
#una advertencia

def factorial(num):
    result=1
    for i in range (1,num+1):
        result*=i
        i+=1
    return result
def main():
    n=int(input("Ingrese un numero entero positivo: "))
    while n<0:
        n=int(input("ADV, Ingrese un numero entero positivo: "))
    print(factorial(n))
main()
"""
"""
#Ej. 9: Desarrollar una función booleana que reciba como parámetro un número entero positivo
#(de hasta nueve cifras) y retorne verdadero (True) si es capicúa o falso (False) en caso
#contrario. Un número capicúa es aquel que leído de izquierda a derecha es igual que
#leído de derecha a izquierda. Por ejemplo 82428 es capicúa.
#Desarrollar un programa que solicite un número por teclado e informe si éste es capicúa
#o no según el resultado retornado por la función.
#Ayuda: Para programar la función considere invertir el número y luego compararlo con el
#número original, si resultan iguales, entonces es capicúa
def capicua(n):
    numerocont=n
    numero=n
    nCapicua=0
    cont=0
    while numerocont>0:
        numerocont=numerocont//10
        cont+=1
    cont=cont-1
    while numero>0:
        nCa=numero%10
        numero=numero//10
        nCapicua+=nCa*10**cont
        cont-=1
    if n==nCapicua:
        result=True
    else:
        result=False
    return result
def main():
    num=65
    print(capicua(num))
main()
"""            
#FIGURAS
"""
*******
*******
*******
def figura(b,h):
    for col in range(0,h):
        for fila in range(0,b):
            if fila>=0:
                print("*",end="")
            print("",end="")
        print("")
def main():
    b=int(input("Ingrese base: "))
    h=int(input("Ingrese altura: "))
    while b<2 or h<2:
        if b<2:
            b=int(input("ERROR, Ingrese base: "))
        if h<2:
            h=int(input("ERROR, Ingrese altura: "))
    figura(b,h)
main()
"""
"""
* * * * * * * 
*           * 
*           * 
* * * * * * * 
def figura(b,h):
    for fila in range(0,h):
        for col in range(0,b):
            if fila==0 or fila==h-1 or col==0 or col==b-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("")
def main():
    base=int(input("Ingrese base 3>=b: "))
    altura=int(input("Ingrese altura 3>=h: "))
    while base<3 or altura<3:
        if base<3:
            base=int(input("Ingrese base 3>=b: "))
        if altura<3:
            altura=int(input("Ingrese altura 3>=b: "))
    figura(base,altura)
main()
"""
"""
*         
* *       
* * *     
* * * *   
* * * * * 
#Ej. 12: Desarrollar un programa que solicite al usuario que ingrese la base de un triángulo
#rectángulo de catetos iguales (número natural mayor o igual a tres, debe validarse).
#Luego desde el programa principal invocar a una función que dibuje en la pantalla
#usando asteriscos dicho triángulo usando el valor de la base pasada como parámetro.

def figura(b):
    for fila in range(0,b):
        for col in range(0,b):
            if col-fila<=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("")
def main():
    b=int(input("Ingrese la base del triangulo rectangulo de catetos iguales >=3: "))
    while b<3:
        b=int(input("ERROR, Ingrese la base del triangulo rectangulo de catetos iguales >=3: "))
    figura(b)
main()
"""
"""
          *           
        * * *         
      * * * * *       
    * * * * * * *     
  * * * * * * * * *   
* * * * * * * * * * * 
#Ej. 13: Desarrollar un programa que solicite al usuario que ingrese una base (número entero
#impar mayor o igual a tres, validar el valor ingresado). El programa invocará a una
#función que reciba como parámetro la base ingresada y que dibuje en pantalla un
#triángulo isósceles de asteriscos.
def figura(b,h):
    for fila in range(0,h):
        for col in range(0,b):
            if fila+col>=b//2 and fila>=col-b//2:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print("")


def main():
    base=int(input("Ingrese una base (numero entero, impar, mayor o igual a 3): "))
    while (base!=int(base)) or (base%2==0) or (base<3):
        base=int(input("ERROR,Ingrese una base (numero entero, impar, mayor o igual a 3): "))
    figura(base,(base//2)+1)
main()
"""
"""
*             
* *           
* * *         
* * * *       
* * *         
* *           
*  
#Ej. 14: Desarrollar un programa que solicite al usuario que ingrese la altura de un triángulo
#(número entero impar mayor o igual a cinco, validar el valor ingresado). Luego deberá
#invocar a una función que reciba como parámetro la altura ingresada y que dibuje en
#pantalla el triángulo de asteriscos como se puede ver en el ejemplo:

def figura(b,h):
    for fila in range(0,h):
        for col in range (0,b):
            if (col<=b//2) and (((fila<=h//2 and fila>=0) and ((fila-col)<=h//2 and (fila-col)>=0)) or ((fila>=h//2 and fila<=b-1) and ((fila+col)>=h//2 and (fila+col)<=b-1))):
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print("")
def main():
    b=7
    figura(b,b)
main()
"""
"""
#Ej. 15: Desarrollar un programa que solicite al usuario que ingrese la diagonal de un rombo
#(validar que el valor ingresado sea impar y mayor o igual a cinco). Luego deberá invocar
#a una función que reciba como parámetro la diagonal ingresada y que dibuje en pantalla
#el rombo de asteriscos como se puede ver en el ejemplo:
      *       
    * * *     
  * * * * *   
* * * * * * * 
  * * * * *   
    * * *     
      * 
def figura(d):
    for fila in range (0,d):
        for col in range(0,d):
            if (((col<=d//2) and (fila<=d//2)) and (((fila+col)>=d//2) and ((fila+col)<=d))) or (((col<=d//2) and (fila>=d//2)) and (((fila-col)<=d//2) and ((fila-col)>=0))) or (((col>=d//2) and (fila<=d//2)) and (((col-fila)<=d//2) and ((col-fila)>=0))) or (((col>=d//2) and (fila>=d//2)) and (((fila+col)>=d-1) and ((col+fila)<=(d-1+d//2)))):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("")
def main():
    num=7
    figura(num)
main()
"""
#Ej. 16: Realizar un programa que solicite al usuario que ingrese el ancho de la figura (número
#entero impar mayor o igual a siete, validar el valor ingresado). Luego deberá invocar a
#una función que reciba como parámetro el ancho ingresado y que dibuje en pantalla la
#figura de asteriscos como se puede ver en el ejemplo:

def figura(l):
    for fila in range(0,(l//2)+1):
        for col in range(0,l):
            if ((col<=l//2) and ((((col-fila)<=l//2) and ((col-fila)>0)) or (col==0) or (fila==l//2))) or ((col>=l//2) and ((((fila+col)>=l//2) and ((fila+col)<l-1)) or (col==l-1) or (fila==l//2))):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print(" ")
def main():
    l=13
    figura(l)
main()













            
            