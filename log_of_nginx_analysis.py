#!/usr/bin/env python
#~*~coding:UTF-8~*~

log_file=open('www_access_20140823.log','r')
log_list=[]
log_dict={}
for line in log_file.readlines():
    tmp_list=line.split()
    tmp_tuple=(tmp_list[8],tmp_list[6],tmp_list[0])
    # log_list.append(tmp_list[6])
    # log_list.append(tmp_list[0])
    if tmp_tuple not in log_dict:
        log_dict[tmp_tuple]=1
    else:
        log_dict[tmp_tuple]=log_dict[tmp_tuple]+1
    # print log_dict[tmp_list[0]]
    # print log_list
# for (k,v) in log_dict.items():
#     log_list=[]
#     log_list.append(k[0])
#     log_list.append(k[1])
#     log_list.append((k[2],v))
#     # tmp_file=open('log_analysis.txt','a')
#     # # tmp_file.write(str(log_file))
#     # tmp_file.write(str(log_list)+'\n')
#     # tmp_file.close()
#     print log_list

tmp_list1=log_dict.items()
# for i in range(10):
#     for j in range(len(tmp_list1)-1):
#         if tmp_list1[j][1]>tmp_list1[j+1][1]:
#             tmp_list1[j],tmp_list1[j+1]=tmp_list1[j+1],tmp_list1[j]
#print tmp_list1
def sort_count(t):
    return t[1]
for s in sorted(tmp_list1,key=sort_count):
    print s
# print tmp_list1[0:9]
# ip_dict={}
# url_dict={}
# for (k,v) in tmp_list1:
#     tmp_ip=k[2]
#     tmp_url=k[1]
#     tmp_ip_dict={}
#     ip_count=0
#     if tmp_ip not in ip_dict:
#         for (key,value) in tmp_list1:
#             if tmp_ip==key[2]:
#                 ip_count=ip_count+value
#         ip_dict[tmp_ip]=ip_count
#     if tmp_url not in url_dict:
#         tmp_ip_dict[tmp_ip]=v
#         url_dict[tmp_url]=tmp_ip_dict
#     else:
#         if tmp_ip not in url_dict[tmp_url]:
#             url_dict[tmp_url][tmp_ip]=v
# print url_dict['/data/uploads/2014/0722/23/small_53ce859e37394.jpg']
#print ip_dict
# ip_list=ip_dict.items()
# for i in range(10):
#     for j in range(len(ip_list)-1):
#         if ip_list[j][1]>ip_list[j+1][1]:
#             ip_list[j],ip_list[j+1]=ip_list[j+1],ip_list[j]
# print ip_list[-11:-1]
# for i in range(0,len(log_dict)):
#     log_list.append(tmp_list1[i][0][0])
#     log_list.append(tmp_list1[i][0][1])
#     log_list.append((tmp_list1[i][0][2],tmp_list1[i][1]))
    # tmp_file=open('log_analysis1.txt','a')
#     # # tmp_file.write(str(log_file))
#     tmp_file.write(str(log_list)+'\n')
#     tmp_file.close()
log_file.close()
