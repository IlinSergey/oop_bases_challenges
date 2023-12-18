"""

Задания:
    1. Создайте класс Developer, который будет наследоваться от класса ItDepartmentEmployee и класса SuperAdminMixin.
    2. Переопределите у класса Developer метод __init__ таким образом, чтобы он на вход принимал еще и язык программирования.
    3. Переопределите метод get_info у класса Developer таким образом, чтобы там выводился еще и язык программирования.
    4. Вызовите у экземпляра класса Developer все возможные методы.
"""


class Employee:
    def __init__(self, name: str, surname: str, age: int, salary: float) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_info(self) -> str:
        return f'{self.name} with salary {self.salary}'


class ItDepartmentEmployee(Employee):
    def __init__(self, name: str, surname: str, age: int, salary: float) -> None:
        super().__init__(name, surname, age, salary)
        self.salary *= 2


class AdminMixin:
    def increase_salary(self, employee: Employee, amount: float) -> None:
        employee.salary += amount


class SuperAdminMixin(AdminMixin):
    def decrease_salary(self, employee: Employee, amount: float) -> None:
        employee.salary -= amount


class Developer(SuperAdminMixin, ItDepartmentEmployee):
    def __init__(self, name: str, surname: str, age: int, salary: float, programming_language: str) -> None:
        super().__init__(name, surname, age, salary)
        self.programming_language = programming_language

    def get_info(self) -> str:
        return f'{super().get_info()}, programming language: {self.programming_language}'


if __name__ == '__main__':
    python_developer = Developer(
        name='Sergey',
        surname='Ilin',
        age=33,
        salary=80_000.00,
        programming_language='Python'
    )
    assert python_developer.get_info() == 'Sergey with salary 160000.0, programming language: Python'
    python_developer.increase_salary(employee=python_developer, amount=20_000.0)
    assert python_developer.get_info() == 'Sergey with salary 180000.0, programming language: Python'
    python_developer.decrease_salary(employee=python_developer, amount=80_000.00)
    assert python_developer.get_info() == 'Sergey with salary 100000.0, programming language: Python'
