import meu_modulo
import utilidades
import operacoes

meu_modulo.saudar("João")

resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)

resultado = operacoes.somar(5, 3)
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")


nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")

#podemos fazer bibliotecas por conta propia para o uso da minha necessidade

