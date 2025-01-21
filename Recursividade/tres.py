# **invertString()**: Faça uma função recursiva que retorne a sequência de caracteres de uma string passada como argumento na ordem inversa.  

def inverterString(string):
    if len(string) == 1:
        return string
    return string[-1] + inverterString(string[:-1])




print(inverterString('ovo'))
print(inverterString('povao'))