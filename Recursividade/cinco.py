###  **compareStr(char *str1, char *str2)**: Faça uma função recursiva que retorne:  
 #   - 0: str1 é igual a str2;  
  #  - 1: str1 é maior que str2;  
 #   - -1: str1 é menor que str2;  
 
 
 # bem não faço ideia de como fazer, não vou usar recursos de lenght ( Acho que a questão so trata de tamanho mesmo   )
 
def compareStr(str1,str2):
    if str1 == '' and str2 == '':
        return 0
    elif str1 == '' and str2 != '':
        return -1
    elif str1 != '' and str2 == '':
        return 1
    return compareStr(str1[1:],str2[1:])

print(compareStr('ovo','gorfo')) # -1

print(compareStr('Andrey','Joao')) # 1

print(compareStr('coco','cocô')) # 0

