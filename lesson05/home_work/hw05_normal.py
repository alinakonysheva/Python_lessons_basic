# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
import hw05_easy

def main_menu():
    temp = -1
    while temp != 0:
        print("Введите 1, если Вам нужно перейти в другую папку")
        print("Введите 2, если Вам нужно порсмотреть содержимое текущей папки")
        print("Введите 3, если Вам нужно удалить папку")
        print("Введите 4, если Вам нужно создать папку")
        print("Введите 0, если Вам все надоело")

        temp = int(input("Что желаете?      "))

        if temp == 1:
        # Осуществляем переход в папку, в два действия: покажем директории,
        # затем покажем, что лежит в выбранной директории
            hw05_easy.show_all_dirs()
            name1 = input("в какую папку Вы желаете перейти?    ")
            path = os.path.join(os.getcwd(), name1)
            try:
                dirs = os.listdir(path)
                print(dirs)
                print('Успешно перешли!')
            except NotADirectoryError:
                print('Такого имени папки не существует, перейти невозможно')

        elif temp == 2:
            hw05_easy.show_all_dirs()


        elif temp == 3:
            # Удалить папку
            name_dir = str(input('Какую папку Вы желаете удалить?     '))
            dir_path = os.path.join(os.getcwd(), name_dir)
            hw05_easy.delete_one_dir(dir_path)

        elif temp == 4:
            name_dir = str(input('Как желаете назвать новую папку?     '))
            dir_path = os.path.join(os.getcwd(), name_dir)
            hw05_easy.create_one_dir(dir_path)


        elif temp == 0:
            print("До свидания!")

            return

        else:
            print("Подумайте еще раз, пожалуйста")

main_menu()
