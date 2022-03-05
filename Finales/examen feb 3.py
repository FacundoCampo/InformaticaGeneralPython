"""def generar(n):
    num=1
    i=0
    while i<n:
        if (num%2!=0 and num%3==0) or num%11==0:
            print(num,",",end="")
            i+=1
        num+=1
generar(11)"""
"""def eliminar(lst,n):
    i=0
    while i<len(lst):
        if lst[i]==n:
            lst.remove(lst[i])
        else:
            i+=1
    print(lst)
eliminar([1,2,3,1,1,1,1,4,1,1,1,1,5,6,1],1)"""

"""lst=[[1,2],"hola mundo",[6,1]]
print(lst[lst[0][0]][0:lst[2][0]])"""
def f1(nomArch):
    arch=open(nomArch,"r")
    lst=[]
    for linea in arch.readlines():
        lst.append(linea[:-1].split(","))
    arch.close
    lst_fin=[]
    for i in range(len(lst)):
        for z in range(len(lst[i])):
            palabra=""
            for x in range(len(lst[i][z])):
                if lst[i][z][x]>="a" and lst[i][z][x]<="z":
                    palabra+=lst[i][z][x]
                elif lst[i][z][x]>="A" and lst[i][z][x]<="Z":
                    palabra+=chr(ord(lst[i][z][x])+32)
                else:
                    if not palabra in lst_fin and palabra!="":
                        lst_fin.append(palabra)
                    palabra=""
    return lst_fin
def f2(nomArch,lst):
    arch=open(nomArch,"r")
    lst2=[]
    for linea in arch.readlines():
        lst2.append(linea[:-1].split(","))
    arch.close
    dic={}
    for i in range(len(lst)):
        dic[lst[i]]=[]
        lst_ag=[]
        for z in range(len(lst2)):
            for x in range(len(lst2[z])):
                if lst2[z][x][len(lst2[z][x])-4:]==lst[i][len(lst[i])-4:]:
                    lst_ag.append(lst2[z][x])
        dic[lst[i]]+=lst_ag
    return dic

lst=f1("lstFeb.txt")
print(f2("lstFeb2.txt",lst))