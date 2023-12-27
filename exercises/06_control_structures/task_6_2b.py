# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_add=input('please insert ip address (example - 10.1.1.1): ')
ip_add_list=ip_add.split('.')
n=ip_add.split('.')
a = True

while True:
	try:
		int(ip_add.replace('.','')) 
		if len(n)!=4:
			raise ValueError
			break
		elif not(int(n[0])>=0 and int(n[0])<=255 and int(n[1])>=0 and int(n[1])<=255 and int(n[2])>=0 and int(n[2])<=255 and int(n[3])>=0 and int(n[3])<=255):
			raise ValueError
			break
	except ValueError:
		print("Неправильный IP-адрес")
		a=False
		break while a :
        if int(ip_add_list[0]) >=1 and int(ip_add_list[0]) <=223:
                print('unicast')
                break
        elif int(ip_add_list[0]) >=224 and int(ip_add_list[0]) <=239:
                print('multicast')
                break
        elif int(ip_add_list[0]) == int(ip_add_list[1]) == int(ip_add_list[2]) == int(ip_add_list[3]) == 255:
                print('local broadcast')
                break
        elif int(ip_add_list[0]) == int(ip_add_list[1]) == int(ip_add_list[2]) == int(ip_add_list[3]) == 0:
                print('unassigned')
                break
        else:
                print('unused')
                break
