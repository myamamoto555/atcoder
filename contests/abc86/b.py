# coding:utf-8

import math
a, b = raw_input().split()

c = math.sqrt(int(a + b))
d = int(c)

if c == d:
    print 'Yes'
else:
    print 'No'

