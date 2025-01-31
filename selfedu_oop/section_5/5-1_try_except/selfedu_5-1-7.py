"""Подвиг 7. В программе вводятся в одну строчку через пробел некоторые данные"""

inp = "1 -5.6 2 abc 0 False 22.5 hello world 7"

# lst_in = input().split()
lst_in = inp.split()

accum = 0
for item in lst_in:
    try:
         accum += int(item)
    except ValueError:
         next
print(accum)
    