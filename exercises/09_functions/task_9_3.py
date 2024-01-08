# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    with open(config_filename,'r') as f:
        file = f.readlines()
    clear_list=[]
    access_dict={}
    trunk_dict={}
    trunk_vlan=[]
    for i in file:
        if 'FastEthernet' in i:
            clear_list.append(i[10:-1])
            clear_list.append(file[int(file.index(i)+2)])
    for i in clear_list:
        if 'access vlan' in i:
            access_dict[clear_list[int(clear_list.index(i)-1)]]=int(i.split()[-1])
            clear_list.remove(i)
        elif 'trunk allowed' in i:
            trunk_dict[clear_list[int(clear_list.index(i)-1)]]=trunk_vlan=[int(a) for a in i.split()[4].split(',')]
    result=(access_dict,trunk_dict,)
    return result
get_int_vlan_map('config_sw1.txt')
