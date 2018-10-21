# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def create_dirs():
# функция, которая создает девять папок с именем dir_n
    a = 1
    while a < 10:
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(a))
        a = a + 1
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print('Такая директория уже существует')

    return

# функция, которая удаляет девять папок с именем dir_n
def delete_dirs():
    a = 1
    while a < 10:
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(a))
        try:
            os.rmdir(dir_path)
        except FileExistsError:
            print('Такая директория уже не существует')
        a = a + 1

    return


create_dirs()
delete_dirs()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os


def show_all_dirs():
# вызов: отображает папки текущей директории
    path = os.path.join(os.getcwd())
    dirs = os.listdir(path)
    print(dirs)


show_all_dirs()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys
import shutil

def copy_this_file():
    shutil.copyfile(sys.argv[0], sys.argv[0]+'.copy')
    return

copy_this_file()
