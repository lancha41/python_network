# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
prefix=[]
ad_metric=[]
nh=[]
lu=[]
outint=[]
with open('ospf.txt', 'r') as f:
    output=f.readlines()
for i in output:
    prefix.append(i.split()[1])
    ad_metric.append(i.split()[2])
    nh.append(i.split()[4])
    lu.append(i.split()[5])
    outint.append(i.split()[-1])
for p in range(len(output)):
    print("Prefix                {}\n"
    "AD/Metric             {}\n"
    "Next-Hop              {}\n"
    "Last update           {}\n"
    "Outbound Interface    {}".format(prefix[p],ad_metric[p].replace("[",'').replace(']',''),nh[p][:-1],lu[p][:-1],outint[p]))
