def div(*args):
    try:
        arg1 = int(input("ВВедите 1 число "))
        arg2 = int(input("ВВедите 2 число "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Ошибка:на ноль делить нельзя"

    return res
print(f'Результат  {div()}')