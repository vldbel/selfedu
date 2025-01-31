"""Подвиг 3. Объявите функцию с сигнатурой:"""

def input_int_numbers():
    try:
        return tuple(map(int, input().split()))
    except TypeError:
        raise ValueError('все числа должны быть целыми')

while True:
    try:
        res= input_int_numbers()
    except ValueError:
        continue
    else:
        if res:
            break

print(' '.join(map(str, res)))