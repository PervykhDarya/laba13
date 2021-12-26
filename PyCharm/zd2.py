# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def sr_garmonic(*args):
    if args:
        summa = float(0)
        for arg in args:
            summa = summa + (1 / arg)
        n = len(args)
        return n / summa
    else:
        return None

if __name__ == "__main__":
    arguments = list(map(int, input('Введите аргументы: ').split()))
    print('Среднее гармоническое значение аргументов: ', sr_garmonic(*arguments))