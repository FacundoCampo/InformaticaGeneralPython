"""def esPrimo(num):
    primo=False
    i=2
    while(i>0):
        for z in range (1,num):
            if num%z==0:
                i-=1
    if i==0:
        primo=True
    return primo
print(esPrimo(2))"""
"""def espalindromo (texto):
    palindromo=True
    for i in range(len(texto)):
        if(texto[-i-1]!=texto[i]):
            palindromo=False
    return palindromo
print(espalindromo("rayarar"))"""
"""xs=['Hola','Mundo',]
xs="Hola"
xs="Mundo"
xs[0]='x'
print(xs)"""
"""def comparar(a,b,c):
    if((a and (b or c)) != ((a and b)or(a and c))):
        return True
    else:
        return False
print(comparar(1,1,1))"""
"""def f2(x):
    x=x+10
    return x
def f1():
    x=10
    print(str(f2(x))+"-",end="")
x=5
f1()
print ("{0:d}".format(f2(x)))"""
"""
xn=[1,2,3,4]
n=1234
print((2 in xn) and (2 in n))
"""
"""
def liquidar():
    archVentas=open("ventasTarjetas.txt","r")
    lstVentas=[]
    for linea in archVentas.readlines():
        lstVentas.append(linea[:-1].split(","))
    archVentas.close
    
    archVendedores=open("Vendedores.txt","r")
    lstVendedores=[]
    for linea in archVendedores.readlines():
        lstVendedores.append(linea[:-1].split(","))
    archVendedores.close
    
    archLQ=open("liquidacionComiciones 3.txt","w")
    lst_id=[]
    for i in range(len(lstVendedores)):
        lst_id.append(lstVendedores[i][0])
    tarjetas=0
    for id in range(len(lst_id)):
        for i in range(len(lstVentas)):
            if lst_id[id]==lstVentas[i][0]:
                tarjetas+=int(lstVentas[i][2])
        for z in range(len(lstVendedores)):
            if lst_id[id]==lstVendedores[z][0]:
                objetivos= int(lstVendedores[z][2])
                lstAg=[]
                comision=(tarjetas*100)/objetivos
                if comision<80:
                    lstAg.append(str(lst_id[id]))
                    lstAg.append(str(float(lstVendedores[z][3])*0))
                elif comision<100 and comision>80:
                    lstAg.append(str(lst_id[id]))
                    lstAg.append(str(float(lstVendedores[z][3])*0.03))
                elif comision>100:
                    lstAg.append(str(lst_id[id]))
                    lstAg.append(str(float(lstVendedores[z][3])*0.1))
                archLQ.write(",".join(lstAg)+"\n")
                lstAg=[]
                tarjetas=0
    archLQ.close
liquidar()"""
def topcinco():
    archVentas=open("ventasTarjetas.txt","r")
    lstVentas=[]
    for linea in archVentas.readlines():
        lstVentas.append(linea[:-1].split(","))
    archVentas.close
    archVendedores=open("Vendedores.txt","r")
    lstVendedores=[]
    for linea in archVendedores.readlines():
        lstVendedores.append(linea[:-1].split(","))
    archVendedores.close
    archLq=open("liquidacionComisiones.txt","r")
    lstLq=[]
    for linea in archLq.readlines():
        lstLq.append(linea[:-1].split(","))
    archLq.close
    maxi=0
    band=0
    lstX=[]
    while band<5:
        for i in range(len(lstLq)):
            if (float(lstLq[i][1])>maxi) and not lstLq[i][1] in lstX:
                maxi=float(lstLq[i][1])
                i2=i
        lstX.append(lstLq[i2][1])
        for x in range(len(lstVendedores)):
            if lstLq[i2][0]==lstVendedores[x][0]:
                print("Codigo {}, Nombre {} y Comision {}".format(lstVendedores[x][0],lstVendedores[x][1],lstLq[i2][1]))
        band+=1
        maxi=0
topcinco()
    