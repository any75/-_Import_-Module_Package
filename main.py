# Разработать структуру программы «Бухгалтерия»:
# main.py;
# application/salary.py;
# application/db/people.py.
# Main.py — основной модуль для запуска программы.
# В модуле salary.py функция calculate_salary.
# В модуле people.py функция get_employees.
#
# Импортировать функции в модуль main.py и вызывать эти функции в конструкции.
# if __name__ == '__main__':
# Сами функции реализовывать не нужно. Достаточно добавить туда какой-либо вывод.
#
# Познакомиться с модулем datetime. При вызове функций модуля main.py выводить текущую дату.
#
# Найти интересный для себя пакет на pypi и в файле requirements.txt указать его с актуальной версией. При желании можно написать программу с этим пакетом.
#
# import application.salary
# import application.db.people
# if __name__ == '__main__':
#     application.salary.calculate_salary()
#     application.db.people.get_employees()

import datetime
print(datetime.datetime.now().strftime('%d.%m.%Y'))


