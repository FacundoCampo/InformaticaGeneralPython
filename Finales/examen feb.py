"""#debe generar n numeros positivos a partir de 1, que son impares y multiplos de 3 o multiplos de 11
def generar(n):
    num=1
    i=0
    while num<n:
        if (num%2!=0 and num%3==0) or num%11==0:
            print(num,",",end="")
            i+=1
        num+=1
generar(30)"""
"""#recibe como parametros una lista lst y un numero n. debe eliminar de la lista a todos los n que aparezcan.
def eliminar(lst,n):
    i=0
    while i<len(lst):
        if lst[i]==n:
            lst.remove(lst[i])
        else:
            i+=1
    return lst
print(eliminar([1,1,2,2,1,3,1,9,1,4,5,1,1,8],1))"""
"""lst=[[1,2],"Hola Mundo",[6,1]]
print(lst[lst[0][0]][0:lst[2][0]])"""
"""def extraer_Palabras(nomArch):
    arch=open(nomArch,"r")
    lst=[]
    for linea in arch.readlines():
        lst.append(linea[:-1].split(","))
    arch.close
    palabra="";lst_fin=[]
    for i in range(len(lst)):
        for z in range(len(lst[i])):
            for x in range(len(lst[i][z])):
                if (lst[i][z][x]>="a" and lst[i][z][x]<="z"):
                    palabra+=lst[i][z][x]
                elif (lst[i][z][x]>="A" and lst[i][z][x]<="Z"):
                    palabra+=chr(ord(lst[i][z][x])+32)
                else:
                    if not palabra in lst_fin and palabra!="":
                        lst_fin.append("{}".format(palabra))
                    palabra=""
    return lst_fin
def f2(nomArch2,lst):
    dic={}
    arch=open(nomArch2,"r")
    lst2=[]
    for linea in arch.readlines():
        lst2.append(linea[:-1].split(","))
    arch.close
    
    for i in range(len(lst)):
        dic[lst[i]]=""
        for z in range(len(lst2)):
            for x in range(len(lst2[z])):
                if lst[i][len(lst[i])-4:]==lst2[z][x][len(lst2[z][x])-4:]:
                    dic[lst[i]]+="{},".format(lst2[z][x])
    print(dic)
nomArch="lstFeb.txt"
lst=extraer_Palabras(nomArch)
print("{} \n".format(lst))
nomArch2="lstFeb2.txt"
f2(nomArch2,lst)"""