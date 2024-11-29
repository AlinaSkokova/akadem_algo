def sum_fromFile(filepath):
    restr1 = -10**9
    restr2 = 10**9
    with open(filepath) as f:
        nums_input = f.read()
    nums_list = nums_input.split(' ')
    try:
        a = int(nums_list[0])
        b = int(nums_list[1])
        if (a >= restr1) and (a <= restr2) and (b >= restr1) and (b <= restr2):
            with open('output.txt', 'w') as f:
                f.write(f'{a + b}')
        else:
            print('Введены числа вне интервала [−10^9, 10^9]')
    except ValueError:
        print('Числа введены неверно')

if __name__ == '__main__':
    sum_fromFile('input.txt')