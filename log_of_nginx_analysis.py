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
for (k,v) in log_dict.items():
    log_list=[]
    log_list.append(k[0])
    log_list.append(k[1])
    log_list.append((k[2],v))
    print log_list
log_file.close()
