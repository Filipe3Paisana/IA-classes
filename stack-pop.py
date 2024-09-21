stack = []

class Pessoa:
    def __init__(self, nome, numero, curso):
        self.numero = numero
        self.nome = nome
        self.curso = curso

def add_pessoa(numero, nome, curso):
    # Cria uma instância de 'Pessoa'
    pessoa_obj = Pessoa(nome, numero, curso)
    # Converte os atributos do objeto 'Pessoa' para um dicionário
    pessoa_dict = {
        "nome": pessoa_obj.nome,
        "numero": pessoa_obj.numero,
        "curso": pessoa_obj.curso
    }
    # Adiciona o dicionário à stack
    push(stack, pessoa_dict)

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
    curso = "Informatica"
    add_pessoa(numero, nome, curso)

def print_stack(stack):
    for pessoa in stack:
        print(f"Nome: {pessoa['nome']}")
        print(f"Numero: {pessoa['numero']}")
        print(f"Curso: {pessoa['curso']}")
        print("------------------------")

# Função principal para execução do código
if __name__ == "__main__":
    input_data()  # Adiciona uma pessoa à stack
    print_stack(stack)  # Imprime a stack
