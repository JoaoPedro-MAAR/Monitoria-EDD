# 1. **recursiveLength()**: Faça uma função recursiva que retorne a quantidade de caracteres de uma string.  

def recursiveLength(string):
    if len(string) == 1:
        return 1
    return 1 + recursiveLength(string[1:])

# Teste 

print(recursiveLength('ovo')) # 3
print(recursiveLength('ronaldinho')) # 10