def funcao():
    variavel_local = 10
    print(variavel_local)

variavel_global = 20

def funcao2():
    print(variavel_global)

funcao()
funcao2()
print(variavel_global)
print(variavel_local)
