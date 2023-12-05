"""
У нас есть правило, по которому никто не может изменить емэил админа. Но у меня это получилось, и я даже не получаю ошибки.

Задания:
    1. Запустите текущий код и убедитесь, что мы можем изменить емэил админа без проблем.
    2. Найдите причину этой досадной оплошности и исправьте. Код в методах менять нельзя
    3. Снова запустите код и убедитесь, что при попытке сменить емэил у админа вы видите ошибку
"""


class User:

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def change_email(self, new_email: str) -> None:
        self.email = new_email


class AdminUserMixin:

    def change_email(self, new_email: str) -> SystemError:
        raise SystemError('It is impossible to change the email address of the administrator')


class AdminUser(AdminUserMixin, User):  # type: ignore [misc]

    def change_user_info(self, user: User, new_username: str, new_email: str) -> None:
        user.username = new_username
        user.email = new_email


if __name__ == '__main__':
    admin_user = AdminUser(username='python_dev', email='learnpython@yandex.ru')
    admin_user.change_email('new_email@gmail.com')
    print(admin_user.email)  # noqa: T201
