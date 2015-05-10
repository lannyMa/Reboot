#!/usr/bin/env python
#~*~coding:UTF-8~*~

log_file=open('www_access_20140823.log','r')
log_list=[]
log_dict={}
for line in log_file.readlines():
    log_list=[]
    tmp_list=line.split()
    log_list.append(tmp_list[8])
    log_list.append(tmp_list[6])
    # log_list.append(tmp_list[0])
    if tmp_list[0] not in log_dict:
        log_dict[tmp_list[0]]=1
    else:
        log_dict[tmp_list[0]]=log_dict[tmp_list[0]]+1
    log_list.append((tmp_list[0],log_dict[tmp_list[0]]))
    # print log_dict[tmp_list[0]]
    print log_list
log_file.close()