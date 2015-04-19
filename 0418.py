#implemnt operaton "in"

#demo_list=[1,2,'a','b',[4,5,6]]
#obj_in = raw_input('input any: ')
#for obj in demo_list:
#    if obj_in == obj:
#        print 'True'
#        break
#    else:
#        print 'False'
#print '----------------------'
#print 1 in demo_list
#print '1' in demo_list
#print [4,5,6] in demo_list

arr=[1,2,3,2,12,3,1,3,-21,-2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
print len(arr)
print max(arr)
print min(arr)
del arr[2]
print arr*2
l = ['a','b','c']
print arr + l
print len(arr)
print arr[2:8]
print arr[0:-1]
print arr[5::3]
print arr[5:9:-1]
print arr[9:5:-1]

arr[0]='no.1'
print arr

#arr[0:]=[123,'222',123]
#print arr

arr[0:2]=[3,4]
print arr
arr[0:1]=[[1,2,3]]
print arr
arr[0:2]=[]
print arr

print arr[1:5:2]
arr[1:5:2]='ab'
print arr

demo_list=[1,2,[3] in [4,5,6]]
print demo_list

print len(arr)