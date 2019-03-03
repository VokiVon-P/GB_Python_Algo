__author__ = 'Павел Новиков (aka VokiVon)'
"""
Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив 
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), 
т.к. именно в этих позициях первого массива стоят четные числа.
"""
import generator

arr_ = generator.gen_array()
print(arr_)
even_arr = [i for i in range(len(arr_)) if not arr_[i] % 2]
print(f'Индексы четных элементов: {even_arr}')




