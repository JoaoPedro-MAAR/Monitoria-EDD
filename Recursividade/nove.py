'''9. **decToBin()**: Faça uma função recursiva que receba um número inteiro na base decimal e imprima seu correspondente na base binária. O protótipo da função é definido por:  
    ```python
    def decToBin(num)
    ```
'''

def __decToBin(num):
    if num > 1:
        __decToBin(num // 2)
    print(num % 2, end='')
    
def decToBin(num):
    __decToBin(num)
    print()

decToBin(10)  # 1010

decToBin(255)  # 11111111


# Fiz isso para ter quebra de linha se nao ficava muito feio