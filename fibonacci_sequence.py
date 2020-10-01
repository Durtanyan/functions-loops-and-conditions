# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 21:23:08 2020

@author: lukin
"""

"""
Число первое:
	number_up_to

Число второе:
	number_after

Число временное:
	number_tmp

Число получаемое:
	summ_up_after = number_up_to + number_after	

Число конечное:
	number_finish
"""
#определяем начальные значения начального и конечного числа
#ОБРАТИТЕ ВНИМАНИЕ, что в начале цикла второе число меньше первого на единицу
number_up_to,number_after = 1, 0

#начальное значение суммы
summ_up_after = 0

#число финиша цикла
number_finish = int(input("Введите число завершения цикла: "))

#основной цикл прерывать его будем по сумме двух чисел
while number_up_to + number_after < number_finish:
	#получаем сумму двух чисел
	summ_up_after = number_up_to + number_after
	#первое меняем на второе
	number_up_to = number_after
	#второе приравниваем к сумме
	number_after = summ_up_after
	#выводим сумму
	print(summ_up_after)
print("_______________________")
print("|   Способ функцией   |")
print("_______________________")
	
def fibonacci_sequence(number_up_to = 1, number_after = 0 ):
	number_finish = int(input("Введите число окончания цикла: "))
	summ_up_after = 0
	while number_up_to + number_after < number_finish:
		#получаем сумму двух чисел
		summ_up_after = number_up_to + number_after
		#первое меняем на второе
		number_up_to = number_after
		#второе приравниваем к сумме
		number_after = summ_up_after
		#выводим сумму
		print(summ_up_after)
	

fibonacci_sequence()	