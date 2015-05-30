###sorted and lambda
# init_list=[(1,4),(5,1),(2,3)]
# # def sorted_obj(obj):
# #     return max(obj)
# def compare(obj):
#     if obj[0]>obj[1]:
#         return obj[0]
#     else:
#         return obj[1]
# # new_list=sorted(init_list,key=sorted_obj)
# # new_list=sorted(init_list,key=lambda obj:max(obj))
# new_list=sorted(init_list,key=lambda obj:compare(obj))
# print sorted(init_list,key=lambda (x,y):x*(x>y)+y*(x<=y))
# print new_list

###add

def operate(str,pri):
    str_list=[]
    tmp_str=''
    for j in list(str):
        try:
            int(j)
        except:
            str_list.append(tmp_str)
            str_list.append(j)
            tmp_str=''
        else:
            tmp_str=tmp_str+j
    str_list.append(tmp_str)
    result=int(str_list[0])
    if not pri:
        print str_list
        for i in range(len(str_list)):
            if str_list[i] == '+':
                result+=int(str_list[i+1])
            elif str_list[i] == '-':
                result-=int(str_list[i+1])
            elif str_list[i] == '*':
                result*=int(str_list[i+1])
            elif str_list[i] == '/':
                if int(str_list[i+1])!=0:
                    result/=int(str_list[i+1])
                else:
                    return 'Error'
            return result
    else:
        result=0
        tmp_list=[]
        ccc=str_list.count('*')+str_list.count('/')
        if ccc != 0:
            i=1
            location=0
            while i<len(str_list):
                if str_list[i]=='*':
                    result=int(str_list.pop(i-1))*int(str_list.pop(i))

                    str_list[i-1]=result

                elif str_list[i]=='/':
                    result=int(str_list.pop(i-1))/int(str_list.pop(i))
                    str_list[i-1]=result

                i+=2
        return str_list

x=operate('5+8*1-6*33*3/4*6',True)
print x