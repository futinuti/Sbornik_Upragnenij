width = float(input("Input width of homestead, m "))
length = float(input("Input length of homestead, m "))
akr_to_metr = 4046.86
square = (width * length) / akr_to_metr
print(f'Square of homestead equal {square:.5f} acres')
