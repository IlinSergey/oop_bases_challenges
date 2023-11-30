""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""


class User:

    def __init__(self, user_id: int, username: str, name: str) -> None:
        self.user_id = user_id
        self.username = username
        self.name = name

    def make_username_capitalized(self) -> str:
        return self.username.capitalize()

    def generate_short_user_description(self) -> str:
        return f'User with id {self.user_id} has {self.username} username and {self.name} name'

    def __repr__(self) -> str:
        return f'user_id: {self.user_id}, user_name: {self.username}, name: {self.name}'


if __name__ == '__main__':
    user = User(user_id=1, username='Serg', name='Sergey')
    print(user)
    print(user.generate_short_user_description())
    print(user.make_username_capitalized())
