"""def ordenArr(A):
    for i in range(len(A)):
        for j in range(1+i,len(A)):
            if(A[i]>A[j]):
                aux=A[i]
                A[i]=A[j]
                A[j]=aux
    return A
print(ordenArr([2,7,3,8,1]))"""
"""def decAbin(num):
    resto=0
    i=0
    bina =0
    while(num>0):
        resto=num%2
        num=num//2
        bina=bina+ resto*10**i
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
    archHab=open("habitantes.txt","r")
    lstHab=[]
    for linea in archHab.readlines():
        lstHab.append(linea[:-1].split(","))
    archHab.close
    
    archLoc=open("Localidad.txt","r")
    lstLoc=[]
    for linea in archLoc.readlines():
        lstLoc.append(linea[:-1].split(","))
    archLoc.close
    
    archHXL=open("habitantesXlocalidad.txt","r")
    lstHXL=[]
    for linea in archHXL.readlines():
        lstHXL.append(linea[:-1].split(","))
    archHXL.close
    
    for i in range(len(lstLoc)):
        if lstLoc[i][1]==nombreLocalidad:
            iD=lstLoc[i][0]
    lst_idHab=[]
    for i in range(len(lstHXL)):
        if lstHXL[i][0]==iD:
            lst_idHab.append(lstHXL[i][1])
    lst=[]
    for i in range(len(lst_idHab)):
        for z in range(len(lstHab)):
            if lstHab[z][0]==lst_idHab[i] and lstHab[z][2]==str(hijos):
                lst.append("{}, {}".format(lstHab[z][0],lstHab[z][1]))
    return lst
print(cantHabitantes("Lujan",3))"""
def edadXlocalidad():
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
    
    lst_id_loc=[]
    for i in range(len(lstHXL)):
        if not lstHXL[i][0] in lst_id_loc:
            lst_id_loc.append(lstHXL[i][0])
    for i in range(len(lst_id_loc)):
        for z in range(i+1,len(lst_id_loc)):
            if lst_id_loc[i]>lst_id_loc[z]:
                aux=lst_id_loc[i]
                lst_id_loc[i]=lst_id_loc[z]
                lst_id_loc=aux
        cant=0;edad=0
        for x in range (len(lstHXL)):
            if lstHXL[x][0]==lst_id_loc[i]:
                for y in range(len(lstHab)):
                    if lstHXL[x][1]==lstHab[y][0]:
                        cant+=1
                        edad+=int(lstHab[y][3])
        prom=edad/cant
        print("{}, {}\n".format(lst_id_loc[i],prom))
edadXlocalidad()