#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Дано слово. Проверить, является ли оно палиндромом.
if __name__ == '__main__':
    x = input("Введите слово: ")
    rev = ''.join(reversed(x))
    if x == rev:
        print("это палиндром")
    else:
        print("это не палиндром")
