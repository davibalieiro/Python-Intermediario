import json
from 206_exe_class_json_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
    print(dados)

    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])

    print(p1.nome)
    print(p2.nome)
    print(p3.nome)

if __name__ == '__main__':
    print('Bora')
    fazer_dump()