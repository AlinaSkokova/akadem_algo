import time
import tracemalloc

def calc_fib(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = calc_fib(n-1, computed) + calc_fib(n-2, computed)
    return computed[n]
    

if __name__ == '__main__':
    try:
        tracemalloc.start()
        t_start = time.perf_counter()
        with open('input.txt') as f:
            n_str = f.read()
        n = int(n_str)
        if (n >= 0) and (n <= 45):
            with open('output.txt', 'w') as f:
                f.write(f'{calc_fib(n)}')
            print(f'Время работы: {time.perf_counter() - t_start} сек.')
            size, peak = tracemalloc.get_traced_memory()
            print(f'Текущие и пиковые затраты памяти: {size} и {peak} байт')
        else:
            print('Введены числа вне интервала [0, 45]')
    except ValueError:
        print('Число введено неверно')