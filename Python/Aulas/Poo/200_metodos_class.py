# Metodos em Instancias de classes Python:
# Hard coded = É algo que foi escrito diretamente no codigo
# self é padrao sempre bom colocar

class Carro:
    def __init__(self, name):
        self.nome = name

    def acelerar(self, ):
        print(f'{self.nome} esta acelerando')

# Carro.acelerar() # Isso vai dar error obviamente, mais so pra lembrar
fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
# Outro jeito
fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()

celta.acelerar()
Carro.acelerar(celta)
