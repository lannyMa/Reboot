#!/usr/bin/env python

read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
str_list=list(read_me)
str_dict={}
for char in str_list:
    if char not in str_dict:
        str_dict[char]=str_list.count(char)
temp_list=str_dict.items()
for i in range(0,len(temp_list)):
    for j in range(0,len(temp_list)-1):
        if temp_list[j][1]>temp_list[j+1][1]:
            temp_list[j],temp_list[j+1]=temp_list[j+1],temp_list[j]
f=open('demo.txt','a')
for index in range(1,11):
    string='No.%s is %s , and count is %s\n' % (index,temp_list[-index][0],str(temp_list[-index][1]))
    f.write(string)
f.close()

# f = open('www_access_20140823.log')
#file_str = str(f.read())
# str_list=file_str.split(' ')
# ip_list=[]
# ip_list.append(str_list[0])
# for ip in str_list:
#     if ip == '"-"':
#         ip_list.append(str_list.append(str_list.index(ip)+1))



