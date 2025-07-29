def adiciona_cliente(name, lista=None):
    if lista is None:
        lista=[]
    lista.append(name)
    return lista

cliente1 = adiciona_cliente('CR')
adiciona_cliente('MR',cliente1)
print(cliente1)

cliente2 = adiciona_cliente('Lua')
adiciona_cliente('JS',cliente2)
print(cliente1)
