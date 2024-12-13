class Node:
    def __init__(self,carga,proximo=None) -> None:
        self.carga = carga
        self.proximo = proximo
    
    def __str__(self) -> str:
        return str(self.carga)
    
    def igual(self,outronode):
        return self.carga == outronode.carga