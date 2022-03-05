"""def ordenArr(a):
    for i in range (len(a)):
        for j in range (1+i,len(a)):
            if(a[i]> a[j]):
                aux=a[i]
                a[i]=a[j]
                a[j]=aux
    print(a)
ordenArr([2,7,3,8,1])
"""
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
print(decAbin(19))"""
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
x=list(range(10, 11, 12))
f1(x)"""
"""def cantHabitante(nombreLocalidad,hijos):
    archHabitantes=open("habitantes.txt","r")
    lstHabitantes=[]
    for linea in archHabitantes.readlines():
        lstHabitantes.append(linea[:-1].split(","))
    archHabitantes.close
    archLocalidades=open("localidades.txt","r")
    lstLocalidades=[]
    for linea in archLocalidades.readlines():
        lstLocalidades.append(linea[:-1].split(","))
    archLocalidades.close
    archhXl=open("habitantesXlocalidad.txt","r")
    lsthXl=[]
    for linea in archhXl.readlines():
        lsthXl.append(linea[:-1].split(","))
    archhXl.close
    idl=""
    for i in range(len(lstLocalidades)):
        if lstLocalidades[i][1]==nombreLocalidad:
            idl=lstLocalidades[i][0]
    lst_id=[]
    for i in range(len(lsthXl)):
        if lsthXl[i][0]==idl:
            lst_id.append(lsthXl[i][1])
    lst_indicado=[]
    for i in range(len(lstHabitantes)):
        for z in range(len(lst_id)):
            if lstHabitantes[i][0]==lst_id[z] and int(lstHabitantes[i][2])==hijos:
                lst_indicado.append(("{} : {}".format(lstHabitantes[i][0],lstHabitantes[i][1])))
    return lst_indicado
print(cantHabitante("Ezeiza",1))"""
def edadXlocalidad():
    archHabitantes=open("habitantes.txt","r")
    lstHabitantes=[]
    for linea in archHabitantes.readlines():
        lstHabitantes.append(linea[:-1].split(","))
    archHabitantes.close
    archhXl=open("habitantesXlocalidad.txt","r")
    lsthXl=[]
    for linea in archhXl.readlines():
        lsthXl.append(linea[:-1].split(","))
    archhXl.close
    lst_id_loc=[]
    for i in range(len(lsthXl)):
        if not lsthXl[i][0] in lst_id_loc:
            lst_id_loc.append(lsthXl[i][0])
    for i in range(len(lst_id_loc)):
        for z in range(1+i,len(lst_id_loc)):
            if int(lst_id_loc[i])>int(lst_id_loc[z]):
                aux=lst_id_loc[i]
                lst_id_loc[i]=lst_id_loc[z]
                lst_id_loc[z]=aux
    cant=0;edad=0
    for i in range(len(lst_id_loc)):
        for z in range(len(lsthXl)):
            if lst_id_loc[i]==lsthXl[z][0]:
                for x in range(len(lstHabitantes)):
                    if lsthXl[z][1]==lstHabitantes[x][0]:
                        edad+=int(lstHabitantes[x][3])
                        cant+=1
        print("ID Localidad: {} promedio edad: {}".format(lst_id_loc[i],(edad/cant)))
        edad=0
        cant=0
edadXlocalidad()
            