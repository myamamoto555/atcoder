# coding:utf-8

N = int(raw_input())

xtmp = 0
ytmp = 0
ttmp = 0
flag = True
allinfo = []
for i in range(N):
    t, x, y = map(int, raw_input().split())
    allinfo.append((t, x, y))

for t, x, y in allinfo:
    xdif = abs(x - xtmp)
    ydif = abs(y - ytmp)
    tdif = t - ttmp
    if tdif >= xdif + ydif:
        if tdif % 2 == (xdif + ydif) % 2:
            continue 
        else:
            flag = False
            break
    else:
        flag = False
        break

if flag:
    print 'Yes'
else:
    print 'No'
