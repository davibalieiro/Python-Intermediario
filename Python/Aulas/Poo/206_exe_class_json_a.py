# Exercicios - Salvar class em Json
import json
CAMINHO_ARQUIVO = '206_exe_class_json.json'

class Pessoa:
    def __init__(self, name, years ) -> None:
        self.nome = name
        self.idade = years


p1 = Pessoa('CR7', 40)
p2 = Pessoa('CR7', 35)
p3 = Pessoa('CR7', 22)
lista = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('Fazendo dump...')
        json.dump(lista, arquivo, ensure_ascii=False, indent=2)
    