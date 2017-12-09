# coding:utf-8

N = raw_input()
ns = list(N)

if ns[0] == ns[1] and ns[1] == ns[2]:
    print "Yes"
elif ns[1] == ns[2] and ns[2] == ns[3]:
    print "Yes"
else:
    print "No"
