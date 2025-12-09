import os

lista_tarefas = []

def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    if nome.strip() != "":
        tarefa = {"descricao": nome, "status": "Pendente"}
        lista_tarefas.append(tarefa)
        print("Tarefa adicionada!")
        salvar_dados()
    else:
        print("Nome inválido")


def menu():
    print("1 - Adicionar")


while True:
    print("\n Gerenciador de Tarefas")
    menu()
    opc = input("Opção: ")

    if opc == "1":
        adicionar_tarefa()
