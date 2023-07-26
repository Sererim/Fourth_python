# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем используйте его строковое представление.
def pack(**kwargs) -> dict:
    d = {}
    for x,y in kwargs.items():
        try:
            hash(x)
            d[y] = x
        except TypeError:
            d[repr(y)] = x
    return d


if __name__ == "__main__":
    print(pack(h=10, lst=[0, 1, 2], s={1, 2, 3, 3}, word="Hello, world!",
               f=0.1, d_dict={1: 2}, yes=True))
