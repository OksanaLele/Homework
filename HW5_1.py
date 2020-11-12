my_file= open('text.txt', 'w')
line = input('Введите текст \n')
my_file.writelines(line)
my_file.close()
