"""Подвиг 7. В практике программирования блок else используют как элемент отладки программы"""

def get_loss(w1, w2, w3, w4):
    try:
        y = w1 // w2
    except ZeroDivisionError as e:
        return "деление на ноль"
    else:
        y = y * 10 - 5 * w2 * w3 + w4
        return y 