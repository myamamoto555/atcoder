#coding:utf-8

S = raw_input()
print S
ssz = S.split('0')
sso = S.split('1')
max = 0
for sss in ssz:
    if max < len(sss):
        max = len(sss)

for sss in sso:
    if max < len(sss):
        max = len(sss)
if S[0]== S[-1]:
    max+= 1
print max
