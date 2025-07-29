# Sistema de uma Barbearia
# Sera necessario: lançamento de venda, adicionais, estoque, adicionar ao estoque, retirar do estoque, opção de pagamento, chek-list de tudo pai.

class manage_product:
    def __init__(self) -> None:
        self._stock = []
        self._sale = []
        self._corte = []

    def return_dict_stock(self, product, price, amonut):
        return {'Product': product, 'Price': price, 'Amount': amonut}
    
    def return_dict_corte(self,product,price):
        return {'Product': product, 'Price': price }
    
    def return_dict_cort(self,):
        pass