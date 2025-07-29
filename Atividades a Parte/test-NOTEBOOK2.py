'''
import dotenv
import pymysql
import os
import pymysql.connections
import pymysql.cursors
dotenv.load_dotenv()

TABLE_NAME = 'Products'


def env(string: str):
    return os.environ[string]


def createDatabase():
    connection = pymysql.connect(
        host=env('MYSQL_HOST'),
        user=env('MYSQL_USER'),
        password=env('MYSQL_PASSWORD'),
        database=env('MYSQL_DATABASE'),
        cursorclass=pymysql.cursors.DictCursor,
    )

    with connection:
        with connection.cursor() as cursor:

            sql = (
                f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( '
                'id INT NOT NULL AUTO_INCREMENT, '
                'name VARCHAR(50) NOT NULL, '
                'qtd FLOAT NOT NULL, '
                'PRIMARY KEY (id)'
                ') '
            )

            cursor.execute(sql)
        connection.commit()


def insertIntoDB():
    pass


class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Management:
    def __init__(self):
        self._products = []

    def _autoDict(self, product, qtd, price):
        return {'product': product, 'qtd': qtd, 'price': price}

    def add_product(self, product: Product, qtd: int, price: float):
        dict_ = self._autoDict(product, qtd, price)
        self._products.append(dict_)
        return

    def list_products(self):
        self._products
        return

    def update_products(self, nome: str,
                        novo_preco: float = None,  # type: ignore
                        nova_quantidade: int = None):  # type: ignore
        for i in self._products:
            if nome == i['product']:
                i['price'] = novo_preco

        return

    def remove_product(self, name: str):
        self._products.remove(name)
        return

    def search_product(self, nome: str):
        return

    def calculate_total_stock(self):
        for value in self._products:
            total = value['price'] * value['qtd']
            print(total)
        return

    def verify_product(self, nome: str):

        return

    def apply_offer(self, nome: str, percentual: float):
        return

    def sort_products_by_price(self, crescente: bool = True):
        return

    def generate_report(self):
        pass
'''
