import random
def aleatorio(a,b):
    num=(random.randint(a,b+1)%5)*2+1
    return num
print(aleatorio(100,300))
"""def cant_dig_impar(num):
    cont=0
    while num>0:
        dig=num%10
        if dig%2!=0:
            cont+=1
        num=num//10
    return not bool(cont%2)
print(cant_dig_impar(24688))"""