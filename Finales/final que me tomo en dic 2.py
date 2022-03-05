import random
def aleatorio(a,b):
    num=((random.randint(a,b))%5)*2+1
    return num
print(aleatorio(0,1000000000))
