# 2 **printstr()**: Faça uma função recursiva que imprima na tela uma string (caractere a caractere).  

def printstrX(string): # bem nao entendi se ele quer uma nova linha para cada palavas ou tudo numa linha so vamo fazer os dois 
    if len(string) == 1:
        print(string)
        return 
    print(string[0],end='')
    printstrX(string[1:])



printstrX('ovo')
printstrX('Pneumoultramicroscopicossilicovulcanoconiótico')


def printstrY(string):
    if len(string) == 1:
        print(string)
        return 
    print(string[0])
    printstrY(string[1:])
    

printstrY('ovo')
printstrY('Pneumoultramicroscopicossilicovulcanoconiótico')