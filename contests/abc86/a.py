#coding:utf-8

a, b = map(int, raw_input().split())

if (a * b) % 2 == 0:
    print 'Even'
else:
    print 'Odd'
