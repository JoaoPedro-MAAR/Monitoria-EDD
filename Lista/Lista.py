import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from No import Node


class Lista:
    def __init__(self) -> None:
        #Vamo usar a implementação head and tail com uma lista encadead 
        self.head = None
        self.tail = None
        self.size = 0
        
    def __len__(self) -> int:
        return self.size
    
    def estavazia(self):
        return self.size == 0
    
    def adicionar(self,carga,posicao):
        if posicao < 0 or posicao > self.size:
            #Chega as posições válidas ou seja so dentro do espectro da de 0 ao tamanho da lista
            raise IndexError("Posição inválida")
        novo = Node(carga)
        if posicao == 0:
            novo.proximo = self.head
            self.head = novo
            if self.size == 0:
                self.tail = novo
        else:
            inicio = self.head
            for i in range(posicao-1):
                inicio = inicio.proximo
            novo.proximo = inicio.proximo
            inicio.proximo = novo
            if posicao == self.size:
                self.tail = novo
        self.size += 1
        
    def append(self,carga):
        self.adicionar(carga,self.size)
        
    def remover(self,posicao):
        if self.estavazia():
            raise IndexError("Lista vazia")
        elif posicao < 0 or posicao >= self.size:
            raise IndexError("Posição inválida")
        elif posicao == 0:
            carga = self.head
            self.head = self.head.proximo
            return carga
        else:
            inicio = self.head
            for i in range( posicao-1):
                inicio = inicio.proximo
            carga = inicio.proximo
            inicio.proximo = inicio.proximo.proximo
            if posicao == len(self):
                self.tail = inicio
            self.size -= 1 
            return carga
        
                
    def pop(self):
        self.remover(self.size-1)
                
    def AlterarValor(self,carga,posicao):
        self.__buscarPosicaoNode(posicao).carga = carga
                
    def buscarPosicao(self,posicao):
        return self.__buscarPosicaoNode(posicao).carga
    
    def __buscarPosicaoNode(self,posicao):
        if posicao < 0 or posicao >= self.size:
            raise IndexError("Posição inválida")
        inicio = self.head
        for i in range(posicao):
            inicio = inicio.proximo
        return inicio
    
    def buscarCarga(self,carga):
        inicio = self.head
        for i in range(self.size):
            if inicio.carga == carga:
                return i+1
            inicio = inicio.proximo
        return None
    
    def checarduplicidade(self):
        inicio = self.head
        for i in range(self.size):
            elemento_da_vez = inicio
            inicio = inicio.proximo
            for _ in range(i+1,self.size):
                if elemento_da_vez.igual(inicio):
                    return True
                inicio = inicio.proximo
            inicio = elemento_da_vez.proximo
        return False
    
    
    
    
    
    def __str__(self):
        if self.estavazia():
            return "[]"
        
        inicio = self.head
        lista = []
        for i in range(self.size):
            lista.append(str(inicio.carga))
            inicio = inicio.proximo
        return " ".join(lista)
    
    
    
    