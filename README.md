# Reboot
Reboot TEST

Homework(0411):

1.判断用户输入
    如果用户输入的是'pc',打印一条‘hehe’
    如果用户输入的是其他字符,打印一条‘hello’
    
2.用户输入两个数，求平均值
3.让用户一直输入数字
    如果输入的是'pc'，终止程序
    打印所有数字之和
4.让用户一直输入数字（只输入数字）
    如果没输入任何值，终止程序
    打印所有输入数字的平均值
5.存10000块钱，年利率是3.25%
    求多少年之后，存款能翻番
6.遍历一个list ['C','js','python','js','css','js','html','node']
    统计这个list中，js出现的次数
7.[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
    求这个list的最大值
8.用户输入数字 判断是不是闰年
    1.如果是100的倍数，要被400整除
    2.被4整除
    3.比如1900不是闰年，2000，2004是闰年
    如果输入不是闰年，提示信息，并且继续输入
9.['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']
    求出这个list中，每个字符出现的次数
10 作业：第七题的list，求出最大的两个值

Homework(0418):
1.实现in这个操作的功能
2.实现 len max min三个操作
3.实现append功能
    （数组最后位置添加元素）
4.实现一个list的排序（不用sort）
    思路：冒泡排序
    遍历一个list，比值交换，遍历一次结束
        最大值在list最后面
    遍历len(list)次，排序完成
    [1,2,1,4,1]
5.实现extend的效果
6.
一个序列[1,2,3,4,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
求第二个4的索引值
<!-- (4,arr.index(4)+1) -->
7.待办事项，让用户持续输入，采用队列
    如果用户输入的是add，让用户再输入字符，加到待办事项列表
        打印列表
        让用户继续输入
    如果用户输入的是do，从代办事项取出一个打印出来
        如果没有事情要做，终止程序
        让用户继续输入
8 反向打印一个list，模拟reverse的功能
    (禁止用切片)
9 [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
    数组去重
10  arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
    arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
    求两个数组共同的值（去重）

作业：
    插入排序对list进行排序

Homework(0425):
1.实现copy的功能
2.统计每个字符出现的次数
(read_me字符串在最后)
3.实现fromkeys的功能
4.实现keys功能
5.实现update功能
6.把一个dict的key和value反转
    （如果value有重复的，把多个key，放在list）
    提示：判断是否list 
        print isinstance([1,2,3],list)
        print type([1,2]) == type([])
init_dict = {'waihao':'pc','name':'pc','age':12,'job':'IT'}

循环 init_dict  k和v
    new_dict[v]不存在
        new_dict[v] = k
    else：
        if new_dict[v]是一个list
            new_dict[v].append(k)
        else:
            new_dict变成，存着之前的值，和刚遍历的值

{'waihao':'pc','name':'pc','a':'pc','age':12,'job':'IT'}
{'pc':'waihao'}
{'pc':['waihao','name']}
{'pc':['waihao','name','a']}

    思路：
        循环（k,v） init_dict
            new_dict[v]存在：
                if new_dict[v]不是list，说明是第二次出现
                    new_dict[v] = [原来的值，k]
                else new_dict[v]是list：
                    new_dict[v].append(k)
            new_dict[v]不存在
                new_dict[v] = k     

7,实现首字母大写的功能 其他字母小写
    'rebOoT'
    （upper lower）
    ‘Reboot’
8. 'reboot' 字符串倒序（不能用切片）
9.用户输入员工名字和id，名字和id之间用:分隔
    多个用户 用逗号分隔，最终输入所有用户对应id的信息
输入内容： em1:009,em2:002,em3:003
输出：[('em1', '009'), ('em2', '002'), ('em3', '003 ')]
    用户可能会把冒号输入成分号 ，也能接受
作业：
    第二题加一个需求，打印出前十个出现的字符（只用学过的知识）

read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
    eg：中文逗号和英文逗号，中文冒号和英文冒号，都支持
