"""def esPrimo(n):
    primo=False
    i=2
    while(i>0):
        for z in range(1,n+1):
            if n%z==0:
                i-=1
        if i==0:
            primo=True
    return primo
print(esPrimo(6))"""
"""def espalindromo (texto):
    palindromo=True
    for i in range(len(texto)):
        if(texto[-i-1]!=texto[i]):
            palindromo=False
    return palindromo
print(espalindromo("ana"))"""
def comparar(a,b,c):
    if((a and (b or c)) != ((a and b)or(a and c))):
        return True
    else:
        return False
print(comparar(1,1,1))
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
    
    archLQ=open("liquidacionComisiones 7.txt","w")
    lst=[]
    for i in range(len(lstVend)):
        if not lstVend[i][0] in lst:
            lst.append(lstVend[i][0])
    for i in range(len(lst)):
        cant=0
        for z in range(len(lstVentas)):
            if lst[i]==lstVentas[z][0]:
                cant+=int(lstVentas[z][2])
        for x in range(len(lstVend)):
            if lst[i]==lstVend[x][0]:
                goal=int(lstVend[x][2])
                x2=x
        prom=(cant*100)/goal
        lst_ag=[]
        if prom<80:
            lst_ag.append(lst[i])
            lst_ag.append(str(int(lstVend[x2][3])*0))
        elif prom>80 and prom<100:
            lst_ag.append(lst[i])
            lst_ag.append(str(float(lstVend[x2][3])*0.03))
        elif prom>100:
            lst_ag.append(lst[i])
            lst_ag.append(str(float(lstVend[x2][3])*0.1))
        archLQ.write(",".join(lst_ag)+"\n")
    archLQ.close
liquidar()"""
"""def topcinco():
    archVend=open("vendedores.txt","r")
    lstVend=[]
    for linea in archVend.readlines():
        lstVend.append(linea[:-1].split(","))
    archVend.close
    
    archLQ=open("liquidacionComisiones 7.txt","r")
    lstLQ=[]
    for linea in archLQ.readlines():
        lstLQ.append(linea[:-1].split(","))
    archLQ.close
    lst=[]
    for i in range(len(lstLQ)):
        if not lstLQ[i][1] in lst:
            lst.append(lstLQ[i][1])
    top=0
    for i in range(len(lst)):
        for x in range(i+1,len(lst)):
            if float(lst[i])< float(lst[x]):
                aux=lst[x]
                lst[x]=lst[i]
                lst[i]=aux
        
        for z in range(len(lstLQ)):
            if lst[i]==lstLQ[z][1]:
                iD=lstLQ[z][0]
        for y in range(len(lstLQ)):
            if lstLQ[y][0]==iD and top<5:
                print("Codigo: {}".format(iD))
                print("Nombre: {}".format(lstLQ[y][1]))
                print("Comision: {}\n".format(lst[i]))
                top+=1
topcinco()"""
        