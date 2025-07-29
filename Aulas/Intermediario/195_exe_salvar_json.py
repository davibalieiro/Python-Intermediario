# Exercicio para desfazer e refazer as tarefas desejadas
import os
import json

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

def ler(caminho, outro_caminho):
    dados = []
    try:
        with open(outro_caminho, 'r',encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    
    except FileNotFoundError:
        print('Nao existe pai')
        salvar(caminho, outro_caminho)
        return dados

def salvar(caminho, outro_caminho):
    dados = caminho
    with open(outro_caminho, 'w',encoding='utf8') as arquivo:
            dados = json.dump(caminho, arquivo, indent=2, ensure_ascii=False)
    return dados
    

CAMINHO_ARQUIVO = '195_exe_salvar_json_exem.py'
tarefa = ler([], CAMINHO_ARQUIVO)
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
    
