# Создайте программу, которая запрашивает у пользователя два целых чис-
# ла a и b, после чего выводит на экран результаты следующих математи-
# ческих операций:
#   сумма a и b;
#   разница между a и b;
#   произведение a и b;
#   частное от деления a на b;
#   остаток от деления a на b;
#   десятичный логарифм числа a;
#   результат возведения числа a в степень b.
# Подсказка. Функцию log10 вы найдете в модуле math.

from math import log10


a = int(input('Введите "a" '))
b = int(input('Введите "b" '))

print(f'сумма {a} и {b} = {a + b}')
print(f'разница между {a} и {b} = {a - b}')
print(f'произведение {a} и {b} = {a * b}')
print(f'частное от деления {a} на {b} = {a / b}')
print(f'остаток от деления {a} на {b} = {a % b}')
print(f'десятичный логарифм числа {a} = {log10(a)}')
print(f'результат возведения числа {a} в степень {b} = {a ** b}')
