a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
if a<b:
    print(a, " - это число наименьшее из двух данных")
elif a>b:
    print(b, " - это число наименьшее из двух данных")
elif a==b:
    print(a or b, " - числа одинаковы")
