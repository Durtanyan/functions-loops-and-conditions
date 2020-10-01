# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:30:31 2020

@author: lukin
"""
"""
Задача #2: FizzBuzz
Если число делится на 3, то нужно вывести Fizz,
если на 5, то Buzz, если на 3 и на 5, то FizzBuzz.

Задача - написать программу, 
которая выводит сумму чисел из диапазона от 1000 до 20000 включительно, 
которые делятся и на 3 и на 5.
"""
summ = 0
integer = 1000
print(integer)
while integer <= 20000:
    if integer % 3 == 0:
        print('Fizz')
        if integer % 5 == 0:
            print('Buzz')
            if (integer % 3 == 0 and integer % 5 == 0):
                print('FizzBuzz')
                summ += integer
    integer += 1
print(f'Сумма чисел из диапазона от 1000 до 20000 включительно равна: {summ}')

"""способ сприменением функции range()
"""
summ1 = 0
for num in range(1000, 20001):
    if num % 3 == 0:
        print('Fizz')
        if num % 5 == 0:
            print('Buzz')
            if num % 3 == 0 and num % 5 == 0:
                print('FizzBuzz')
                summ1 += num

print(summ1)

print(f'Сумма чисел из диапазона от 1000 до 20000 включительно равна: {summ1}')











