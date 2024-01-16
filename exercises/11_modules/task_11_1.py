# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    list_out=command_output.split('\n')
    try:
        while True:
            list_out.remove('')
    except ValueError:
        pass
    result=dict()
    for i in list_out:
        
        if not 'show' in i and (i.startswith('R') or i.startswith('SW')):
            cdp=i.split()
            string_cdp=[]
            local_device_list=[]
            local_device=list_out[0].replace('>show cdp neighbors', '')
            local_device_list.append(local_device)
            local_int=cdp[1]+cdp[2]
            local_device_list.append(local_int)
            hostname=cdp[0]
            port_id=cdp[-2]+cdp[-1]
            string_cdp.append(hostname)
            string_cdp.append(port_id)
            result[tuple(local_device_list)]=tuple(string_cdp)
    return result

if __name__ == "__main__":
    with open("sh_cdp_n_r3.txt") as f:
        print(parse_cdp_neighbors(f.read()))
