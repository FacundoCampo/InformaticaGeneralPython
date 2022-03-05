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
print(esPrimo(11))"""
"""def espalindromo (texto):
    palindromo=True
    for i in range(len(texto)):
        if(texto[-i-1]!=texto[i]):
            palindromo=False
    return palindromo
print(espalindromo("rayar"))"""
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
print(comparar(1,1000004,199999999999))"""
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
    archVentas=open("ventastarjetas.txt","r")
    lstVentas=[]
    for linea in archVentas.readlines():
        lstVentas.append(linea[:-1].split(","))
    archVentas.close
    archVend=open("vendedores.txt","r")
    lstVend=[]
    for linea in archVend.readlines():
        lstVend.append(linea[:-1].split(","))
    archVend.close
    archLq=open("liquidacionComisiones 6.txt","w")
    lst_id=[]
    for i in range(len(lstVend)):
        if not lstVend[i][0] in lst_id:
            lst_id.append(lstVend[i][0])
    for i in range(len(lst_id)):
        cant=0
        for z in range(len(lstVentas)):
            if lstVentas[z][0]==lst_id[i]:
                cant+=int(lstVentas[z][2])
        for x in range(len(lstVend)):
            if lstVend[x][0]==lst_id[i]:
                goal=int(lstVend[x][2])
                x2=x
        prom=(cant*100)/goal
        lst_ag=[]
        if prom<80:
            lst_ag.append(lst_id[i])
            lst_ag.append(str(float(lstVend[x2][3]*0)))
        elif prom>80 and prom<100:
            lst_ag.append(lst_id[i])
            lst_ag.append(str(float(lstVend[x2][3])*0.03))
        elif prom>100:
            lst_ag.append(lst_id[i])
            lst_ag.append(str(float(lstVend[x2][3])*0.1))
        archLq.write(",".join(lst_ag)+"\n")
    archLq.close
liquidar()"""

def topCinco():
    archVend=open("vendedores.txt","r")
    lstVend=[]
    for linea in archVend.readlines():
        lstVend.append(linea[:-1].split(","))
    archVend.close
    archLq=open("liquidacionComisiones 6.txt","r")
    lstLq=[]
    for linea in archLq.readlines():
        lstLq.append(linea[:-1].split(","))
    archLq.close
    lst_com=[]
    for i in range(len(lstLq)):
        if not lstLq[i][1] in lst_com:
            lst_com.append(lstLq[i][1])
    for i in range(len(lst_com)):
        for z in range(1+i,len(lst_com)):
            if float(lst_com[i])<float(lst_com[z]):
                aux=lst_com[i]
                lst_com[i]=lst_com[z]
                lst_com[z]=aux
    top=5
    for i in range(len(lst_com)):
        for z in range(len(lstLq)):
            if lst_com[i]==lstLq[z][1]:
                iD=lstLq[z][0]
        for x in range(len(lstVend)):
            if lstVend[x][0]==iD and top>0:
                print("Codigo: {}".format(iD))
                print("Nombre: {}".format(lstVend[x][1]))
                print("Comision: {}\n".format(lst_com[i]))
                top-=1
topCinco()