# Exercicio para desfazer e refazer as tarefas desejadas
import os

def listar(tarefas):
    print()
    if not tarefas:
        print('Não tem tarefas para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')


def desfazer(tarefas, tarefa_feitas):
    print()
    if not tarefas:
        print('Não tem tarefas para desfazer')
        return

    tarefa = tarefas.pop()
    tarefa_feitas.append(tarefa)


def refazer(tarefas, tarefa_feitas):
    print()
    if not tarefa_feitas:
        print('Não tem tarefas para refazer')
        return

    tarefa = tarefa_feitas.pop()
    tarefas.append(tarefa)


def adcition(tarefa):
    print()
    if not tarefa.strip():
        print('CADE A TAREFA PAI')
        return


tarefa = []
tarefa_new = []

while True:
    print('Comandos: Listar, Desfazer, Refazer')
    tarefa = input('Digite um dos Comandos acima: ')

    if tarefa == 'Listar':
        listar(tarefa)
        continue

    elif tarefa == 'Desfazer':
        desfazer(tarefa, tarefa_new)
        continue

    elif tarefa == 'Refazer':
        refazer(tarefa, tarefa_new)
        continue

    elif tarefa == 'clear':
        os.system('clear')
        continue

    else:
        print('Digite um valor valido')
        continue
