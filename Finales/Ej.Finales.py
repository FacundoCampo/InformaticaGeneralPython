def buscarS(xs,s):
    band=0
    i2=0
    tupla=(-1,-1)
    for i in range(len(s),len(xs)-1):
        if xs[i2:i]==s and band==0:
            ini=i2
            fin=i
            tupla=(ini,fin)
            band=1
        i2+=1
    return tupla
def listaIndice(xs,s):
    lstTupla=[]
    tup=buscarS(xs,s)
    if tup!=(-1,-1):
        lstTupla.append(tup)
        xs=xs[tup[1]:]
        while len(s)<len(xs):
            tup=buscarS(xs,s)
            if tup!=(-1,-1):
                lstTupla.append(tup)
                xs=xs[tup[1]:]
            else:
                xs=xs[tup[1]:]
    elif tup==(-1,-1):
        lstTupla.append([])
    return lstTupla
def main():
    s=str(input("Ingrese un str: "))
    arch=open("info.txt","r")
    for linea in arch.readlines():
        xs=linea
    print(listaIndice(xs,s))
    arch.close
main()
