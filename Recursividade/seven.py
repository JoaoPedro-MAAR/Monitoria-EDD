# 7. Escreva uma função recursiva que retorne a soma dos n primeiros números inteiros. Se n = 3, a soma seria igual a 1 + 2 + 3 = 6.  

def Somatorio(n):
    if n == 1:
        return 1
    return n + Somatorio(n-1)



print(Somatorio(3)) # 6 
print(Somatorio(500)) # 125250

 