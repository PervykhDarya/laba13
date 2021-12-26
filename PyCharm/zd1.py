# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def sr_geom(*args):
    if args:
        summa = 0
        for arg in args:
            summa = summa + arg
        n = len(args)
        return summa / n
    else:
        return None

if __name__ == "__main__":
    arguments = list(map(int, input('Введите аргументы: ').split()))
    print('Среднее геометрическое значение аргументов: ', sr_geom(*arguments))