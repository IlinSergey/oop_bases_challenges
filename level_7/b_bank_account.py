"""
Банк позволяет уходить в минус по счету, чтобы клиенты не оказывались в без денег в самый неподходящий момент

Задания:
    1. Напишите логику метода decrease_balance таким образом, чтобы можно было уменьшать баланс, но чтобы он не становился
       меньше чем значение в атрибуте класса min_balance. Если он будет меньше - вызывайте исключение ValueError
    2. Создайте экземпляр класса BankAccount, вызовите у него метод decrease_balance и убедитесь, что баланс уменьшается
       и если он уменьшается больше чем можно, то вызывается исключение

"""
import unittest


class BankAccount:
    min_balance = -100

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def decrease_balance(self, amount: float):
        if amount < 0:
            raise ValueError('Amount should be a non negative.')
        new_balance = self.balance - amount
        if new_balance >= self.min_balance:
            self.balance = new_balance
        else:
            raise ValueError('Balance limit exceeded.')

    def __repr__(self) -> str:
        return f"{self.owner}'s balance: {self.balance}"


if __name__ == '__main__':

    class TestBancAccount(unittest.TestCase):

        def setUp(self) -> None:
            self.account = BankAccount(owner='Bob', balance=100.00)

        def test_decrease_balance_succesful(self):
            current_balance = self.account.balance
            amount_to_decrease = 80.0
            expected_result = current_balance - amount_to_decrease
            self.account.decrease_balance(amount_to_decrease)
            self.assertEqual(self.account.balance, expected_result)

        def test_decrease_balance_raises_value_error_with_negative_amount(self):
            self.assertRaises(ValueError, self.account.decrease_balance, -20.0)

        def test_decrease_balance_raises_value_error_with_limit_exceeded(self):
            self.assertRaises(ValueError, self.account.decrease_balance, -120.0)

    unittest.main()
