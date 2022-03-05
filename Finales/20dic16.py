def sacar_n(lst):
    new_lst=[]
    for line in lst:
        if "\n" in line:
            new_lst.append(line[:-1])
        else:
            new_lst.append(line)
    return new_lst
#tengo problemas con el 1er numero del csv, y en vez de 60 me toma 6    
def factura(id_abonado):
    file=open("abonados.csv","r")
    lineas=file.readlines()
    lineas=sacar_n(lineas)
    file.close()
    dic_ab={}
    for f in lineas:
        f=f.split(",")
        dic_ab[int(f[0])]=[f[1],f[2], f[3]]
    file2=open("cate.csv", "r")
    contenido=file2.readlines()
    contenido= sacar_n(contenido)
    file2.close()
    dic_cat={}
    for line in contenido:
        line=line.split(",")
        dic_cat[line[0]]= [float(line[1]), float(line[2])]
    f3=open("conex.csv", "r")
    read=f3.readlines()
    read=sacar_n(read)
    f3.close()
    lis=[] #me crea lista de sub [['ï»¿6', '1'], ['1', '15'], ['8', '12'],
    for linea in read:
        linea=linea.split(",") #ya me crea la list
        lis.append(linea) #a el append no le puedo pasar 2 arg
    suma=0 
    for sl in lis:
        if sl[0]==str(id_abonado):
            suma+=int(sl[1])#problemas con los minutos, y el 3 inicial
    if id_abonado in list(dic_ab.keys()):
        nombre=dic_ab[id_abonado][0]
        domi=dic_ab[id_abonado][1]
        a=dic_ab[id_abonado][2]
        abono=float(dic_cat[a][0])
        importe= float((dic_cat[a][1]))*suma #con int me da cero
        total=abono+importe
    
    print("nombre:{}\n domicilio:{}\nabono:{}\nimporte:{}\ntotal:{}".format(nombre,domi,abono,importe,total))      
factura(3)







'''f3=open("conex.csv", "r")
read=f3.readlines()
f3.close() 
dic_con={}
for linea in read:
    linea=linea.split(",")
    dic_con[linea[0]]=linea[1]     #si se repiten los keys, va actualizando el value
print(dic_con)'''
        
''' f3=open("conex.csv", "r")
    read=f3.readlines()
    read=sacar_n(read)
    f3.close()
    lis=[] #me crea ñista de sub [['ï»¿6', '1'], ['1', '15'], ['8', '12'],
    
    for linea in read:
        linea=linea.split(",") #ya me crea la list
        lis.append(linea) #a el append no le puedo pasar 2 arg
    aux=[] #ñps id_ab repetidos
    for sl in lis:
        #if sl[0] not in aux:
        aux.append(sl[0])
    print(aux)
    '''
'''cont=[]
   
    for sl in lis:
        if sl[0]==str(id_abonado):
            #problemas con los minutos, y el 3 inicial
            cont.append(sl[1])'''