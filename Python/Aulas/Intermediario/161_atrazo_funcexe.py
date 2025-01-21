# Adiar execução de funções

def soma(x, y):
    return x+y


def mult(x, y):
    return x*y


def executa(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_cinco = executa(soma, 5)
mulit_dez = executa(mult, 10)

print(soma_cinco(10))
print(mulit_dez(10))
