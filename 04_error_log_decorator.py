# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

def log_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Открываем файл лога в режиме 'a' для добавления записей
            with open('function_errors.log', 'a') as log_file:
                # Получаем имя функции
                function_name = func.__name__
                # Получаем параметры вызова
                args_str = ', '.join([repr(arg) for arg in args] + [f'{key}={repr(value)}' for key, value in kwargs.items()])
                # Получаем тип и текст ошибки
                error_type = type(e).__name__
                error_text = str(e)
                # Формируем строку для записи в лог
                log_entry = f'{function_name} {args_str} {error_type} {error_text}\n'
                # Записываем строку в лог файл
                log_file.write(log_entry)
            # Пробрасываем ошибку дальше
            raise e
    return wrapper

# Проверить работу на следующих функциях
@log_errors
def perky(param):
    return param / 0


@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')



# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
def log_errors(log_file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Открываем файл лога в режиме 'a' для добавления записей
                with open(log_file_name, 'a') as log_file:
                    # Получаем имя функции
                    function_name = func.__name__
                    # Получаем параметры вызова
                    args_str = ', '.join([repr(arg) for arg in args] + [f'{key}={repr(value)}' for key, value in kwargs.items()])
                    # Получаем тип и текст ошибки
                    error_type = type(e).__name__
                    error_text = str(e)
                    # Формируем строку для записи в лог
                    log_entry = f'{function_name} {args_str} {error_type} {error_text}\n'
                    # Записываем строку в лог файл
                    log_file.write(log_entry)
                # Пробрасываем ошибку дальше
                raise e
        return wrapper
    return decorator


@log_errors('function_errors.log')
def perky(param):
    return param / 0

perky(param=42)

@log_errors('function_errors.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')

