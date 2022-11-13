# Создать список, содержащий цены на товары (10–20 товаров) например: 
# [57.8, 46.51, 97, ...] Вывести на экран эти цены через запятую в одну строку, 
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). 
# Вывести цены, отсортированные по возрастанию, новый список не создавать 
# (доказать, что объект списка после сортировки остался тот же). 
# Создать новый список, содержащий те же цены, но отсортированные по убыванию. 
# Вывести цены пяти самых дорогих товаров.

from random import uniform
from math import log10

def GetStringPrices(prices_list):
    result = ''
    for price in prices_list:
        fraction = round((price - int(price)) * 100)
        if log10(fraction) < 1: 
            fraction = f'0{fraction}'
        result += f'{int(price)} руб {fraction} коп, '
    return result


def ListSort(some_list):
    for i in range(len(some_list)):
        min_idx = i
        for j in range(i + 1, len(some_list)):
            if some_list[j] < some_list[min_idx]: 
                min_idx = j
        temp = some_list[i]
        some_list[i] = some_list[min_idx]
        some_list[min_idx] = temp


def GetReversedSortedList(some_list):
    result_list = some_list.copy()
    for i in range(len(result_list) - 1):
        for j in range(len(result_list) - 1):
            if result_list[j] < result_list[j + 1]:
                temp = result_list[j]
                result_list[j] = result_list[j + 1]
                result_list[j + 1] = temp
    return result_list


prices = []
for _ in range(10):
    prices.append(round(uniform(0, 100), 2)) 

print('Исходный список:          \t', prices)
print('Цены в виде строки:      \t', GetStringPrices(prices))
reverse_list = GetReversedSortedList(prices)
ListSort(prices)
print('Сортированный по убыванию:  \t', reverse_list)
print('Сортированный по возрастанию: \t', prices)
print('Цены 5-ти самых дорогих: \t', reverse_list[0:4])