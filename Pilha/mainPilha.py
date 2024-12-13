from Pilha import Pilha

lista = Pilha()
for i in range(1,10):
    lista.append(i*10)


print(lista)

print("Tamanho: ", len(lista))#2
print("Adicionando 10")
lista.append(10)
print("Tamanho: ", len(lista))#3

print("Checando duplicidade: ",lista.checarduplicidade())
print(lista) 
lista.remover()
print("Checando duplicidade: ",lista.checarduplicidade())
print(lista)
print("Tamanho: ", len(lista))#2
   
print("Invertando")
lista.inverter()
print(lista)

