'''8. **menores_rec()**: Faça uma função recursiva que receba como parâmetro uma lista de valores numéricos e um número inteiro key. A função deve retornar quantos elementos da lista possuem valor inferior a key. O protótipo da função é definido por:  
    ```python
    def menores_rec(lista, key)
    ```'''
    
    
    
def menores_rec(lista,key):
    if len(lista) == 0:
        return 0
    if lista[0] < key:
        return 1 + menores_rec(lista[1:], key)
    return 0 + menores_rec(lista[1:], key)
    
    
lista = [1 , 5 , 9 , 10 , 13 , 7 , 0]
key = 8
print(menores_rec(lista,key)) # 4
print(menores_rec(lista,1)) # 1