'''
Escopo de função em Python
Escopo significa o local onde aquele codigo pode atingir
Existe o escopo global e o local
O escopo global é o escopo onde todo o codigo é alcançavel
O escopo local é onde apenas nome do mesmo local podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escoposexternos
A palavra global faz uma variavel do escopo externo ser a mesma no escopo interno

'''
x = 1


def escopo():
    global x
    x = 10

    def outro():
        x = 20
        y = 2
        print(x, y)
    outro()
    print(x)


print(x)
escopo()
print(x)
