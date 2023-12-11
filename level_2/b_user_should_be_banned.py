"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']


class User:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def should_be_banned(self, banned_surname_list: list[str]) -> bool:
        return self.surname in banned_surname_list

    def __repr__(self) -> str:
        return f'name: {self.name}, surname: {self.surname}, age: {self.age}'


if __name__ == '__main__':
    user = User(name='John', surname='Wilhelm', age=30)
    assert user.should_be_banned(banned_surname_list=SURNAMES_TO_BAN) == True
