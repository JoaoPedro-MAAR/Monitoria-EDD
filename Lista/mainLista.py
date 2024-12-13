from Lista import Lista

lista = Lista()
for i in range(10):
    lista.append(i*10)
print(lista)
lista.append(10)
print("Checando duplicidade: ",lista.checarduplicidade())
print(lista)
lista.AlterarValor(200,0)
print("Checando duplicidade: ",lista.checarduplicidade())
print(lista) 
lista.remover(1)
print("Checando duplicidade: ",lista.checarduplicidade())
print(lista)   
