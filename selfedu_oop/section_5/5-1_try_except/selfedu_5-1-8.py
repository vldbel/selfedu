"""Подвиг 8. В программе вводятся в одну строчку через пробел некоторые данные"""

def convert_to_num(x):
    try:
        return int(x)
    except ValueError:
        ...
    try:
        return float(x)
    except ValueError:
        return x

inp = "1 -5.6 True abc 0 23.56 hello"

# lst_in = input().split()
lst_in = inp.split()

lst_out = list(map(convert_to_num, lst_in))

print(lst_out)
