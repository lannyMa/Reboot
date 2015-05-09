try:
    f = open('xx.txt')
except:
    print 'file not exist'
else:
    print 'file exist'
finally:
    print 'always'