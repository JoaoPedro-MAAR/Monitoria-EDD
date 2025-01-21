'''
11. **seqTermos1()**: Faça uma função recursiva que calcule a soma dos n termos da série:  
     ```python
     n = 1 2 3 4 5 n
     série: 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/n
     def seqTermos1(n):
          if n == 1:
                return 1
'''



def seqTermos1(n):
    if n == 1:
        return 1
    return (1/n) + seqTermos1(n-1)

print(seqTermos1(3)) # 1.833 dizima
print(seqTermos1(8)) # 2.7178571428571425