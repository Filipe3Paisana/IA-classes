stack = []

class pessoa :
    def __init__(self, nome, numero, curso):
        self.numero = numero
        self.nome = nome
        self.curso = curso



def add_pessoa(numero, nome, curso):
    pessoa(nome, numero, curso)
    push(stack, pessoa)

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
    print(stack)