import os


class FinanceManager:  # Criando um tipo
    def __init__(self, money=0):
        self.money = money


class UserData(FinanceManager):  # UserData extends FinanceManager
    def __init__(self, money=0):  # <--
        super().__init__(money=0)

        self.expenses = {
            'alimentacao': 0,  # 0 = valor gasto
            'entretenimento': 0,  # tipo alimentação, entretenimento etc
            'saude': 0,
            'filhos': 0,
            'educacao': 0,
            'transporte': 0,  # Dinheiro gasto
        }

    def add_dinheiro(self):  # criar uma função para adicionar dinheiro á conta
        while True:
            try:
                dinheiro = float(input('Quanto quer colocar dinheiro: '))
                self.money += dinheiro
                print(f'Saldo atual: {self.money}')
                break
            except:
                print('Digite apenas valor inteiro')
                continue

    def gastar(self):  # criar uma função que subtrai o dinheiro atual e adiciona ao indice pegado do usuario a self.expanses
        try:
            dinheiro_gasto = float(input('Digite o valor gasto: '))

            print('Opções\n')
            cmd_gastar = {
                '1': 'alimentacao',
                '2': 'entretenimento',
                '3': 'saude',
                '4': 'filhos',
                '5': 'educacao',
                '6': 'transporte',
            }

            for i, item in cmd_gastar.items():  # <--
                print(f'{i}. {item}')

            escolha = input('Escolha uma opção: ').lower()
            if escolha not in cmd_gastar:
                print('Opção desconhecida')

            else:
                self.expenses[cmd_gastar[escolha]
                              ] += dinheiro_gasto  # type: ignore
                self.money -= dinheiro_gasto
            print(f'Saldo atual: {self.money}')

        except ValueError:
            print('Error')

        except Exception as e:
            print(f'Um erro ocorreu: {e}')

    # fazer um relatorio, tendo o nome do item que gastou e quanto gastou naquele item

    def gerar_relatorio(self):

        total = sum(self.expenses.values())
        os.system('cls')
        print('Relatório de gasto')
        for i, item in self.expenses.items():

            print(f'{i.capitalize()}. R${item:.2f}')

        print(f'Total: R${total:.2f}')

    def ver_se_teve_lucro(self):
        # self.money -> acessa o dinheiro atual

        # se o dinheiro for menor que o total, crie uma variavel substituindo o total - o dinheiro atual

        # senão, é profit
        total = sum(self.expenses.values())

        if self.money < total:
            total_novo = self.money - total
            os.system('cls')
            print(f'Você teve perca de R${total_novo:.2f}')
        else:
            total_novo = self.money - total
            os.system('cls')
            print(f'Você teve lucro de R${total_novo:.2f}')


def main():
    sistema = UserData()
    while True:
        cmd = {
            # vai executar a açãode adicionar dinheiro se a tecla 1 for enviada
            '1': lambda: sistema.add_dinheiro(),
            '2': lambda: sistema.gastar(),
            '3': lambda: sistema.gerar_relatorio(),
            '4': lambda: sistema.ver_se_teve_lucro(),
            '5': lambda: exit()
        }
        print(f'Dinheiro atual: {sistema.money}')
        print('Opções \n 1. Adicionar Dinheiro \n 2. Gasto \n 3. Gerar Relatorio \n 4. Ver estado atual \n 5. Sair')
        get_cmd = input('Digite uma opção: ').strip()

        if get_cmd not in cmd:
            os.system('cls')
        else:
            cmd[get_cmd]()


if __name__ == '__main__':  # Se ESSE arquivo for rodado, rode essa função
    main()
