# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
b=input("Enter VLAN number: ")
pp=[]
result=[]

with open('CAM_table.txt','r') as f:
    file=f.readlines()
    for item in file:
        item_list=item.split()
        if item_list and item_list[0][1].isdigit():
          pp.append("{:<9}{:<20}{}".format(item_list[0],item_list[1],item_list[3]))

for i in pp:
   result.append(i.split())
for i in result:
    i[0]=int(i[0])
result.sort()
for i in result:
   i[0]=str(i[0])
   if b==i[0]:
     print("{:<9}{:<20}{}".format(i[0],i[1],i[2]))
