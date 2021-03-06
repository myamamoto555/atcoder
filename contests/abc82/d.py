# coding:utf-8

alls = raw_input()
tarx, tary = map(int, raw_input().split())

ss = alls.split("T")

xs = []
ys = []
posx = set()
posy = set()
posy.add(0)
for i, s in enumerate(ss):
    if i == 0:
        posx.add(len(s))
    elif i % 2 == 0:
        xs.append(len(s))
    else:
        ys.append(len(s))

for x in xs:
    tmpx = set()
    for px in posx:
        tmpx.add(px+x)
        tmpx.add(px-x)
    posx = tmpx

for y in ys:
    tmpy = set()
    for py in posy:
        tmpy.add(py+y)
        tmpy.add(py-y)
    posy = tmpy

if tarx in posx and tary in posy:
    print "Yes"
else:
    print "No"
