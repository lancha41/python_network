# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

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
        elif 'duplex' in i:
            access_dict[clear_list[int(clear_list.index(i)-1)]]=int(1)
            clear_list.remove(i)
    return access_dict,trunk_dict
get_int_vlan_map('config_sw1.txt')
