def sum_total():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_num = line.split()
            print(sum(map(int, my_num)))
    except ValueError:
        print('Неправильный ввод')

sum_total()