'''

6. **ispalindrome()**: Faça uma função recursiva que retorne verdadeiro caso uma string seja palíndrome, ou falso caso contrário. O protótipo da operação é definido por:  
    ```python
    def ispalindrome(str)
    ```


'''

def ispalindrome(string):
    if len(string) == 1 or len(string) == 0:
        return True
    if string[0] == string[-1]:
        return True and ispalindrome(string[1:-1])
    else:
        return False 
    
    
print(ispalindrome('ovo')) # True
print(ispalindrome('polo')) # False 
