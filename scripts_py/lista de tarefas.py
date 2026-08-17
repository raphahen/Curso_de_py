"""
Gerenciador de Tarefas - CLI
Projeto simples em Python para praticar:
- Funções
- Listas e dicionários
- Manipulação de arquivos (JSON)
- Estruturas de repetição e condicionais
- Interação com o usuário via terminal

Autor: Rapha
"""

import json
import os
from datetime import datetime

ARQUIVO_DADOS = "tarefas.json"


def carregar_tarefas():
    """Lê as tarefas salvas no arquivo JSON. Se não existir, retorna lista vazia."""
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo JSON."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


def adicionar_tarefa(tarefas):
    descricao = input("Descrição da tarefa: ").strip()
    if not descricao:
        print(">> A descrição não pode ser vazia.\n")
        return

    nova_tarefa = {
        "descricao": descricao,
        "concluida": False,
        "criada_em": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print(">> Tarefa adicionada com sucesso!\n")


def listar_tarefas(tarefas):
    if not tarefas:
        print(">> Nenhuma tarefa cadastrada.\n")
        return

    print("\n--- Suas Tarefas ---")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "[X]" if tarefa["concluida"] else "[ ]"
        print(f"{indice}. {status} {tarefa['descricao']} (criada em {tarefa['criada_em']})")
    print()


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        numero = int(input("Número da tarefa a marcar como concluída: "))
        indice = numero - 1
        if indice < 0 or indice >= len(tarefas):
            print(">> Número inválido.\n")
            return

        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        print(">> Tarefa marcada como concluída!\n")
    except ValueError:
        print(">> Digite um número válido.\n")


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        numero = int(input("Número da tarefa a remover: "))
        indice = numero - 1
        if indice < 0 or indice >= len(tarefas):
            print(">> Número inválido.\n")
            return

        removida = tarefas.pop(indice)
        salvar_tarefas(tarefas)
        print(f">> Tarefa '{removida['descricao']}' removida.\n")
    except ValueError:
        print(">> Digite um número válido.\n")


def exibir_menu():
    print("=" * 35)
    print("      GERENCIADOR DE TAREFAS")
    print("=" * 35)
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")
    print("=" * 35)


def main():
    tarefas = carregar_tarefas()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Até logo!")
            break
        else:
            print(">> Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
