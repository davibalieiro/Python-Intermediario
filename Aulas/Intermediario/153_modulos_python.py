# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
from sys import platform as pf
from sys import exit as ex
import sys as s
from sys import exit, platform
import sys

platform = 'A MINHA'
print(sys.platform)
print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

print(platform)

# alias 1 - import nome_modulo as apelido

sys = 'alguma coisa'
print(s.platform)
print(sys)


# alias 2 - from nome_modulo import objeto as apelido

print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

print(platform)
exit()

# Entendendo os proprios modulos do Python
# O primeiro se chama __main__
# Voce pode importar outro modulo  inteiro ou parte abaixo dele
# O puthon conhece todos os modulo e pacotes presente nos
# caminhos de sys.path
# import aula105
print('Esse é', __name__)
# print(aula105.alguma_variavel_de_la)
