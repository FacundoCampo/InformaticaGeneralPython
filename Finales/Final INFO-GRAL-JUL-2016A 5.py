"""def esPrimo(n):
    primo=False
    i=2
    while(i>0):
        for z in range(1,n+1):
            if n%z==0:
                i-=1
        if i==0:
            primo=True
        else:
            i=-1
    return primo
print(esPrimo(12))"""
"""def espalindromo (texto):
    palindromo=True
    for i in range(len(texto)):
        if(texto[-i-1]!=texto[i]):
            palindromo=False
    return palindromo
print(espalindromo("ana"))"""
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
"""xn=[1,2,3,4]
n=1234
print((2 in xn) and (2 in n))"""
"""def liquidar():
    archVentas=open("ventasTarjetas.txt","r")
    lstVentas=[]
    for linea in archVentas.readlines():
        lstVentas.append(linea[:-1].split(","))
    archVentas.close
    
    archVend=open("vendedores.txt","r")
    lstVend=[]
    for linea in archVend.readlines():
        lstVend.append(linea[:-1].split(","))
    archVend.close
    
    archLQ=open("liquidacionComisiones 5.txt","w")
    archLQ.close
    
    archLQ=open("liquidacionComisiones 5.txt","a")
    lst_id=[]
    for i in range(len(lstVend)):
        if not lstVend[i][0] in lst_id:
            lst_id.append(lstVend[i][0])
    
    for i in range(len(lst_id)):
        cant=0;lst_ag=[]
        for z in range(len(lstVentas)):
            if lst_id[i]==lstVentas[z][0]:
                cant+=int(lstVentas[z][2])
        for x in range(len(lstVend)):
            if lst_id[i]==lstVend[x][0]:
                obj=int(lstVend[x][2])
                x2=x
        prom=(cant*100)/obj
        if prom<80:
            lst_ag.append(lst_id[i])
            lst_ag.append("0")
        elif prom>80 and prom<100:
            lst_ag.append(lst_id[i])
            lst_ag.append(str(float(lstVend[x2][3])*0.03))
        elif prom>100:
            lst_ag.append(lst_id[i])
            lst_ag.append(str(float(lstVend[x2][3])*0.1))
        archLQ.write(",".join(lst_ag)+"\n")
    archLQ.close
liquidar()"""
def topcinco():
    archVend=open("vendedores.txt","r")
    lstVend=[]
    for linea in archVend.readlines():
        lstVend.append(linea[:-1].split(","))
    archVend.close
    
    archLQ=open("liquidacionComisiones 5.txt","r")
    lstLQ=[]
    for linea in archLQ.readlines():
        lstLQ.append(linea[:-1].split(","))
    archLQ.close
    
    lstCom=[]
    
    for i in range(len(lstLQ)):
        if not lstLQ[i][1] in lstCom:
            lstCom.append(lstLQ[i][1])
    for x in range(len(lstCom)):
        for i in range(1+x,len(lstCom)):
            if float(lstCom[x])<float(lstCom[i]):
                aux=lstCom[x]
                lstCom[x]=lstCom[i]
                lstCom[i]=aux
    lstAux=[]
    for z in range(len(lstCom)):
        if len(lstAux)<5:
            lstAux.append(lstCom[z])
            for i in range(len(lstLQ)):
                if lstCom[z]==lstLQ[i][1]:
                    id=lstLQ[i][0]
                    print("Codigo: {}".format(id))
            for y in range(len(lstVend)):
                if lstVend[y][0]==id:
                    print("Nombre: {}".format(lstVend[y][1]))
                    print("Comision: {}".format(lstCom[z]))
topcinco()