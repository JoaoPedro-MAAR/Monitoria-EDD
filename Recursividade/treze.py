'''
13. Dado um vetor de números reais, escreva uma função recursiva para determinar a soma dos elementos do vetor.  

'''


    
    
def SomaAll(vetor):
    if len(vetor) == 1:
        return vetor[0]
    return vetor[0] + SomaAll(vetor[1:])



vetor = [ 1,2,3] # 6
print(SomaAll(vetor))
vetor2 = [23, 45, 12, 67, 34, 89, 21, 56, 78, 90] # 515
print(SomaAll(vetor2))

