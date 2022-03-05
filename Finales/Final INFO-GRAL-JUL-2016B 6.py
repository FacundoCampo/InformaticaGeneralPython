"""def ordenArr(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if(A[i]>A[j]):
                aux=A[i]
                A[i]=A[j]
                A[j]=aux
    print(A)
ordenArr([2,7,3,8,1])"""
"""def decAbin(num):
    resto=0
    i=0
    bina=0
    while(num>0):
        resto=num%2
        num=num//2
        bina=bina+resto*10**i
        i=i+1
    return bina
print(decAbin(42996606))"""
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
"""s=['Juan','Carlos']
s="Carlos"
s="Juan"
s[0]='x'
print(s)"""
"""def cantHabitantes(nombreLocalidad,hijos):
    archHab=open("habitantes.txt","r")
    lstHab=[]
    for linea in archHab.readlines():
        lstHab.append(linea[:-1].split(","))
    archHab.close

    archLoc=open("localidad.txt","r")
    lstLoc=[]
    for linea in archLoc.readlines():
        lstLoc.append(linea[:-1].split(","))
    archLoc.close
    
    archHXL=open("habitantesXlocalidad.txt","r")
    lstHXL=[]
    for linea in archHXL.readlines():
        lstHXL.append(linea[:-1].split(","))
    archHXL.close
    hijos=str(hijos)
    for i in range(len(lstLoc)):
        if lstLoc[i][1]==nombreLocalidad:
            id_loc=lstLoc[i][0]
    lst_id_hab=[]
    for i in range(len(lstHXL)):
        if lstHXL[i][0]==id_loc:
            lst_id_hab.append(lstHXL[i][1])
    lst=[]
    for i in range(len(lst_id_hab)):
        for z in range(len(lstHab)):
            if lstHab[z][0]==lst_id_hab[i] and lstHab[z][2]==hijos:
                lst.append((lst_id_hab[i],lstHab[z][1]))
    return lst
print(cantHabitantes("Lujan",3))"""
"""def edadXlocalidad():
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
    for i in range(len(lst_id_loc)):
        for x in range(i+1,len(lst_id_loc)):
            if lst_id_loc[i]>lst_id_loc[x]:
                aux=lst_id_loc[i]
                lst_id_loc[i]=lst_id_loc[z]
                lst_id_loc[z]=aux
    for i in range(len(lst_id_loc)):
        lst_id_hab=[];edad=0;cant=0
        for z in range(len(lstHXL)):
            if lstHXL[z][0]==lst_id_loc[i]:
                lst_id_hab.append(lstHXL[z][1])
        for x in range(len(lst_id_hab)):
            for y in range(len(lstHab)):
                if lstHab[y][0]==lst_id_hab[x]:
                    edad+=int(lstHab[y][3])
                    cant+=1
        if cant>0:
            print("Id_loc: {}, Promedio: {}".format(lst_id_loc[i],edad//cant))
edadXlocalidad()"""