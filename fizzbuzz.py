# -*- coding: utf-8 -*-
"""
FizzBuzz

1. Imprima Fizz se o numero for multiplo de 3
2. Imprima Buzz se o numero for multiplo de 5
3. Imprima FizzBuzz se o numero for multiplo de 3 e 5
4. Caso não seja nem Fizz e nem Buzz imprima o próprio numero
"""


def fizz_buzz(param):
    if param % 3 == 0 and param % 5 == 0:
        param = 'fizzbuzz'

    elif param % 3 == 0:
        param = 'fizz'

    elif param % 5 == 0:
        param = 'buzz'

    return param


if __name__ == '__main__':
    assert fizz_buzz(1) == 1
    assert fizz_buzz(2) == 2
    assert fizz_buzz(4) == 4

    assert fizz_buzz(3) == 'fizz'
    assert fizz_buzz(6) == 'fizz'
    assert fizz_buzz(9) == 'fizz'

    assert fizz_buzz(5) == 'buzz'
    assert fizz_buzz(10) == 'buzz'
    assert fizz_buzz(20) == 'buzz'

    assert fizz_buzz(15) == 'fizzbuzz'
    assert fizz_buzz(45) == 'fizzbuzz'
    assert fizz_buzz(75) == 'fizzbuzz'
