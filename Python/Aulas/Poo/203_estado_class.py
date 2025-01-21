# Mantendo estado dentro da classe

class Camera:
    def __init__(self, name, filmando=False):
        self.name = name
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.name}Burro ta filmado')
            return

        print(f'{self.name} esta filmando algo')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.name}nao ta filmado')
            return

        print(f'{self.name} agora ela esta parando de filmando algo')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.name} nao pode tirar foto agora')
            return
        
        print(f'{self.name}Ta fotogarfando')

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
c1.filmar()

# print(c1.filmando)
# print(c2.filmando)


