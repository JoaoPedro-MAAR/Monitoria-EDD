# printInverse()**: Faça uma função recursiva que imprima uma string ao contrário. 

# Vou fazer so na horizontal mesmo e que se foda 
def printInverse(string):
    if len(string) == 1 or len(string) == 0:
        print(string)
        return
    print(string[-1],end='')
    printInverse(string[:-1])
    
    
printInverse('João Pedro')
printInverse('Andrey Vasconcelos')