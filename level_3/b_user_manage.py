"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames: list[str] = []

    def add_user(self, username: str) -> None:
        self.usernames.append(username)

    def get_users(self) -> list[str]:
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str) -> None | str:
        try:
            self.usernames.remove(username)
        except ValueError:
            return 'Такого пользователя не существует.'


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        self.usernames.clear()


if __name__ == '__main__':

    user_maneger = UserManager()
    assert user_maneger.usernames == []
    user_maneger.add_user(username='Bob')
    assert 'Bob' in user_maneger.usernames
    user_maneger.get_users() == ['Bob',]

    admin_manager = AdminManager()
    assert admin_manager.usernames == []
    admin_manager.add_user(username='Jimmy')
    assert 'Jimmy' in admin_manager.usernames
    assert admin_manager.get_users() == ['Jimmy',]
    admin_manager.add_user(username='Billi')
    admin_manager.ban_username(username='Jimmy')
    admin_manager.ban_username('Gary') == 'Такого пользователя не существует.'
    assert 'Jimmy' not in admin_manager.usernames
    assert admin_manager.get_users() == ['Billi',]

    super_admin_manager = SuperAdminManager()
    super_admin_manager.add_user('Patrik')
    super_admin_manager.add_user('Gary')
    assert super_admin_manager.get_users() == ['Patrik', 'Gary',]
    super_admin_manager.add_user('Sandy')
    super_admin_manager.ban_username('Gary')
    super_admin_manager.ban_username('Jimmi') == 'Такого пользователя не существует.'
    assert super_admin_manager.get_users() == ['Patrik', 'Sandy',]
    super_admin_manager.ban_all_users()
    assert super_admin_manager.usernames == []


