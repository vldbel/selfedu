try:
    x, y = map(int, input().split())
    res = x / y
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print('everything went fine')
finally:
    print('finally')