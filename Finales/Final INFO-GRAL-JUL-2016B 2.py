"""def ordenar(a):
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i] > a[j]:
                aux=a[i]
                a[i]=a[j]
                a[j]=aux
    return a
def main():
    a=[2,7,3,8,1]
    print(ordenar(a))
main()"""
"""
def decAbin(num):
    resto=0
    i=0
    bina=0
    while (num>0):
        resto=num%2
        num=num//2
        bina=bina+resto*(10**i)
        i=i+1
    return bina
def main():
    print(decAbin(19))
main()"""
"""
def f1(x):
    for i in range(0,len(x)):
        if(i in x):
            print('a',end="")
        else:
            print('b',end="")
x=list(range(10, 1, 2))
f1(x)
"""
"""
s=['Juan','Carlos']
s="Carlos"
s="Juan"
s[0]='x'
print(s)
"""
"""
def cantHabitantes(nombreLocalidad,hijos):
    archHabitante=open("habitantes.txt","r")
    lstHabitante=[]
    for linea in archHabitante.readlines():
        lstHabitante.append(linea[:-1].split(","))
    archHabitante.close
    archLocalidades=open("localidades.txt","r")
    lstLocalidades=[]
    for linea in archLocalidades.readlines():
        lstLocalidades.append(linea[:-1].split(","))
    archLocalidades.close
    archHxL=open("habitantesXlocalidad.txt","r")
    lstHxL=[]
    for linea in archHxL.readlines():
        lstHxL.append(linea[:-1].split(","))
    archHxL.close
    for i in range(len(lstLocalidades)):
        if lstLocalidades[i][1]==nombreLocalidad:
            id_Localidad=lstLocalidades[i][0]
    lst_id_habit=[]
    for i in range(len(lstHxL)):
        if id_Localidad==lstHxL[i][0]:
            lst_id_habit.append(lstHxL[i][1])
    lstResult=[]
    for i in range (len(lstHabitante)):
        for z in range(len(lst_id_habit)):
            if lst_id_habit[z]==lstHabitante[i][0]:
                if int(lstHabitante[i][2])==hijos:
                    lstResult.append([lstHabitante[i][0],lstHabitante[i][1]])
    return lstResult
def main():
    print(cantHabitantes("Lujan",3))
main()
"""
def edadXlocalidad():
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
    archHxL=open("habitantesXlocalidad.txt","r")
    lstHxL=[]
    for linea in archHxL.readlines():
        lstHxL.append(linea[:-1].split(","))
    archHxL.close
    lst_id_localidad=[]
    for i in range(len(lstHxL)):
        if not lstHxL[i][0] in lst_id_localidad:
            lst_id_localidad.append(lstHxL[i][0])
    cant_hab=int()
    años=int()
    for i in range (len(lst_id_localidad)):
        for z in range (len(lstHxL)):
            if lst_id_localidad[i]==lstHxL[z][0]:
                for x in range(len(lstHabitantes)):
                    if lstHxL[z][1]==lstHabitantes[x][0]:
                        años+=int(lstHabitantes[x][3])
                        cant_hab+=1
        prom=años/cant_hab
        print("id localidad {} --> promedio edad {}".format(lst_id_localidad[i],prom))
        cant_hab=int()
        años=int()
edadXlocalidad()