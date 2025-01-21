# Escopo da classe e metodos da class

class Animal:
    # nome = 'Leo'
    
    def __init__(self, name) -> None:
        self.nome = name
        # var = 'value'
        # print(var)

    def comendo(self):
        alimento = input('Digite o que o leao ta comendo:')
        return f'{self.nome} esta comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    

leao = Animal(name='Leo')
print(leao.nome)
print(leao.comendo())