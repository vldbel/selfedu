"""Подвиг 4. В программе вводятся два значения в одну строчку через пробел."""

x, y = input().split()
res = str(x) + str(y)
try:
    res = float(x) + float(y)
except ValueError:
    pass
try:
    res = int(x) + int(y)
except ValueError:
    pass
finally: 
    print(res)