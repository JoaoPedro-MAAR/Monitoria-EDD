import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from No import Node


class Fila:
    def __init__(self) -> None:
        self.inicio = None
        self.fim = None
        self.size = 0
        
    def __len__(self) -> int:
        return self.size
    
    def estavazia(self):
        return self.size == 0
    
    def adicionar(self,carga):
        novo = Node(carga)
        if self.estavazia():
            self.inicio = novo
            self.fim = self.inicio
        else:
            self.fim.proximo = novo
            self.fim = novo
        self.size += 1
        
    def append(self,carga):
        self.adicionar(carga)
        
    def remover(self):
        if self.estavazia():
            raise IndexError("Lista vazia")
        carga = self.inicio
        self.inicio = self.inicio.proximo
        self.size -= 1
        return carga
        
                
    def pop(self):
        self.remover(self.size-1)
                
    def buscarPosicao(self,posicao):
        return self.__buscarPosicaoNode(posicao).carga
    
    def __buscarPosicaoNode(self,posicao):
        #Busca por posição e retornar o no
        if posicao < 0 or posicao >= self.size:
            raise IndexError("Posição inválida")
        inicio = self.inicio
        for i in range(posicao):
            inicio = inicio.proximo
        return inicio
    
    def buscarCarga(self,carga):
        inicio = self.inicio
        for i in range(self.size):
            if inicio.carga == carga:
                return i+1
            inicio = inicio.proximo
        return None
    
    def checarduplicidade(self):
        inicio = self.inicio
        for i in range(self.size):
            elemento_da_vez = inicio
            inicio = inicio.proximo
            for j in range(i+1,self.size):
                if elemento_da_vez.igual(inicio):
                    return True
                inicio = inicio.proximo
            inicio = elemento_da_vez.proximo
        return False
    
    
    def concatenar(self,f2):
        #Não foi especificado como deveriamos concatenar então so botaremos um com outro a f1(nossa fila) sera a primeira e o f2 a segunda
        while not f2.estavazia():
            self.adicionar(f2.remover())
            
            
    
    
    def __str__(self):
        if self.estavazia():
            return "[]"
        
        inicio = self.inicio
        lista = []
        for i in range(self.size):
            lista.append(str(inicio.carga))
            inicio = inicio.proximo
        return "Inicio - > "+" ".join(lista) +"<- Fim "
    
    
    
    