import time
import tracemalloc

def fib_lastDigit(n):
    if n < 2:
        return n
    prev = 0
    curr = 1
    for _ in range(n - 1):
        fib = (curr + prev) % 10
        prev = curr
        curr = fib
    return curr
    
if __name__ == '__main__':
    try:
        tracemalloc.start()
        t_start = time.perf_counter()
        with open('input.txt') as f:
            n_str = f.read()
        n = int(n_str)
        if (n >= 0) and (n <= (10 ** 7)):
            with open('output.txt', 'w') as f:
                f.write(f'{fib_lastDigit(n)}')
            print(f'Время работы: {time.perf_counter() - t_start} сек.')
            size, peak = tracemalloc.get_traced_memory()
            print(f'Текущие и пиковые затраты памяти: {size/(1024*1024)} и {peak/(1024*1024)} мб')
        else:
            print('Введены числа вне интервала [0, 10^7]')
    except ValueError:
        print('Число введено неверно')