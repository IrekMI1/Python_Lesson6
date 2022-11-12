# Задача 1
# Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками 
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух 
# целочисленных разрядов. Сформировать из обработанного списка строку:

def GetString(some_list):
    list_string = ''
    for item in some_list:
        if item.isdigit():
            if len(item) == 1: list_string += f'"0{item}" '
            else: list_string += f'"{item}" '
        elif '-' in item or '+' in item:
            if len(item) == 2: list_string += f'"{item[0]}' + f'0{item[1]}" '
            else: list_string += f'"{item}" '
        else: list_string += f'{item} '
    return list_string


def GetTreatedList(some_list):
    i = 0
    while i < len(some_list):
        if some_list[i].isdigit():
            if len(some_list[i]) == 1: 
                some_list[i] = f'0{some_list[i]}'
            some_list.insert(i, '"')
            some_list.insert(i + 2, '"')
            i += 3
        elif some_list[i][0] in '+-':
            if len(some_list[i]) == 2:
                some_list[i] = f'{some_list[i][0]}' + f'0{some_list[i][1]}'
            some_list.insert(i, '"')
            some_list.insert(i + 2, '"')
            i += 3
        else: i += 1


input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
string_list = GetString(input_list)
print("Исходный список: \t", input_list)
GetTreatedList(input_list)
print("Обработанный список: \t", input_list)
print("Вывод в строку: \t", string_list)