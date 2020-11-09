from functools import reduce
numbers = [item for item in range(100, 1001) if item % 2 == 0]
print(f'Список четных значений {[item for item in range(100, 1001) if item % 2 == 0]}')

def my_func(prev_el, el):
    return prev_el * el
print(reduce(my_func, numbers))