"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float) -> None:
        self.balance += amount

    def decrease_balance(self, amount: float) -> None:
        self.balance -= amount


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self) -> bool:
        return self.balance > 1000


if __name__ == '__main__':

    bank_account = BankAccount(owner_full_name='Spongebob Squarepants',
                               balance=500.00)
    credit_account = CreditAccount(owner_full_name='Mr. Krabs',
                                   balance=10_000.00)

    assert bank_account.balance == 500.00
    bank_account.increase_balance(amount=500.00)
    assert bank_account.balance == 1_000.00
    bank_account.decrease_balance(amount=400.00)
    assert bank_account.balance == 600.00

    assert credit_account.balance == 10_000.00
    credit_account.increase_balance(amount=500.00)
    assert credit_account.balance == 10_500.00
    assert credit_account.is_eligible_for_credit() is True
    credit_account.decrease_balance(amount=10_400.00)
    assert credit_account.balance == 100.00
    assert credit_account.is_eligible_for_credit() is False
