# -*- coding: utf-8 -*-
"""
FizzBuzz

1. Imprima Fizz se o numero for multiplo de 3
2. Imprima Buzz se o numero for multiplo de 5
3. Imprima FizzBuzz se o numero for multiplo de 3 e 5
"""


def fizz_buzz(param):
    if param == (1, 2):
        return param

    if param == 3:
        return 'fizz'


if __name__ == '__main__':
    assert fizz_buzz(1) == 1
    assert fizz_buzz(2) == 2
    assert fizz_buzz(3) == 'fizz'
