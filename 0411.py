#coding=UTF-8
print 'Hello World'
# string format
var_db='database_name'
var_id='2'
s='select * from %s where id = %s'
sql=s % (var_db,var_id)
print sql

print 2==3
print 2>3
print 'w' in 'wenwen'
print 'w' not in 'wenwen'

print 2>3 and 3>2
print 2>3 or 3>2

name=raw_input('Please input your name: ')
if name=='shaqiang':
    print 'Hello %s ' % (name)
else:
    print 'you are not shaqiang'

name1=raw_input('please input your name: ')
if name1=='pc':
    print 'hehe'
else:
    print 'hello'

name2=raw_input('please input your name: ')
if name2=='pc':
    print 'hehe'
elif name2=='wd':
    print 'hello'
else:
    print('who r u')

print(2+3)
print('2'+'3')

user_age=raw_input('your age: ')
print(user_age*2)
print(int(user_age)*2)

num=raw_input('input number: ')
num1=raw_input('input number: ')
print((int(num)+int(num1))/2)

i=0
while i < 100:
    print i
    i=i+1

sum=0
while True:
    x=raw_input('please input number: ')
    if x=='pc':
        break
    else:
        sum=int(x)+sum
print sum

init_num=0
init_status='input'
while init_status=='input':
    input_number=raw_input('Input number: ')
    if input_number=='pc':
        init_status='stop'
    else:
        init_num=int(input_number)+init_num
print init_num

init_num=0
init_status='input'
while init_status=='input':
    input_number=raw_input('Input number: ')
    if not input_number:
        init_status='stop'
    else:
        init_num=int(input_number)+init_num
print init_num
