"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""
import sys
from enum import Enum
from io import StringIO


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self) -> str:
        return f'Product {self.title} with price {self.price}'


class PrintLoggerMixin():
    def log(self, log_message: str) -> None:
        print(log_message)  # noqa: T201


class PremiumProduct(PrintLoggerMixin, Product):
    def increase_price(self):
        self.price *= 1.2
        self.log(f'Premium product new price: {self.price}')

    def get_info(self) -> str:
        base_info = super().get_info()
        self.log(f'get info from Premium product with: {base_info}')
        return f'{base_info} (Premium)'


class DiscountedProduct(PrintLoggerMixin, Product):
    def decrease_price(self) -> None:
        self.log(f'Discounted product new price: {self.price}')
        self.price /= 1.2

    def get_info(self) -> str:
        base_info = super().get_info()
        self.log(f'get info from Discounted product with: {base_info}')
        return f'{base_info} (Discounted)'


if __name__ == '__main__':

    class Methods(Enum):
        get_info = 'get_info'
        increase_price = 'increase_price'
        decrease_price = 'decrease_price'

    def get_output_from_method(product: PremiumProduct | DiscountedProduct,
                               method: Methods) -> str:
        captured_output = StringIO()
        sys.stdout = captured_output

        match method:
            case Methods.get_info:
                product.get_info()
            case Methods.increase_price:
                product.increase_price()
            case Methods.decrease_price:
                product.decrease_price()

        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

    premium_product = PremiumProduct(title='Ikra', price=1000.00)
    discounted_product = DiscountedProduct(title='Grechka', price=10.00)

    assert get_output_from_method(premium_product,
                                  Methods.get_info) == 'get info from Premium product with: Product Ikra with price 1000.0'
    assert get_output_from_method(discounted_product,
                                  Methods.get_info) == 'get info from Discounted product with: Product Grechka with price 10.0'
    assert get_output_from_method(premium_product,
                                  Methods.increase_price) == 'Premium product new price: 1200.0'
    assert get_output_from_method(discounted_product,
                                  Methods.decrease_price) == 'Discounted product new price: 10.0'
