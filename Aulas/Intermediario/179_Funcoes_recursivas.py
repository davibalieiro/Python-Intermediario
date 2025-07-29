# Funcao recursivas e recursividade
# Funcao que podem se chamar de volta
# uteis p/ dividie problemas grandes em partes menores Toda funcao recursiva deve ter:
# Um problema que posso ser dividido em parte menores
# Um caso recursivo que resolve o pequeno problema
# Um caso base que para a recursao
# Fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120
import sys
sys.setrecursionlimit(1004)

def recursiva(inic=0, end=10):
    # caso base
    print(inic,end)
    if inic >= end:
        return inic,end

    # caso recursivo -- contar ate o final
    inic+=1
    return recursiva(inic,end)
    # ele salva isso na memoria

print(recursiva())
print(recursiva(0,1000))
# outra coisa

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
