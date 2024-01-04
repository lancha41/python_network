# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Пример итогового словаря, который должна возвращать функция (перевод строки
после каждого элемента сделан для удобства чтения):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}
def generate_trunk_config(intf_vlan_mapping, trunk_template):
    trunk_list=[]
    trunk_dict={}
    trunk_dict_new={}
    for int in intf_vlan_mapping:
        trunk_dict[f'{int}']=None
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                vlan_list=intf_vlan_mapping[int]
                vlan_list = [str(n) for n in vlan_list]
                trunk_list.append(f"{command} {','.join(vlan_list)}")
            else:
                trunk_list.append(command)

    for i in trunk_dict:
        if i.startswith('Fast'):
            trunk_dict_new[i]=trunk_list[0:3]
            trunk_list=trunk_list[3:]
    return trunk_dict_new
print(generate_trunk_config(trunk_config,trunk_mode_template))
