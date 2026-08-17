try: 
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")


try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")


try:
    # Código gerou exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção
exit()
