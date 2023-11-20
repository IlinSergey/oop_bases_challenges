"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income

    def decrease_balance(self, cost: float):
        if self.balance >= cost:
            self.balance -= cost
        else:
            raise ValueError('Low ballance!')


if __name__ == '__main__':
    bill = BankAccount(
        owner_full_name='Ilin Sergey',
        balance=10_000.00
    )
    print(bill.balance)
    bill.decrease_balance(cost=5_000.00)
    print(bill.balance)
    try:
        bill.decrease_balance(cost=15_000.00)
    except ValueError as error:
        print(error)
