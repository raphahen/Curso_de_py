def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("descrição do erro")
try:
    funcao()
except Exeception as e:
    print(f"ERRO: {str(e)}")
    
