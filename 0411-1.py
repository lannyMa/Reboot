__author__ = 'wenwen'
#for name in ['wenwen','wd','pc']:
#    print name

#for num in range(1,99):
#    print num

#print range(20)
#for n in range(20):
#    print n

#for num in range(0,10):
#    if num==7:
#        break
#    print num

#for num in range(0,10):
#    if num==7:
#        continue
#    print num

#for n in range(10):
#    if n==7:
#        print n
#        continue

#for n in range(10):
#    if n==7:
#        continue
#        print n

#init_num=0
#init_count=0.0
#while True:
#    input_number=raw_input('Input number: ')
#    if not input_number:
#        break
#    else:
#        init_count=init_count+1
#        init_num=int(input_number)+init_num
#print init_num/init_count

#bj = 10000
#gz=50000
#y = 0
#while bj < 20000:
#    bj = bj * ( 1 + 0.0325 )
#    print bj
#    y = y + 1
#print y

#arrs=['C','js','python','js','css','js','html','node']
#count=0
#for arr in arrs:
#    if arr=='js':
#        count=count+1
#print count
#print 'js' in arrs

#person = {'name':'wenwen','score':'60'}
#print person
#print person['name']
#print person['score']
#if 'name' in person:
#    print person['name']
#if 'wenwen' in person:
#    print 'hello'
#for p in person:
#    print p
#    print person[p]

#arr=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
#maxn=0
#for num in arr:
#    if num>maxn:
#        maxn=num
#print maxn

#while True:
#    year=raw_input('please input year: ')
#    iyear=int(year)
#    if iyear%100==0:
#        if iyear%400==0:
#            print year+' shi run nian'
#            break
#        else:
#            continue
#    elif iyear%4==0:
#        print year+' shi run nian'
#        break
#    else:
#        continue
#print 'End'

#person = {
#    'name':'pc'
#}
#person['name'] = 'wd'
#person['age'] = 65
#print person
#for p in person:
#    print 'key is %s and value is %s' % (p,person[p])

###important###
#d = {}
#l = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']
#for item in l:
#    count = 0
#    for tmp in l:
#        if item==tmp:
#            count = count+1
#    d[item]=count
#for lang in d:
#    print 'language is %s and count is %s' % (lang,d[lang])


#d={}
#l = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']
#for item in l:
#    if item in d:
#        d[item]=d[item]+1
#    else:
#        d[item]=1
#for lang in d:
#    print 'language is %s and count is %s' % (lang,d[lang])

#homework
# nb way
arr=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_num=arr[0]
sec_num=0
for num in arr:
    if num>max_num:
        sec_num=max_num
        max_num=num
    elif max_num>num and num>sec_num:
        sec_num=num
print 'max='+str(max_num)
print 'sec='+str(sec_num)
# my way
#arr=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,5555,45]
#max_num=arr[0]
#sec_num=0
#for num in arr:
#    if num>max_num:
#        max_num=num
#for num1 in arr:
#        if num1>sec_num and num1!=max_num:
#            sec_num=num1
#print 'max='+str(max_num)
#print 'sec='+str(sec_num)