# coding:utf-8

A, B = map(int, raw_input().split())
S = raw_input()

flag = False
if S[A] == '-':
    Ss = S.split('-')
    if len(Ss) == 2:
        if len(Ss[0]) == A and len(Ss[1]) == B:
            if Ss[0].isdigit() and Ss[1].isdigit():
                flag = True

if flag:
    print 'Yes'
else:
    print 'No'
        
