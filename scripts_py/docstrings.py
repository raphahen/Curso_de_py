base = float(input("Digite a base do seu retângulo: "))
autura = float(input("Digite a altura do seu retângulo: "))

def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
    return base * altura

def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_variavel(1, 2, 3))
print(soma_variavel(4, 5, 6, 7))
