# coding:utf-8


N = raw_input()
fs = list(N)

fx = 0
for f in fs:
    fx += int(f)

if int(N) % fx == 0:
    print "Yes"
else:
    print "No"
