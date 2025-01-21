# count é um iterador sem fim
from itertools import count

c1 = count()
print(next(c1))
# print('c1', hasattr(c1,'__iter__'))
# print('c1', hasattr(c1,'__next__'))


# detalhe é infinit lembrando

for i in c1:
    if i > 100:
        break
    print(i)
