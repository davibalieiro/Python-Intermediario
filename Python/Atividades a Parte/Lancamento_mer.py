
'''
Projeto: vendas
Cadastrar produtos com nome, preço e quantidade.
Listar todos os produtos cadastrados.
Atualizar o preço e a quantidade de um produto.
Realizar uma venda, atualizando a quantidade disponível.
Listar as vendas realizadas.
'''
import os


class manage_product:
    def __init__(self) -> None:
        self._stock = []
        self._sale = []

    def return_dicion_stock(self, product, amount, price) -> dict:
        return {'Produto': product, 'Quantidade do Produto': amount, 'Preço': price}

    def return_dicion_sale(self, item, amount):
        return {'Produto': item, 'Quantidade do Produto': amount}

    def cadastr_product(self):
        try:
            product = input("Qual é o nome do produto: ")
            qtd_product = int(input("Qual a quantidade desse produto: "))
            price_product = float(input("Digite o Preço desse produto: "))

            value_dicion = self.return_dicion_stock(
                product, qtd_product, price_product)
            self._stock.append(value_dicion)
            print("Produto novo cadrastrado com sucesso")
            os.system('cls')

        except ValueError:
            print(
                "Alguma coisa deu errado, Digite apenas numeros para Quantidade e Preço.")

    def sale(self):
        if len(self._stock) <= 0:
            print('Estoque vazio')
            return

        product_chosen = input("Escolha um produto: ")
        qtd_chosen = int(
            input("Quantas unidades desse produto serão levadas: "))
        product_found = False

        for product in self._stock:
            if product_chosen == product['Produto']:
                product_found = True
                if qtd_chosen <= product['Quantidade do Produto']:
                    product['Quantidade do Produto'] -= qtd_chosen
                    self._sale.append(self.return_dicion_sale(
                        product_chosen, qtd_chosen))
                    print(f'Foram vendidas: {qtd_chosen} '
                          f'unidades de {product_chosen}')
                    return
                else:
                    print('Quantidade insuficiente no estoque')
                    return

        if not product_found:
            print('Produto não encontrado no estoque')

    def list_stock(self):
        if not self._stock:
            print('Não a nada no estoque')
        else:
            for item in self._stock:
                print()
                print(f'Nome: {item['Produto']}')
                print(f'Quantidade: {item['Quantidade do Produto']}')
                print(f'Preço: {item['Preço']}')
                print()
                print('-' * 40)

    def list_sale(self):
        if not self._sale:
            print('Nada foi vendido por enquanto')
        else:
            print('*' * 40)
            for sale in self._sale:
                print()
                print(f'Foi vendido: {sale['Produto']}')
                print(f'Quantidade: {sale['Quantidade do Produto']}')
                print('-' * 40)

    def update_new_product(self):
        new_update_product = input('Digite qual produto deseja Atualizar: ')
        product_found = False
        for upadete in self._stock:
            if new_update_product == upadete['Produto']:
                try:
                    new_update_amonut = int(
                        input('Digite a Quantide que deseja Atualizar: '))
                    new_update_price = float(input('Digite o novo Preço:'))
                    upadete['Quantidade do Produto'] = new_update_amonut
                    upadete['Preço'] = new_update_price
                    print(f'Produto:{upadete}')
                    product_found = True
                    return
                except ValueError:
                    print(
                        "Alguma coisa deu errado, Digite apenas numeros para Quantidade e Preço.")
                    return
        if not product_found:
            print('Produto não encontrado')
    os.system('cls')


def main():
    product_registration_in_market = manage_product()
    while True:
        option = {
            '1': lambda: product_registration_in_market.cadastr_product(),
            '2': lambda: product_registration_in_market.sale(),
            '3': lambda: product_registration_in_market.update_new_product(),
            '4': lambda: product_registration_in_market.list_stock(),
            '5': lambda: product_registration_in_market.list_sale(),
        }
        print('Opções: \n 1.Cadastrar Estoque \n 2.Vender \n 3.Atualizar \n 4.Listar Estoque \n 5.Listar Vendas ')
        entrada = input('Escolha uma opção: ')

        if entrada not in option:
            print('Você esta fazendo coisa errada.')
        else:
            option[entrada]()


if __name__ == '__main__':
    main()
