# -*- coding: utf-8 -*-
""" Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды, в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ignore = ["duplex", "alias","configuration"]
from sys import argv
name_file=argv[1]
with open(name_file,'r') as f:
   output=f.readlines()

for item in output:
   if not ((ignore[0] in item) or (ignore[1] in item) or (ignore[2] in item)):
      print(item)

#for line in output:
#   if ('!' in line) :
 #     continue
  # else:
   #   word_inter=set(ignore)&set(line.replace('\n','').split())
   #if not word_inter:
    #  result.append(line.replace('\n',''))
     # print(line.replace('\n',''))
