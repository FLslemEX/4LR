#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Вывести все имеющиеся в нем буквосочетания нн.
if __name__ == '__main__':
    x = input("Введите предложение: ")
    s = len(x)
    for i in range(s):
         x = x.replace("нн",' ')
    print(x)
