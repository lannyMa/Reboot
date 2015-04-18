arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,65555,45]

max_one=0
max_two=0
tmp=0
i=0
for num in arr:
    if num>max_one:
        max_one=num
        tmp=i
    i=i+1
i=0
for num in arr:
    if num>max_two and i!=tmp:
        max_two=num
    i=i+1
print max_one
print max_two