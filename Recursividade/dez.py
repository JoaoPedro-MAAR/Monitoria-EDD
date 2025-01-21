'''

10. Um material radioativo denominado invictus, quando em contato com o oxigênio, perde metade de sua massa
a cada 50 segundos. Faça uma função recursiva que receba uma quantidade de massa do invictus, em gramas, 
e exiba o tempo (em segundos) necessário para que sua massa se torne menor que 0,8 g.
A função também deve retornar o valor da massa final.  

'''

def meiaVida(massa):
    return __meiaVida(massa,0)
    
    
    
def __meiaVida(massa,tempo):
    if massa<0.8:
        return massa,tempo
    return __meiaVida(massa/2,tempo+50)
    


# Quando voce não quer que o usuario passe um parametro é interessante fazer assim , principalmente quando o
# valor é necessario para as chamadas , porem seu primeiro valor pode ser obtido ou conhecido

print(meiaVida(10)) # 0.625 , 200
print(meiaVida(320)) # 0.625 , 650
print(meiaVida(2)) # 0.5  , 100
    