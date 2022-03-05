"""def generar(n):
    num=1
    i=0
    while i<n:
        if (num>1 and num%2!=0 and num%3==0) or (num%11==0):
            print(num,",",end="")
            i+=1
        num+=1
generar(7)"""
"""def eliminar(lst,n):
    i=0
    while i<len(lst):
        if lst[i]==n:
            lst.remove(lst[i])
        else:
            i+=1
    return lst
print(eliminar([1,1,1,1,2,1,3,1,4,1,1,1,1,5,1],1))"""
"""lst=[[1,2],"hola mundo",[6,1]]
print(lst[lst[0][0]][0:lst[2][0]])"""
def f1(nomArch):
    arch=open(nomArch,"r")
    lst=[]
    for linea in arch.readlines():
        lst.append(linea[:-1].split(","))
    arch.close
    pal="";lst_fin=[]
    for i in range(len(lst)):
        for z in range(len(lst[i])):
            for x in range(len(lst[i][z])):
                if lst[i][z][x]>="a" and lst[i][z][x]<="z":
                    pal+=lst[i][z][x]
                elif lst[i][z][x]>="A" and lst[i][z][x]<="Z":
                    pal+=chr(ord(lst[i][z][x])+32)
                else:
                    if pal!="" and not pal in lst_fin:
                        lst_fin.append(pal)
                    pal=""
    return lst_fin
def f2(nomArch,lst):
    arch=open(nomArch,"r")
    lst2=[]
    for linea in arch.readlines():
        lst2.append(linea[:-1].split(","))
    arch.close
    dic={}
    lst_ay=[]
    for i in range(len(lst)):
        dic[lst[i]]=[]
        for x in range(len(lst2)):
            for y in range(len(lst2[x])):
                if len(lst[i])>=4 and lst[i][len(lst[i])-4:]== lst2[x][y][len(lst2[x][y])-4:]:
                    lst_ay.append(lst2[x][y])
                    dic[lst[i]]+=lst_ay
                    lst_ay=[]
    return dic
lst=f1("lstFeb.txt")
print(lst)
print(f2("lstFeb2.txt", lst))
