# Curso: Sistemas para Internet/Redes de Computadores  
## Disciplina: Estrutura de Dados  
### Período: 2º  
#### Professor: Alex Sandro da Cunha Rêgo  

## Recursividade

### Como criar uma função recursiva

Uma função recursiva é uma função que se chama a si mesma para resolver subproblemas menores de um problema maior. Para criar uma função recursiva, siga os seguintes passos:
Defina o problema: Entenda claramente o problema que você está tentando resolver e como ele pode ser dividido em subproblemas menores.

Identifique o caso base: O caso base é a condição que termina a recursão. Sem um caso base, a função recursiva entraria em um loop infinito. O caso base geralmente é a condição mais simples do problema, que pode ser resolvida diretamente sem necessidade de recursão.

Divida o problema: Divida o problema em subproblemas menores que se aproximem do caso base. A função recursiva deve chamar a si mesma com esses subproblemas.

Combine os resultados: Combine os resultados dos subproblemas para resolver o problema maior.

#### Exemplo de função recursiva

Vamos criar uma função recursiva para calcular o fatorial de um número:

```python
def fatorial(n):
    # Caso base: fatorial de 0 ou 1 é 1
    if n == 0 ou n == 1:
        return 1
    # Chamada recursiva: n * fatorial de (n-1)
    else:
        return n * fatorial(n-1)
```

Neste exemplo:
- O caso base é quando `n` é 0 ou 1, onde o fatorial é 1.
- A função se chama recursivamente com `n-1` até atingir o caso base.
- Os resultados das chamadas recursivas são combinados multiplicando `n` pelo fatorial de `n-1`.

### Identificando casos base

Para identificar casos base, pergunte-se:
- Qual é a condição mais simples do problema?
- Quando a função deve parar de se chamar recursivamente?
- Qual é o resultado direto para essa condição simples?

Encontrar o caso base é crucial para garantir que a função recursiva termine corretamente e não entre em um loop infinito.
### STRINGS  

1. **recursiveLength()**: Faça uma função recursiva que retorne a quantidade de caracteres de uma string.  
2. **printstr()**: Faça uma função recursiva que imprima na tela uma string (caractere a caractere).  
3. **invertString()**: Faça uma função recursiva que retorne a sequência de caracteres de uma string passada como argumento na ordem inversa.  
4. **printInverse()**: Faça uma função recursiva que imprima uma string ao contrário.  
5. **compareStr(char *str1, char *str2)**: Faça uma função recursiva que retorne:  
    - 0: str1 é igual a str2;  
    - 1: str1 é maior que str2;  
    - -1: str1 é menor que str2;  
6. **ispalindrome()**: Faça uma função recursiva que retorne verdadeiro caso uma string seja palíndrome, ou falso caso contrário. O protótipo da operação é definido por:  
    ```python
    def ispalindrome(str)
    ```

### VARIADOS  

7. Escreva uma função recursiva que retorne a soma dos n primeiros números inteiros. Se n = 3, a soma seria igual a 1 + 2 + 3 = 6.  
8. **menores_rec()**: Faça uma função recursiva que receba como parâmetro uma lista de valores numéricos e um número inteiro key. A função deve retornar quantos elementos da lista possuem valor inferior a key. O protótipo da função é definido por:  
    ```python
    def menores_rec(lista, key)
    ```
9. **decToBin()**: Faça uma função recursiva que receba um número inteiro na base decimal e imprima seu correspondente na base binária. O protótipo da função é definido por:  
    ```python
    def decToBin(num)
    ```
10. Um material radioativo denominado invictus, quando em contato com o oxigênio, perde metade de sua massa a cada 50 segundos. Faça uma função recursiva que receba uma quantidade de massa do invictus, em gramas, e exiba o tempo (em segundos) necessário para que sua massa se torne menor que 0,8 g. A função também deve retornar o valor da massa final.  
11. **seqTermos1()**: Faça uma função recursiva que calcule a soma dos n termos da série:  
     ```python
     n = 1 2 3 4 5 n
     série: 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/n
     def seqTermos1(n):
          if n == 1:
                return 1
     ```
12. **seqTermos2()**: Faça uma função recursiva que calcule a soma dos n termos da série:  
     ```python
     4 + 55 + 106 + 177 + 268 + ⋯ + (n^2 + 1) / (n + 3)
     def seqTermos2(n)
     ```
13. Dado um vetor de números reais, escreva uma função recursiva para determinar a soma dos elementos do vetor.  
14. Dado um vetor de números inteiros, escreva uma função recursiva para identificar o maior valor armazenado no vetor.  
15. Dado um vetor de números inteiros, escreva uma função recursiva para verificar se um vetor está ordenado ou não.  
16. O código abaixo imprime, de forma recursiva, o Triângulo de Pascal. De acordo com o programa, qual a sequência numérica a ser impressa para cada iteração do comando for inserido no programa principal?  
     ```python
     def pascal(n):
          if n == 1:
                return [1]
          else:
                line = [1]
                previous_line = pascal(n-1)
                for i in range(len(previous_line)-1):
                     line.append(previous_line[i] + previous_line[i+1])
                line += [1]
                return line

     # Aqui se inicia o programa principal
     for i in range(1, 6):
          print(pascal(i))
     ```

### Torre de Hanói  

17. Torre de Hanói é um "quebra-cabeça" clássico com solução via recursividade que consiste em uma base contendo três pinos, em um dos quais são dispostos alguns discos uns sobre os outros, em ordem crescente de diâmetro, de cima para baixo. O problema consiste em passar todos os discos de um pino para outro qualquer, usando um dos pinos como auxiliar, de maneira que um disco maior nunca fique em cima de outro menor em nenhuma situação. O número de discos pode variar sendo que o mais simples contém apenas três.  
     ```python
     Hastes: A B C
     ```

     É interessante observar que o número mínimo de "movimentos" para conseguir transferir todos os discos da primeira estaca à terceira é 2^n - 1, sendo n o número de discos. Logo:  
     - Para solucionar um Hanói de 4 discos, são necessários 15 movimentos  
     - Para solucionar um Hanói de 7 discos, são necessários 127 movimentos  
     - Para solucionar um Hanói de 15 discos, são necessários 32.767 movimentos  

     Acompanhe a solução recursiva do problema da Torre de Hanói e exiba o que vai ser impresso na tela.  
     ```python
     def moveTower(numDiscos, origem, destino, auxiliar):
          '''
          numDiscos: int - Quantidade de discos a movimentar.
          origem: identificador da torre de origem
          destino: identificador da torre destino.
          temp: identificador da torre auxiliar
          '''
          if numDiscos >= 1:
                moveTower(numDiscos-1, origem, auxiliar, destino)
                moveDisco(origem, destino)
                moveTower(numDiscos-1, auxiliar, destino, origem)

     def moveDisco(origem, destino):
          print("Movendo disco da haste", origem, "para a haste", destino)

     moveTower(3, "A", "B", "C")
     ```

18. Implemente uma função recursiva que converta um número da base decimal para qualquer uma das seguintes bases: binária (2), octal (8) e hexadecimal (16). A função deve obedecer ao seguinte protótipo:  
     ```python
     def decToBase(num, base)
     ```
19. Faça uma função recursiva que retorne a soma de todos os elementos de uma lista de inteiros passada como argumento. O protótipo da função é definido por:  
     ```python
     def somaLista(lista)
     ```

### Estrutura de Dados Prof: Alex Sandro C. Rêgo 
