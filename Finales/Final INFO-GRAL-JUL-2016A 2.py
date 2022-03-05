"""def liquidar():
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
    lst_id_vendedores=[]
    for i in range(len(lstVendedores)):
        if not lstVendedores[i][0] in lst_id_vendedores:
            lst_id_vendedores.append(lstVendedores[i][0])
    archLC=open("LiquidacionComisiones 2.txt","w")
    cant_tarj=0
    for i in range(len(lst_id_vendedores)):
        for z in range(len(lstVentas)):
            if lst_id_vendedores[i]==lstVentas[z][0]:
                cant_tarj+=int(lstVentas[z][2])
        lstAgregar=[]
        for x in range(len(lstVendedores)):
            if lstVendedores[x][0]==lst_id_vendedores[i]:
                mierda=int(lstVendedores[x][2])
                prom=cant_tarj*100/float(lstVendedores[x][2])
                if prom<80:
                    comisiones=0
                    lstAgregar.append(str(lstVendedores[x][0]))
                    lstAgregar.append(str(comisiones))
                elif prom>80 and prom<100:
                    comisiones=float(lstVendedores[x][3])*0.03
                    lstAgregar.append(str(lstVendedores[x][0]))
                    lstAgregar.append(str(comisiones))
                elif prom>100:
                    comisiones=float(lstVendedores[x][3])*0.1
                    lstAgregar.append(str(lstVendedores[x][0]))
                    lstAgregar.append(str(comisiones))
        archLC.write(",".join(lstAgregar)+"\n")
        lstAgregar=[]
        cant_tarj=0
    archLC.close
liquidar()"""
"""
def espalindromo(texto):
    palindromo=True
    for i in range(len(texto)):
        if (texto[-(i+1)]!=texto[i]):
            palindromo=False
    print(palindromo)
espalindromo("ananaa")
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
print(comparar(2,2,2))"""
"""
def f2(x):
    x=x+10
    return x
def f1():
    x=10
    print(str(f2(x))+"-",end="")
x=5
f1()
print ("{0:d}".format(f2(x)))"""
xn=[1,2,3,4]
n=1234
print((2 in xn) and (2 in n))