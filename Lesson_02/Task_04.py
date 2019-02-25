__author__ = "Павел Новиков (aka VokiVon)"
"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
n = int(input("Введите натуральное число n ( целое больше 0): "))

i = 0
out_sum = 0
DIVIDER = -2
# первоначальная инициализация для получения первого члена последовательности = 1
tmp = DIVIDER
while i < n:
    tmp /= DIVIDER
    out_sum += tmp
    i += 1

print(f"Сумма {n} элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ... = {out_sum}")
