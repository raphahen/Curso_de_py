nome = input("Digite seu nome: ")

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao(nome)

def soma (a, b):
    return a + b
resultado = soma(3,4)
print(resultado)


quadrado = lambda x: x ** 2
print(quadrado(5))
