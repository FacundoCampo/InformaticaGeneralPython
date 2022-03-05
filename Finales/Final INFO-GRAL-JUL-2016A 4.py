"""def esPrimo(n):
    primo=False
    i=2
    while(i>0):
        
        for x in range(1,n+1):
            if n%x==0:
                i-=1
        if i==0:
            primo=True
    return primo
print(esPrimo(16))"""
"""def espalindromo (texto):
    palindromo=True
    for i in range(len(texto)):
        if(texto[-i-1]!=texto[i]):
            palindromo=False
    return palindromo
print(espalindromo("rayarar"))"""
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
"""xn=[1,2,3,4]
n=1234
print((2 in xn) and (2 in n))"""
"""def liquidar():
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
    archLC=open("liquidacionComisiones 4.txt","w")
    lstLC=[]
    lstID=[]
    for i in range(len(lstVendedores)):
        if not lstVendedores[i][0] in lstID:
            lstID.append(lstVendedores[i][0])
    tarjetas=0
    for i in range(len(lstID)):
        for z in range(len(lstVentas)):
            if lstID[i]==lstVentas[z][0]:
                tarjetas+=int(lstVentas[z][2])
        for y in range(len(lstVendedores)):
            if lstID[i]==lstVendedores[y][0]:
                objetivo=int(lstVendedores[y][2])
                y2=y
        comision=(tarjetas/objetivo)*100
        if comision<80:
            lstLC.append(str(lstID[i]))
            lstID.append(str(lstVendedores[y2][3]))
        elif comision>80 and comision<100:
            lstLC.append(str(lstID[i]))
            lstLC.append(str(float(lstVendedores[y2][3])*0.03))
        elif comision>100:
            lstLC.append(str(lstID[i]))
            lstLC.append(str(float(lstVendedores[y2][3])*0.1))
        archLC.write(",".join(lstLC)+"\n")
        tarjetas=0
        lstLC=[]
    archLC.close
liquidar()"""
def topCinco():
    archVendedores=open("vendedores.txt","r")
    lstVendedores=[]
    for linea in archVendedores.readlines():
        lstVendedores.append(linea[:-1].split(","))
    archVendedores.close
    archLC=open("liquidacionComisiones 4.txt","r")
    lstLC=[]
    for linea in archLC.readlines():
        lstLC.append(linea[:-1].split(","))
    archLC.close
    maxi=0;lstMax=[];top=0
    while top<5:
        for i in range(len(lstLC)):
            if float(lstLC[i][1])>maxi and not lstLC[i][1] in lstMax:
                maxi=float(lstLC[i][1])
                i2=i
        lstMax.append(lstLC[i2][1])
        for z in range(len(lstVendedores)):
            if lstLC[i2][0]==lstVendedores[z][0]:
                z2=z
        print("{} {} {}".format(lstLC[i2][0],lstVendedores[z2][1],lstLC[i2][1]))
        maxi=0
        top+=1
topCinco()
        
    