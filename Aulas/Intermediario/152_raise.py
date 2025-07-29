# raise - lançamento exceções (eros)

def division_zero(d):
    if d == 0:
        raise ZeroDivisionError('Não pai')


def division(n, d):
    if not isinstance(d, (float, int)):
        raise TypeError('Denov não')

    division_zero(d)
    return n/d


print(division(8, 0))
