"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone


if __name__ == '__main__':
    user = User(
        name='Sergey',
        username='Serg',
        age=33,
        phone='89992223322'
    )
    print(f'Информация о пользователе: {user.name}, {user.username}, {user.age}, {user.phone}.')
