# coding:utf-8

import copy

alls = raw_input()
tarx, tary = map(int, raw_input().split())

ss = alls.split("T")

xs = []
ys = []
posx = []
posy = [0]
for i, s in enumerate(ss):
    if i == 0:
        posx.append(len(s))
    elif i % 2 == 0:
        xs.append(len(s))
    else:
        ys.append(len(s))

for x in xs:
    tmpx = []
    for px in posx:
        tmpx.append(px+x)
        tmpx.append(px-x)
    set(tmpx)
    posx = copy.deepcopy(tmpx)

for y in ys:
    tmpy = []
    for py in posy:
        tmpy.append(py+y)
        tmpy.append(py-y)
    set(tmpy)
    posy = copy.deepcopy(tmpy)

if tarx in posx and tary in posy:
    print "Yes"
else:
    print "No"
