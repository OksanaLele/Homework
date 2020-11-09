from random import randint
numbers = []
for i in range(10):
    numbers.append(randint(1, 100))
print(numbers)
result_list = [
    val for idx, val in enumerate(numbers)
    if idx > 0 and numbers[idx - 1] < val
]
print(result_list)
