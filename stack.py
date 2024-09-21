stack = []

class Pessoa:
    def __init__(self, nome, numero, curso):
        self.numero = numero
        self.nome = nome
        self.curso = curso

def add_pessoa(numero, nome, curso):
    
    pessoa_obj = Pessoa(nome, numero, curso)
    
    push(stack, pessoa_obj)

def push(stack, value):
    stack.append(value)
    return stack

def pop(stack):
    if len(stack) > 0:
        return stack.pop()

def peek(stack):
    if not stack:
        return None
    return stack[-1]

def is_empty(stack):
    return not bool(stack)

def input_data():
    numero = 123
    nome = "Filipe"
    curso = "informatica"
    add_pessoa(numero, nome, curso)

if __name__ == "__main__":
    input_data()  

    
    print("Stack atual:", stack)
    
    
    pessoa_top = peek(stack)
    if pessoa_top:
        print(f"Topo da stack: {pessoa_top.nome}, {pessoa_top.numero}, {pessoa_top.curso}")
    
    
    pessoa_removida = pop(stack)
    if pessoa_removida:
        print(f"Elemento removido: {pessoa_removida.nome}, {pessoa_removida.numero}, {pessoa_removida.curso}")
    
    
    print("Stack após pop:", stack)

    
    print("Stack está vazia?", is_empty(stack))
stack = []

class Pessoa:
    def __init__(self, nome, numero, curso):
        self.numero = numero
        self.nome = nome
        self.curso = curso

def add_pessoa(numero, nome, curso):
    # Cria uma instância da classe Pessoa e armazena em uma variável
    pessoa_obj = Pessoa(nome, numero, curso)
    # Passa a instância criada para a função push
    push(stack, pessoa_obj)

def push(stack, value):
    stack.append(value)
    return stack

def pop(stack):
    if len(stack) > 0:
        return stack.pop()

def peek(stack):
    if not stack:
        return None
    return stack[-1]

def is_empty(stack):
    return not bool(stack)

def input_data():
    numero = 123
    nome = "Filipe"
    curso = "informatica"
    add_pessoa(numero, nome, curso)

if __name__ == "__main__":
    input_data()  # Adiciona a pessoa à stack

    
    print("Stack atual:", stack)
    
    
    pessoa_top = peek(stack)
    if pessoa_top:
        print(f"Topo da stack: {pessoa_top.nome}, {pessoa_top.numero}, {pessoa_top.curso}")
    
    
    pessoa_removida = pop(stack)
    if pessoa_removida:
        print(f"Elemento removido: {pessoa_removida.nome}, {pessoa_removida.numero}, {pessoa_removida.curso}")
    
    
    print("Stack após pop:", stack)

    
    print("Stack está vazia?", is_empty(stack))
