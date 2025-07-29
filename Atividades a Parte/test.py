# LANCHONETE
# e saida de vendas
# login sempre bom
# requer pedido e preco

from pathlib import Path
import openpyxl
import os

ROOT = Path(__file__).parent
EXCEL_FILE = ROOT / 'products.xlsx'

xl = openpyxl.load_workbook(EXCEL_FILE)
sheet = xl['Sheet']


class Order:
    # SETAR PEDIDO E PREÇO
    def __init__(self, order: str, price: float) -> None:
        self._order = order
        self._price = price

    # Para criar dicionario automaticamente @matheus

    def _generateDict(self, order: str, qtd: int, price: float) -> dict:
        return {'order': order, 'qtd': qtd, 'price': price}

    @property
    def getOrder(self) -> str:
        return self._order

    @getOrder.setter
    def getOrder(self, item: str):
        self._order = item

    @property
    def getPrice(self) -> float:
        return self._price

    @getPrice.setter
    def getPrice(self, item: float):
        self._price = item

    # aqui fica os o funcionamentos onde vamos registrar a venda de um produto

    def registerOrder(self, product, qtd, price):
        _orderInfo = []  # <-- Registrar pedidos nessa lista

        dict_ = self._generateDict(product, qtd, price)
        _orderInfo.append(dict_)

        # traduzindo: colocando os pedidos vendidos no Excel
        # Registrar
        # no excel

    def insertOrderInExcel(self, prod, quantity, price):

        counter = 0
        for i in sheet.iter_rows(min_row=2):
            product = i[0]
            qtd = i[1]
            price_ = i[2]

            # Aqui a gente pode colocar um sistema pra ver o quanto vendeu e
            #  outras estatisticas

    def ViewInfo(self):

        # 1 - abrir a planilha
        # 2 - selecionar o nome da sheet
        # 3 - pegar a sheet e os dados dela
        # 4 - perguntar qual produto ele quer ver as informações
        # 5 - revelar para o usuario a quantidade de {produto} que vendeu e receita

        pass


orderInput = input('O que foi vendido: ')
priceInput = float(input('Qual o preço: '))

order = Order(order=orderInput, price=priceInput)

# (uwu)
