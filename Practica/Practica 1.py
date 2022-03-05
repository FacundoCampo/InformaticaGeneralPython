"""
#Ej. 2: Desarrollar un programa que solicite al usuario el ingreso de su nombre y luego de su
#apellido. Luego el programa deberá mostrar un saludo al usuario con su apellido y su
#nombre (en ese orden) separados por un espacio y como se muestra a continuación:
n= input("Ingrese su nombre: ")
a= input("Ingrese su apellido: ")
print("Hola",n,a,"!")
"""
"""
#Ej. 3: Desarrollar un programa que solicite los dos lados de un rectángulo. Luego el programa
#debe calcular y mostrar por pantalla el perímetro y área del mismo.
la= int(input("Ingrese lado 1: "))
lb= int(input("Ingrese lado 2: "))
print("Perimetro", (la*2)+(lb*2))
print("Area", la*lb)
"""
"""
#Ej. 4: Desarrollar un programa que solicite al usuario el ingreso de un número real y luego el
#programa muestra por pantalla la parte entera y la parte fraccionaria de dicho número
#por separado.
ni=float(input("Ingresenumero real: "))
n2=int(ni)
n3= (ni-n2)
print("Parte entera: ", n2)
print("parte fraccionaria: ", n3)
"""
"""
#Ej. 5: Desarrollar un programa que solicite al usuario el ingreso de un número natural de 5
#dígitos y que luego muestre por pantalla a cada dígito elevado al cuadrado separado por
#un guión.
ni=int(input("ingrese numero natural de 5 digitos: "))
a1=ni%10
a2=ni%100//10
a3=ni%1000//100
a4=ni%10000//1000
a5=ni%100000//10000
print("Separación en dígitos: "a5**2,"-",a4**2,"-",a3**2,"-",a2**2,"-",a1**2)
"""
"""
#Ej. 6: Realizar un programa en el que se ingrese la base y la altura de un triángulo rectángulo
#e informe el área y el perímetro del mismo. El programa debe mostrar el resultado con
#una precisión de 2 dígitos decimales y de la siguiente forma:
b=int(input("Ingrese base del triangulo: "))
h=int(input("Ingrese altura del tranulo: "))
perimetro= ((((b**2)+(h**2))**(1/2))+b+h)
area=(b*h)/2
print("Calculos para un triangulo de base",b," y altura",h)
print("<<<Area={:.2f}>>> <<<Perimetro={:.2f}>>>".format(area, perimetro))
"""
"""
#Ej. 7: Desarrollar un programa en el que se ingresen dos números enteros positivos y que
#genere y muestre un tercer número que esté compuesto por las unidades del primer
#número y por las decenas del segundo.
n1=int(input("ingrese un primer numero: "))
n2=int(input("Ingrese un segundo numero: "))
a2=n2%100//10
a1=n1%10
print(a2*10+a1)
"""
"""
#Ej. 8: Desarrollar un programa en el que se ingrese un valor numérico entero, el cual
#representa una cantidad expresada en segundos, y luego lo exprese en días, horas,
#minutos y segundos.
s=int(input("Ingrese unnumero en segundos: "))
d=s//86400
h=(s-86400)//3600
m=(s-86400-2*3600)//60
s=(s-86400-2*3600-60)
print("{} dia(s), {} hora(s), {} minuto(s), {} segundo(s)." .format(d, h, m, s))
"""
"""
#Ej. 9: Desarrollar un programa que solicite al usuario el ingreso de un número natural de una
#cantidad impar de cifras (al menos 3 cifras). Luego el programa deberá informar la
#cantidad de cifras del número ingresado, la primera y la última cifra del número
#ingresado, como así también su cifra central como se muestra a continuación:

n=int(input("Ingresar un numero natural impar min 3 cifras: "))
cantCif= len(str(n))
ultCif= n%10
medCif= n%10**(cantCif//2+1)//10**(cantCif//2)
priCif= n//10**(cantCif-1)
print("El numero ingresado tiene {} cifras".format(cantCif))
print("La primera cifra es {}, la ultima es {} y la central es {}.".format(priCif, ultCif, medCif))
"""
"""
#Ej. 10: Desarrollar un programa que solicite un número binario natural (base 2) con un máximo
#de 5 bits y lo convierta a un número decimal (en base 10).
def main():
    nB=int(input("Ingrese un numero binario: "))
    b0=nB%10
    b1=nB%100//10
    b2=nB%1000//100
    b3=nB%10000//1000
    b4=nB%100000//10000
    nd=(b4*2**4+b3*2**3+b2*2**2+b1*2**1+b0*2**0)
    print("Número en decimal: {}".format(nd))
main()
"""
"""
#Ej. 11: Desarrollar un programa que solicite al usuario el ingreso de un número natural en base
#10 (de no más de 5 cifras) y lo convierta a un número octal (en base 8).
def main():
    nD=int(input("Ingrese un numero decimal (maximo 5 cifras): "))
    nD0=nD%8
    nD1=(nD//8)%8
    nD2=((nD//8)//8)%8
    nD3=(((nD//8)//8)//8)%8
    nD4=((((nD//8)//8)//8)//8)%8
    nO=(nD0*10**0 + nD1*10**1 + nD2*10**2 + nD3*10**3 + nD4*10**4)
    print("Numero en octal: {}".format(nO))
main()
"""
"""
#Ej. 12: Desarrollar un programa que solicite al usuario 3 números enteros y muestre la suma de
#dichos números por pantalla. Se deben mostrar los números alineados como en el
#ejemplo dado a continuación. Para el caso de números negativos el signo debe quedar a
#plena izquierda.
    
def main():
    ne1=int(input("Ingrese el primer numero entero: "))
    ne2=int(input("Ingrese el segundo numero entero: "))
    ne3=int(input("Ingrese el tercer numero entero: "))
    suma= ne1+ne2+ne3
    print("{:=10d}\n".format(ne1))
    print("{:=10d}\n".format(ne2))
    print("{:=10d}\n".format(ne3))
    print("----------")
    print("{:=10d}".format(suma))
    
main()  
"""
"""
#Ej. 13: Desarrollar un programa que solicite al usuario el ingreso de un multiplicando natural de
#3 cifras y luego un multiplicador natural de 3 cifras. El programa será usado con fines
#didácticos a fin de enseñar el método para obtener el producto. Se pide que el programa
#muestre por pantalla los pasos y cálculos intermedios tal como se hacen sobre una hoja
#de papel, respetando exactamente las alineaciones y forma para la salida.
def main():
    m1= int(input("Ingrese el multiplicando: "))
    m2= int(input("Ingrese el multiplicador: "))
    part1=(m2%10)*m1
    part2=(m2%100//10)*m1
    part3=(m2%1000//100)*m1
    print("{:=10d}".format(m1))
    print("X {:=8d}".format(m2))
    print("----------")
    print("{:=10d}".format(part1))
    print("+ {:=7d}-".format(part2))
    print("{:=8d}--".format(part3))
    print("----------")
    print("{:=10d}".format(m1*m2))

main()
"""    
    