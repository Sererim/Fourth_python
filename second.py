# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем используйте его строковое представление.
import inspect


def pack(key) -> dict:
    call = inspect.currentframe().f_back.f_locals.items()
    try:
        return {key.__hash__(): name for name, value in call if value is key}
    except TypeError:
        return {key.__repr__(): name for name, value in call if value is key}


if __name__ == "__main__":
    h = 0
    print(pack(h))
    l = (0, 0)
    print(pack(l))
    s = set(l)
    print(pack(s))
