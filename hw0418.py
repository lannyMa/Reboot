__author__ = 'wenwen'
demo_list=[1,2,'a','b',[4,5,6]]
arr=[1,2,3,4,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
###The realization of in function
#test=[4,5,6]
#init_index=0
#for obj in demo_list:
#    if obj == test:
#        print True
#        break
#    else:
#        if init_index == len(demo_list)-1:
#            print False
#        else:
#            init_index=init_index+1

###The realization of len function
#init_index=0
#for object in demo_list:
#    init_index=init_index+1
#print init_index

###The realization of max function
#init_max=arr[0]
#for num in arr:
#    if num>init_max:
#        init_max=num
#print init_max

###The realization of min function
#init_min=arr[0]
#for num in arr:
#    if num<init_min:
#        init_min=num
#print init_min

# ##The realization of append function
# init_count=len(demo_list)
# add_item=[2,3]
# demo_list[init_count:]=[add_item]
# print demo_list

###sort
# count=0
# while count<len(arr):
#     init_index=0
#     for i in range(0,len(arr)-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]
#     count=count+1
# print arr

# ##The realization of extend function
# demo_list1=[4,5,6]
# demo_list[len(demo_list):]=demo_list1
# print demo_list

###the index of second 4
#arr_list=[1,2,3,4,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
#way 1
# count=0
# init_index=0
# for item in arr_list:
#     if item == 4:
#         count=count+1
#         if count==2:
#             break
#     init_index=init_index+1
# print init_index

#way 2
# init_index=arr_list.index(4)
# print  arr_list[init_index+1:].index(4)+init_index+1

#way 3
# print arr_list.index(4,arr_list.index(4)+1)

###list
# init_dothing=[]
# init_status=True
#
# while init_status:
#     action=raw_input('Input the action: ')
#     if action=='add':
#         thing=raw_input('Input the plan: ')
#         init_dothing.append(thing)
#         print init_dothing
#     elif action=='do':
#         if len(init_dothing)>0:
#             print init_dothing.pop(0)
#         else:
#             init_status=False
#     else:
#         print 'You must input add or do'

###The realization of reverse function
##demo_list.reverse()
##print demo_list

# for i in range(0,len(demo_list)-1):
#     item=demo_list[len(demo_list)-1]
#     demo_list.remove(item)
#     demo_list.insert(i,item)
# #    print demo_list
# print demo_list

###
# for item in arr_list:
#     item_count=arr_list.count(item)
#     if item_count>1:
#         print(item)
#         for i in range(1,item_count):
#             arr_list.remove(item)
# print arr_list

###
#way 1
arr_list1=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr_list2=[2,1,3,2,43,234,454,452,234,14,21,14]
# d={}
# for num in arr_list1:
#     if num in arr_list2:
#         d[num]=arr_list1.count(num)+arr_list2.count(num)
# print d
#way 2
# for i in arr_list1:
#     for j in arr_list2:
#         if i==j:
#             print i



###HomeWork####
# arr_list=[5000,4333,3,4,888,12,3,14,3,21,2,2,3,4111,22,3333,4]
# init_count=len(arr_list)
# for i in range(0,init_count):
#     init_index=i
# #choose min
#     for j in range(i+1,init_count):
#         if arr_list[init_index]>arr_list[j]:
#             init_index=j
# #            print 'init_index='+str(init_index)
# #            print arr_list
#     temp=arr_list[i]
#     arr_list[i]=arr_list[init_index]
#     arr_list[init_index]=temp
# #    print i
# #    print arr_list
#
# print(arr_list)

##zhangchen
l2 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
l1 = l2[0]


for i in l2:
    for l in range(1,len(l1)):
        if i <= l1[l]:
            l1.insert(l,i)
            print l1
            print '*'*10
            break

        elif i > l1[len(l1)-1]:
            l1.append(i)
print l1
print l2