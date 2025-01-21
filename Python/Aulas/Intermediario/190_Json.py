import json
pessoa = {
    'nome': 'Davi',
    'sobrenome': 'Balieiro',
    'endero': [
        {'rua': 'R1', 'numero': 47},
        {'rua': 'R2', 'numero': 14},
    ],
    'altura': 1.8,
    'n': (1,2,3,4,5),
    'dev': True,
    'nada': None
}

with open('aula190_json', 'w') as arquivo:
    json.dump(pessoa,arquivo)
    