import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from No import Node


class Pilha:
    def __init__(self) -> None:
        #Vamo usar a implementação head and tail com uma lista encadead 
        self.topo = None
        self.size = 0
        
    def __len__(self) -> int:
        return self.size
    
    def estavazia(self):
        return self.size == 0
    
    def adicionar(self,carga):
        self.topo = Node(carga, self.topo)
        self.size += 1
        
    def append(self,carga):
        self.adicionar(carga)
        
    def remover(self):
        if self.estavazia():
            raise IndexError("Lista vazia")
        carga = self.topo
        self.topo = self.topo.proximo
        self.size -= 1 
        return carga
                
        
                
    def pop(self):
        self.remover()
                

                
    def buscarPosicao(self,posicao):
        return self.__buscarPosicaoNode(posicao).carga
    
    def __buscarPosicaoNode(self,posicao):
        if posicao < 0 or posicao > self.size:
            raise IndexError("Posição inválida")
        inicio = self.topo
        if self.size == 1:
            return self.topo
        for _ in range(posicao):
            inicio = inicio.proximo
        return inicio
    
    def buscarCarga(self,carga):
        inicio = self.topo
        for i in range(self.size):
            if inicio.carga == carga:
                return i+1
            inicio = inicio.proximo
        return None
    
    def checarduplicidade(self):
        inicio = self.topo
        for i in range(self.size):
            elemento_da_vez = inicio
            inicio = inicio.proximo
            for j in range(i+1,self.size):
                if elemento_da_vez.igual(inicio):
                    return True
                inicio = inicio.proximo
            inicio = elemento_da_vez.proximo
        return False
    
    
    
    
    
    def __str__(self):
        if self.estavazia():
            return "[]"
        
        inicio = self.topo
        lista = []
        for _ in range(self.size):
            lista.append(str(inicio.carga))
            inicio = inicio.proximo
        return "Topo -> "+" ".join(lista)
    
    def inverter(self):
        tamanho = self.size
        list = []
        while  not self.estavazia():
            valor = self.remover()
            list.append(valor)
            
        list.reverse()
        for _ in range(tamanho):
            self.adicionar(list.pop())
            
    
    
    