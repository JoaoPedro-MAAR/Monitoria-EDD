import lista_sequencial.ListaSequencialNumPy as lsn

# Gustavo - Questão 1 - Prova 1
print("Questão 1")

# Gustavo - Questão 1 da prova
# Provavelmente a resolução de vocês vai mudar de acordo com a implementação da lista, estou usando uma lista sequencial um pouco diferente da de vocês.
def insere_ordenado(self, carga:any):  
  """ Método que insere um elemento na lista de forma ordenada.
        
    Args:
    carga (any): o conteúdo que deseja armazenar na lista.
        
    Raises:
    ListaError: Exceção lançada quando a lista está cheia.
        
    Examples:
        
    lst = Lista()
    lst.inserir(1, 4)
    lst.inserir(2, 28)
    lst.inserir(3, 34)
    lst.inserir(4, 55)
        
    lst.insere_ordenado(49)
        
    print(lst) # exibe [4, 28, 34, 49, 55]
  """  
              
  if self.estaCheia():
      raise ListaError('Lista cheia. Nao é possivel inserir elementos')
  posicao = 0
  for i in range(len(self.__dado)):
      if self.__dado[i] == None or carga < self.__dado[i]:
          posicao = i
          break
  self.inserir(posicao+1, carga)

lista = lsn.Lista()
print(lista)

lista.inserir(1, 4)
lista.inserir(2, 28)
lista.inserir(3, 34)
lista.inserir(4, 55)

print(lista)

lista.insere_ordenado(49)
lista.insere_ordenado(56)
lista.insere_ordenado(100)
lista.insere_ordenado(5)

print(lista)
print()

# Gustavo - Questão 3 - Prova 1
print("Questão 3")

class Processo:
  def __init__(self, pid, tempo_execucao, prioridade):
    self.pid = pid
    self.tempo_execucao = tempo_execucao
    self.prioridade = prioridade
    
  def __lt__(self, outroProcesso):
    return self.prioridade > outroProcesso.prioridade

class GerenciadorDeProcessos:
  def __init__(self):
    self.__jobs = lsn.Lista()
    
  def add(self, processo:Processo):
    self.__jobs.inserir(1, processo)
    
  def __executar_proximo_processo(self):
    """ Executa o próximo processo da fila de acordo com a prioridade """
    if self.__jobs.estaVazia():
      return
    
    processo = self.__get_processo()
    if processo is None:
      return
    
    processo.tempo_execucao -= 1
    
    if processo.tempo_execucao == 0:
      self.__jobs.remover(self.__jobs.busca(processo))
      print(f"Processo {processo.pid} finalizado")
    
  
  def __get_processo(self) -> Processo:
    """ Retorna o processo com maior prioridade 
    
    Returns:
    Processo: processo com maior prioridade
    """
    if self.__jobs.estaVazia():
      raise Exception("Não há processos na fila")
    
    prioridade = 1
    
    while True:
      for i in range(1, self.__jobs.__len__() + 1):
        processo = self.__jobs.get(i)
        if processo.prioridade == prioridade:
          return processo
      prioridade += 1
      
  def simular_tempo(self):
    self.__executar_proximo_processo()
    
  def __str__(self):
    print("Fila de processos:")
    for i in range(len(self.__jobs) , 0, -1):
      processo = self.__jobs[i]
      print(f"Processo {processo.pid} - Prioridade {processo.prioridade} - Tempo de execução {processo.tempo_execucao}")
    return ""

gp = GerenciadorDeProcessos()

p1 = Processo(1, 5, 2)
p2 = Processo(2, 3, 3)
p3 = Processo(3, 1, 1)

gp.add(p1)
gp.add(p2)
gp.add(p3)

for _ in range(10):
  gp.simular_tempo()
