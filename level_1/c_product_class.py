"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""
from decimal import Decimal


class Product:
    def __init__(self, title: str, description: str, price: Decimal, weight: float) -> None:
        self.title = title
        self.description = description
        self.price = price
        self.weight = weight

    def __repr__(self):
        return f'Информация о продукте: {self.title}, {self.description}, {self.price} руб., {self.weight} кг.'


if __name__ == '__main__':
    apple = Product(
        title='apple',
        description='really delicious apple',
        price=Decimal(100.00),
        weight=0.2
    )

    print(apple)
