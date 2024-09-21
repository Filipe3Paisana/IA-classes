def soma_recursiva(n):
    soma = 0
    for item in n:
        if isinstance(item, list):
            # Chama recursivamente para somar os itens dentro da sublista
            soma += soma_recursiva(item)
        else:
            soma += item
    return soma

if __name__ == "__main__":
    lista = [1, 2, [3, 4], [5, 6]]
    resultado = soma_recursiva(lista)
    print(f"Soma total: {resultado}")
