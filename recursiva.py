

def soma_recursiva(n):
    soma = 0
    total = []
    for item in n:
        if isinstance(item, list):
            soma_recursiva(item)
        else:
            soma += item
            total.apeend(soma)


if __name__ == "__main__":

    lista = [1, 2, [3, 4], [5, 6]]
    soma_recursiva(lista)
