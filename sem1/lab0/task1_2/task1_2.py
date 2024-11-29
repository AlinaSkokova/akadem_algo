def sq_sum_ab():
    k = 0
    restr1 = -10**9
    restr2 = 10**9
    while k != 1:
        nums_input = input('Введите два целых числа через пробел: ')
        nums_list = nums_input.split(' ')
        try:
            a = int(nums_list[0])
            b = int(nums_list[1])
            if (a >= restr1) and (a <= restr2) and (b >= restr1) and (b <= restr2):
                k = 1
            else:
                print('Введены числа вне интервала [−10^9, 10^9]')
        except ValueError:
            print('Числа введены неверно')
    print(f'{(a + b) ** 2}')

if __name__ == '__main__':
    sq_sum_ab()