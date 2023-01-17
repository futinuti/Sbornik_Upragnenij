cash = int(input('Введите сдачу в центах'))

print(f'Монеты по 2$ {cash // 200} штук')
cash = cash % 200
print(f'Монеты по 1$ {cash // 100} штук')
cash = cash % 100
print(f'Монеты по 0.25$ {cash // 25} штук')
cash = cash % 25
print(f'Монеты по 0.10$ {cash // 10} штук')
cash = cash % 10
print(f'Монеты по 0.05$ {cash // 5} штук')
cash = cash % 5
print(f'Монеты по 0.01$ {cash} штук')
