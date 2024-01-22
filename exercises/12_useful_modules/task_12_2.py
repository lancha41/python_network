# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
from task_12_1 import ping_ip_addresses
def convert_ranges_to_ip_list(list_ips):
   new_ips_list=[]
   for ip in list_ips:
    if not '-' in ip:
        new_ips_list.append(ip)
    elif '-' in ip:
        ip1=ip.split('-')[0]
        ip2=ip.split('-')[1]
        if not '.' in ip2:
            ip2_list=[]
            ip1_list=ip1.split('.')
            for i in ip1_list[:3]:
                ip2_list.append(i)
            ip2_list.append(ip2)
            ip2='.'.join(ip2_list)
            for i in range(int(ip1_list[-1]),int(ip2_list[-1]),1):
                clr_ip=ip1_list[:3]
                clr_ip.append(str(i))
                new_ips_list.append('.'.join(clr_ip))
            new_ips_list.append(ip2)
        else:
            ip1_list=ip1.split('.')
            ip2_list=ip2.split('.')
            for i in range(int(ip1_list[-1]),int(ip2_list[-1]),1):
                clr_ip=ip1_list[:3]
                clr_ip.append(str(i))
                new_ips_list.append('.'.join(clr_ip))
            new_ips_list.append(ip2)
   return new_ips_list
if __name__ == "__main__":
   pass
