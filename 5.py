small_bottles = int(input('How mach bottles < 1 litr'))
big_bottles = int(input('How mach bottles > 1 litr'))
money_for_bottles = (small_bottles * 0.1) + (big_bottles * 0.25)
print(f'Cash is {money_for_bottles:.2f}$')
