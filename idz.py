# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


def summ(*args):
    if args:
        summa = 0
        args = reversed(args)
        for argument in args:
            if argument > 0:
                summa += argument
            else:
                break
        return summa
    else:
        return None


if __name__ == "__main__":
    arguments = list(map(float, input('Введите числа: ').split()))
    print('Сумма чисел после последнего отрицательного: ', summ(*arguments))