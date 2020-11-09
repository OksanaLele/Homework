def fact(num: int):
    result = 1
    for el in range(1, num + 1):
        result *= el
        yield result


N = 5
for x in fact(N):
    print(x)
