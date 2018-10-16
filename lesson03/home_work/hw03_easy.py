# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    """
    Возвращает число, округленное до указанного количества знаков после запятой.
    """

    result = number
    power = 10 ** ndigits
    n = result * power

    if n - int(n) >= 0.5:

        result = (int(n) + 1) / power

    else:
        result = int(n) / power

    return result

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    """
    Возвращает true для счастливого билета. Билет считается счастливым если
     количество цифр на нем равно шести и сумма его первых и последних цифр равны.
    """

    a = str(ticket_number)
    return len(a) == 6 and (int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]))

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
