"""def ordenArr(a):
    for i in range(len(a)):
        for j in range(1+i,len(a)):
            if(a[i]>a[j]):
                aux=a[i]
                a[i]=a[j]
                a[j]=aux
    return a
print(ordenArr([2,4,3,5,7,8,1,9,6]))"""
"""def decAbin(num):
    resto=0
    i=0
    bina =0
    while(num>0):
        resto=num%2
        num=num//2
        bina=bina+resto*10**i
        i=i+1
    return bina
print(decAbin(9))"""
"""def fa(a):
    return fb(a)+1
def fb(b):
    for i in range(0, len(b)):
        return int("".join(b))+i
a=['1','2']
print ("{0:d}{1:d}".format(fb(a),fa(a)))"""
"""def comparar(a,b,c):
    if((a and(b or c)) == ((a and b)or(a and c))):
        return True
    else:
        return False
print ("{0:d}{0:d}".format(0,comparar(1,1,1)))"""
"""def f1(x):
    for i in range(0,len(x)):
        if(i in x):
            print('a',end="")
        else:
            print('b',end="")
x=list(range(10, 1, 2))
f1(x)"""
"""def cantHabitantes(nombreLocalidad,hijos):
    archLoc=open("localidades.txt","r")
    lstLoc=[]
    for linea in archLoc.readlines():
        lstLoc.append(linea[:-1].split(","))
    archLoc.close
    
    archHXL=open("habitantesXlocalidad.txt","r")
    lstHXL=[]
    for linea in archHXL.readlines():
        lstHXL.append(linea[:-1].split(","))
    archHXL.close
    
    archHab=open("habitantes.txt","r")
    lstHab=[]
    for linea in archHab.readlines():
        lstHab.append(linea[:-1].split(","))
    archHab.close
    
    hijos=str(hijos)
    for i in range(len(lstLoc)):
        if lstLoc[i][1]==nombreLocalidad:
            id_Loc=lstLoc[i][0]
    lst_id_hab=[]
    for y in range(len(lstHXL)):
        if lstHXL[y][0]==id_Loc:
            lst_id_hab.append(lstHXL[y][1])
    lstRes=[]
    for z in range(len(lst_id_hab)):
        for x in range(len(lstHab)):
            if lstHab[x][0]==lst_id_hab[z] and lstHab[x][2]==hijos:
                lstRes.append("{}, {}".format(lst_id_hab[z],lstHab[x][1]))
    return lstRes
print(cantHabitantes("Lujan",3))"""
def edadXlocalidad():
    archHab=open("habitantes.txt","r")
    lstHab=[]
    for linea in archHab.readlines():
        lstHab.append(linea[:-1].split(","))
    archHab.close
    archHXL=open("habitantesXlocalidad.txt","r")
    lstHXL=[]
    for linea in archHXL.readlines():
        lstHXL.append(linea[:-1].split(","))
    archHXL.close
    lst_id_loc=[]
    for i in range(len(lstHXL)):
        if not lstHXL[i][0] in lst_id_loc:
            lst_id_loc.append(lstHXL[i][0])
    for z in range(len(lst_id_loc)):
        for y in range(1+z,len(lst_id_loc)):
            if lst_id_loc[z]>lst_id_loc[y]:
                aux=lst_id_loc[z]
                lst_id_loc[z]=lst_id_loc[y]
                lst_id_loc[y]=aux
    for x in range(len(lst_id_loc)):
        edad=0;cant=0
        for n in range(len(lstHXL)):
            if lstHXL[n][0]==lst_id_loc[x]:
                for p in range(len(lstHab)):
                    if lstHab[p][0]==lstHXL[n][1]:
                        edad+=int(lstHab[p][3])
                        cant+=1
        print("id_loc: {}, prom edad: {}".format(lst_id_loc[x], edad/cant))
edadXlocalidad()