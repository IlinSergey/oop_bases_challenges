"""
Мы используем константу EBAY_TITLE только в классе EbayProduct и хочется чтобы она жила в классе, а не где-то отдельно

Задания:
    1. Сделайте так, чтобы тайтл ебэя жил в классе
    2. Создайте экземпляр класса EbayProduct, вызовите у него метод get_product_info и убедитесь, что метод отдает
       то что вы ожидаете.
"""


class EbayProduct:
    _ebay_title = 'eBay'

    @property   # property для защиты атрибута от изменения
    def ebay_title(self):
        return self._ebay_title

    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_product_info(self):
        return f'Product {self.title} with price {self.price} from {self.ebay_title} marketplace'

    def __call__(self):
        return self.get_product_info()


if __name__ == '__main__':
    ebay_product = EbayProduct(title='Book', price=10.0)
    assert ebay_product() == 'Product Book with price 10.0 from eBay marketplace'
