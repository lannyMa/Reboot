#!/usr/bin/env python
#coding:UTF-8

tem_dict={}
tem_list=[]
tem_file=open('tem.txt','r')
tem_sum=0
tem_avg=0.0
tem_max=0
# i=0
# for line in tem_file.readlines():
#     tem_c=float(str(line).split(' ')[1])
#     tem_sum=tem_sum+tem_c
#     tem_list.append(tem_c)
#     i=i+1
# #    tem_dict={(line).split(' ')[0]:float(str(line).split(' ')[1])}
# tem_avg=tem_sum/i
tmp_file=tem_file.read()
tmp_list=str(tmp_file).split()
tmp_count=len(tmp_list)
for i in range(1,tmp_count,2):
    tem_sum=tem_sum+float(tmp_list[i])
    tem_list.append(float(tmp_list[i]))
for tem in tem_list:
    if tem > tem_max:
        tem_max=tem
tem_avg=tem_sum/(tmp_count/2)
print 'highest is %s' % tem_max
print 'avg is %s' % tem_avg




