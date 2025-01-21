"""
contendo um menu inicial com as opções de:
registrar paciente

ver pacientes e o id dos pacientes

"""
import secrets
import string as st

random = secrets.SystemRandom()

letras = st.ascii_letters
numeros = st.digits


def gerar_dicionario(nome: str, id_: str) -> dict:
    return {'nome': nome, 'id': id_}


pacientes = [

]

execucao = 0
while execucao < 3:

    nomes_paciente = str(input('Digite um o seu nome: '))
    combinacao = ''.join(random.choices(letras + numeros, k=5))
    dicionario = gerar_dicionario(nomes_paciente, combinacao)
    pacientes.append(dicionario)
    execucao += 1


for pessoa in pacientes:
    print(f'{pessoa['nome']} - {pessoa['id']}')
    print('-'*50)


nome_codigo = str(input('Digite o nome: '))
chegar_id = str(input('Digite o id: '))

encontrar = False
for item in pacientes:
    if nome_codigo == item['nome'] and chegar_id == item['id']:
        print('Pessoa encontrada')
        encontrou = True
        break

if not encontrar:
    print('Pessoa não encontrada')
    exit()
