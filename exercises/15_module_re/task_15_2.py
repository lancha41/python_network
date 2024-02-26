# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re
def parse_sh_ip_int_br(config):
   with open(config,'r') as f:
      lines=f.readlines()
   flist=[]
   regex=(r'(\S+)\s+(\d+\.{3}\d*|\S+)\s+(\S+\s+){2}(\S{2,4}|\S+\s+\S+)\s+(\S+)')
   for line in lines[2:]:
      match=re.search(regex,line)
      if match:
         flist.append((match.group(1),match.group(2),match.group(4),match.group(5),))
   return flist

print(parse_sh_ip_int_br('sh_ip_int_br_2.txt'))
