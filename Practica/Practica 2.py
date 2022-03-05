"""
#Ej. 1: Programar una función que reciba como parámetros la longitud de los lados de un
#triángulo y que retorne el área del mismo. Utilizarla en un programa que solicite al
#usuario los datos, invoque a la función e informe el área calculada. Todos los datos y
#textos que se muestren por pantalla en este y en todos los ejercicios de la presente guía
#deben respetar estrictamente el formato de los ejemplos dados.
def areaTri(l1,l2,l3):
    p=(l1 + l2 + l3)/2
    area=(p*(p-l1)*(p-l2)*(p-l3))**(0.5)
    return area
def main():
    lado1=int(input("Ingrese lado 1: "))
    lado2=int(input("Ingrese lado 2: "))
    lado3=int(input("Ingrese lado 3: "))
    print("El area del triangulo es = {:.2f} ".format(areaTri(lado1,lado2,lado3)))
main()
"""
"""
#Ej. 2: Programar la función raiz que recibe como parámetros un radicando x ( número real ) y
#un índice n ( número natural ). La función deberá retornar la raíz n (enésima) de x .
#Utilizarla en un programa que solicite al usuario el radicando real y el índice natural.
#Luego invocar a la función raiz e informar la raíz calculada.
import math
def raiz(rad,ind):
    rais= math.pow(rad,1/ind)
    return rais
def main():
    radicando=int(input("Ingrese el radicando (numero real): "))
    indice=int(input("Ingrese el índice (numero natural): "))
    print("La raiz {} de {} es = {:.6f}".format(radicando,indice,raiz(radicando,indice)))
main()
"""
"""
#Ej. 3: El concepto de paridad es de fundamental importancia para la detección y corrección de
#errores en el almacenamiento y transmisión de datos en los sistemas informáticos. Para
#cada dato en binario se genera un bit adicional (bit de paridad) de manera tal que este
#será 1 ( uno ) si la suma de la cantidad de 1 ( unos ) presentes en el dato es impar y 0
#( cero ) si esta suma es par.
#Programar la función booleana paridad que recibe como parámetro un número binario
#de hasta 8 bits y genera y retorna el bit de paridad correspondiente. Utilizarla en un
#programa que solicite al usuario el ingreso del número binario, invoque a la función e
#informe la paridad generada.
def paridad(nBool):
    b0=nBool%10
    b1=nBool%100//10
    b2=nBool%1000//100
    b3=nBool%10000//1000
    b4=nBool%100000//10000
    b5=nBool%1000000//100000
    b6=nBool%10000000//1000000
    b7=nBool%100000000//10000000
    return (b0+b1+b2+b3+b4+b5+b6+b7)%2
def main():
    nB=int(input("Ingrese un numero de binario de hasta 8 bits: "))
    print("Bit de paridad generado: {}".format(paridad(nB)))
main()
"""
"""
#Ej. 4: Programar las funciones areaCirc , areaCuad y areaNegr a.
#areaCirc recibe como parámetro el diámetro de un círculo y calcula y retorna el área
#del mismo.
#areaCuad recibe como parámetro el lado de un cuadrado y calcula y retorna el área del
#mismo.
#areaNegra recibe como parámetro el lado de un cuadrado de una figura (como la dada
#a continuación) y calcula y retorna el área negra resultante.
#Luego utilizar las funciones en un programa que solicitará al usuario el lado del cuadrado
#y mostrará por pantalla el valor correspondiente para el área de color negra y además
#indicará el porcentaje que éste área representa con respecto al área total del cuadrado.
import math
def areaCirc(diam):
    areaCi=((diam/2)**2)*(math.pi)
    return areaCi
def areaCuad(lado):
    areaCu=(lado*lado)
    return areaCu
def areaNegra(l1):
    areaNe=(areaCuad(l1)-areaCirc((2/3)*l1)-2*areaCirc((1/3)*l1))
    return areaNe
def main():
    a=int(input("Ingrese el lado: "))
    b=((areaNegra(a)*100)/areaCuad(a))
    print("El area negra es {:.2f} y es un {:.2f} % del area total del cuadrado.".format(areaNegra(a),b))
main()
"""
"""
#Ej. 5: Programar una función que reciba como parámetros 2 números naturales y retorne un
#número natural al azar comprendido entre estos 2 números (inclusive). Debe asumirse
#que esta función será invocada de manera que el primer parámetro representa el límite
#inferior del intervalo y el segundo el límite superior.
#Utilizarla en un programa que solicite al usuario los límites del intervalo e invoque a la
#función tres veces de la siguiente manera:
#5.1. Invocarla con los extremos del intervalo ingresados por teclado y mostrar en
#pantalla el valor generado.
#5.2. Invocarla como en el punto 5.1, pero usando como extremo inferior el valor
#generado en 5.1.
#5.3. Invocarla como en el punto 5.2, pero usando como extremo superior el valor
#generado en 5.2.
import random
def azar(nMin,nMax):
    nAzar= random.randint(nMin,nMax)
    return nAzar
def main():
    nMi=int(input("Ingrese el limite inferior (numero natural): "))
    nMa=int(input("Ingrese el limite superior (numero natural): "))
    nAz= azar(nMi,nMa)
    nAz2=azar(nAz,nMa)
    print("1-Limite inferior {}, limite superior {}. Numero generado: {}".format(nMi,nMa,nAz))
    print("2-Limite inferior {}, limite superior {}. Numero generado: {}".format(nAz,nMa,nAz2))
    print("3-Limite inferior {}, limite superior {}. Numero generado: {}".format(nAz,nAz2,azar(nAz,nAz2)))
main()
"""
"""
#Ej. 6: Programar una función booleana que retorne 0 o 1 al azar.
#Utilizarla en un programa en que se solicite al usuario dos alternativas para cada uno de
#los ítems de una cena: vestimenta, plato y bebida. Luego el programa muestra por
#pantalla la cena que resulta de elegir cada ítem al azar.
import random
def azar():
    az=random.randint(0,1)
    return az
def main():
    v1=str(input("Ingrese alternativa 1 para vestimenta: "))
    v2=str(input("Ingrese alternativa 2 para vestimenta: "))
    p1=str(input("Ingrese alternativa 1 para plato: "))
    p2=str(input("Ingrese alternativa 2 para plato: "))
    b1=str(input("Ingrese alternativa 1 para bebida: "))
    b2=str(input("Ingrese alternativa 2 para bebida: "))
    func1= azar()
    func2= azar()
    func3= azar()
    vestimenta= (v1*func1)+(v2*(1-func1))
    plato=(p1*func2)+(p2*(1-func2))
    bebida=(b1*func3)+(b2*(1-func3))
    print("Cena al azar: {}, {} y {}".format(vestimenta,plato,bebida))
main()
"""
"""
#Ej. 7: Programar la función justificado que reciba una frase fra y un valor natural ancho
#como parámetros. La función debe retornar un string de un tamaño total ancho , que
#comienza y termina con comillas simples y que contiene a la frase fra , justificada a la
#derecha y rellena con espacios a la izquierda.
#Utilizarla en un programa en que se solicite al usuario la frase y el ancho deseado, se
#invoque a la función y se imprima por pantalla el valor retornado.
def justificado(fra,ancho):
    return ("'" + " "*ancho + fra + "'")
def main():
    f= str(input("Ingrese la frase: "))
    a= int(input("Ingrese un numero: "))
    print(justificado(f,a))
main()
"""
"""
#Ej. 8: Dado la función main() , completar el programa programando las funciones crearFila
#y crearRectangulo de modo que al ejecutar el programa dibuje un rectangulo de
#asteriscos. La función main() no debe ser modificado:
#crearFila recibe como parámetro un número natural ancho y retorna un string
#conformado por una cantidad ancho de asteriscos.
#crearRectangulo recibe como parámetros dos números naturales ancho y alto , y
#retorna un string que al ser mostrado por pantalla dibuja un rectángulo de ancho por
#alto asteriscos. Esta función invoca a crearFila para crear el string de cada fila.
def crearFila(anc):
    return ("*"*anc)
def crearRectangulo(anc,alt):
    return ("{}\n".format(crearFila(anc))*alt)
def main():
    ancho = int(input('Ingrese ancho: ' ))
    alto = int(input('Ingrese alto: '))
    print(crearRectangulo (ancho, alto))
main()
"""