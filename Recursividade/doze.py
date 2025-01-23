'''
12. **seqTermos2()**: Faça uma função recursiva que calcule a soma dos n termos da série:  
     ```python
     4 + 55 + 106 + 177 + 268 + ⋯ + (n^2 + 1) / (n + 3)
     def seqTermos2(n)
'''

# Entendi nada wtf 
def seqTermos2(n):
     if n==1:
          return (2/4)
     return (((n**2)+1)/(n+3))+seqTermos2(n-1)



print(seqTermos2(5))