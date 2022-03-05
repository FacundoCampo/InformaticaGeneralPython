"""
def esPrimo(n):
    primo=""
    i=2
    while i>0:
        for num in range(1,n+1):
            if n%num==0:
                n=int(n/num)
                i-=1
    if n==1:
        primo=True
    else:
        primo=False
    return primo
def main():
    print(esPrimo(7))
main()
"""
"""
def espalindromo(texto):
    palindromo=True
    for i in range(len(texto)):
        if (texto[-i-1]!=texto[i]):
            palindromo=False
    return palindromo
def main():
    print(espalindromo("rayar"))
main()
"""
"""
xs=['Hola','Mundo',]
xs="Hola"
xs="Mundo"
xs[0]='x'
print(xs)
"""
"""
def comparar(a,b,c):
    if((a and (b or c)) != ((a and b)or(a and c))):
        return True
    else:
        return False
def main():
    print(comparar("a","b","c"))
main()
"""
"""
def f2(x):
    x=x+10
    return x
def f1():
    x=10
    print(str(f2(x))+"-",end="")
x=5
f1()
print ("{0:d}".format(f2(x)))
"""
"""
xn=[1,2,3,4]
n=1234
print((2 in xn) and (2 in n))
"""

def liquidar():
    archVentas=open("ventasTarjetas.txt","r")
    lstVentas=[]
    for linea in archVentas.readlines():
        lstVentas.append(linea[:-1].split(","))
    archVentas.close
    archVendedores=open("vendedores.txt","r")
    lstVendedores=[]
    for linea in archVendedores.readlines():
        lstVendedores.append(linea[:-1].split(","))
    archVendedores.close
    archLiquidacion=open("liquidacionComisiones.txt","w")
    cuenta=0
    lstAgregar=[]
    for i in range(len(lstVendedores)):
        for j in range(len(lstVentas)):
            if lstVendedores[i][0]==lstVentas[j][0]:
                cuenta+=int(lstVentas[j][2])
        if ((cuenta*100)/(int(lstVendedores[i][2])))<80:
            lstAgregar.append(lstVendedores[i][0])
            lstAgregar.append(str(float(lstVendedores[i][3])*0))
        elif ((cuenta*100)/(int(lstVendedores[i][2])))>80 and ((cuenta*100)/(int(lstVendedores[i][2])))<100:
            lstAgregar.append(lstVendedores[i][0])
            lstAgregar.append(str(float(lstVendedores[i][3])*0.03))
        elif ((cuenta*100)/(int(lstVendedores[i][2])))>100:
            lstAgregar.append(lstVendedores[i][0])
            lstAgregar.append(str(float(lstVendedores[i][3])*0.1))
        archLiquidacion.write(",".join(lstAgregar)+"\n")
        cuenta=0
        lstAgregar=[]
    archLiquidacion.close
liquidar()

"""
def topcinco():
    archVentas=open("ventasTarjetas.txt","r")
    lstVentas=[]
    for linea in archVentas.readlines():
        lstVentas.append(linea[:-1].split(","))
    archVentas.close
    archVendedores=open("vendedores.txt","r")
    lstVendedores=[]
    for linea in archVendedores.readlines():
        lstVendedores.append(linea[:-1].split(","))
    archVendedores.close
    archLiquidacion=open("liquidacionComisiones.txt","r")
    lstLiquidacion=[]
    for linea in archLiquidacion.readlines():
        lstLiquidacion.append(linea[:-1].split(","))
    archLiquidacion.close
    cuenta=0
    maxi=int()
    while cuenta<5:
        for i in range(len(lstLiquidacion)-1):
            if float(lstLiquidacion[i][1])>maxi:
                maxi=float(lstLiquidacion[i][1])
                i2=i
        for j in range(len(lstVendedores)):
            if lstLiquidacion[i2][0]==lstVendedores[j][0]:
                nombre=lstVendedores[j][1]
        print("{}, {}, {}\n".format(lstLiquidacion[i2][0],nombre,lstLiquidacion[i2][1]))
        lstLiquidacion.remove(lstLiquidacion[i2])
        cuenta+=1
        maxi=int()
topcinco()
"""