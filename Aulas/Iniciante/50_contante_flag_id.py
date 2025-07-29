'''
Variavel constante = letra Maiuscula = exe(CARRO_CORRIDA)
Muita condições no seu if (ruim)
    <- Contagem de complexidade (ruim)
'''

velocidade = 81  # Velocidade do carro
local_carro = 90  # Localização do carro

RADAR_1 = 80  # Velocidade maxima permidida
LOCAL_1 = 100  # Local do Radar
RADAR_RANGE = 1  # A distancia onde o radar vai pegar

velocidade_ultrapassada = velocidade > RADAR_1

condicao_multa = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_ultrapassada:
    print('O carro passou da velocidade')

if condicao_multa and velocidade_ultrapassada:
    print('O carro foi multado')

'''
Flag (Bandeira) - Marcal um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
'''
condicao = True
passou = None
if condicao:
    passou = True
    print('algo')
else:
    print('algo nao')

if passou is None:
    print('Nao passou no if')

# if passou is not None:
else:
    print('Passou no if')
