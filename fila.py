#aula de python / faculdade / 28/05/25

# definição estrutua de pilha
#self.itens = vetor

#código gpt...

# Definindo a pilha como uma lista vazia
pilha = []

# Função para adicionar (empilhar) um elemento na pilha
def empilhar(item):
    pilha.append(item)
    print(f'{item} foi adicionado à pilha.')

# Função para remover (desempilhar) o elemento do topo da pilha
def desempilhar():
    if pilha_vazia():
        print('A pilha está vazia. Não é possível desempilhar.')
        return None
    else:
        item = pilha.pop()
        print(f'{item} foi removido da pilha.')
        return item

# Função para visualizar o elemento do topo da pilha
def topo():
    if pilha_vazia():
        print('A pilha está vazia.')
        return None
    else:
        return pilha[-1]

# Função para verificar se a pilha está vazia
def pilha_vazia():
    return len(pilha) == 0

# Função para exibir a pilha atual
def exibir# Definindo a pilha como uma lista vazia
pilha = []

# Função para adicionar (empilhar) um elemento na pilha
def empilhar(item):
    pilha.append(item)
    print(f'{item} foi adicionado à pilha.')

# Função para remover (desempilhar) o elemento do topo da pilha
def desempilhar():
    if pilha_vazia():
        print('A pilha está vazia. Não é possível desempilhar.')
        return None
    else:
        item = pilha.pop()
        print(f'{item} foi removido da pilha.')
        return item

# Função para visualizar o elemento do topo da pilha
def topo():
    if pilha_vazia():
        print('A pilha está vazia.')
        return None
    else:
        return pilha[-1]

# Função para verificar se a pilha está vazia
def pilha_vazia():
    return len(pilha) == 0

# Função para exibir a pilha atual
def exibir_pilha():
    if pilha_vazia():
        print('A pilha está vazia.')
    else:
        print('Pilha atual:', pilha)

# Exemplo de uso
empilhar(10)
empilhar(20)
empilhar(30)
exibir_pilha()

print('Topo da pilha:', topo())

desempilhar()
exibir_pilha()

desempilhar()
desempilhar()
desempilhar()  # Tentando desempilhar uma pilha vazia
_pilha():
    if pilha_vazia():
        print('A pilha está vazia.')
    else:
        print('Pilha atual:', pilha)

# Exemplo de uso
empilhar(10)
empilhar(20)
empilhar(30)
exibir_pilha()

print('Topo da pilha:', topo())

desempilhar()
exibir_pilha()

desempilhar()
desempilhar()
desempilhar()  # Tentando desempilhar uma pilha vazia
