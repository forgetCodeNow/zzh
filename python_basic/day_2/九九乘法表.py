for num1 in range(1, 10):
    for num2 in range(1, num1 + 1):
        print(f'{num2} * {num1} = {num1 * num2}', end='\t')
    print()
