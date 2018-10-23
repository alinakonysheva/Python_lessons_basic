# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os


def create_one_dir(dir_path):
    # функция, которая создает одну папку

    try:
        os.mkdir(dir_path)
        print('Директория удачно создана!')
    except FileExistsError:
        print('Такая директория уже существует')
    return


# создаем девять директорий

a = 1
while a < 10:
    dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(a))

    create_one_dir(dir_path)

    a = a + 1


def delete_one_dir(dir_path):
    try:
        os.rmdir(dir_path)
        print('Директория удалена!')
    except FileNotFoundError:
        print('Такой директории не существует')
    return


# удаляем девять директорий

a = 1
while a < 10:
    dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(a))
    delete_one_dir(dir_path)
    a = a + 1

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
