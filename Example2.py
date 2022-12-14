# Дан список, содержащий искажённые данные с должностями и именами сотрудников.
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 
# 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, 
# как привести их к корректному виду. Можно ли при этом не создавать новый список?

employee_list = [
    'инженер-конструктор Игорь',
    'главный бухгалтер МАРИНА', 
    'токарь высшего разряда нИКОЛАй', 
    'директор аэлита'
]
for i in range(len(employee_list)):
    name = ''
    for j in range(len(employee_list[i]) - 1, -1, -1):
        if employee_list[i][j] != ' ':
            name += employee_list[i][j]
        else:
            name = ''.join(reversed(name)).capitalize()
            employee_list[i] = employee_list[i][0:j] + ' ' + name
            print(f'Привет, {name}')
            break

print(employee_list)