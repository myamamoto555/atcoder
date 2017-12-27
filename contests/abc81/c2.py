# coding:utf-8

from collections import defaultdict

N, K = map(int, raw_input().split())
As = map(int, raw_input().split())

dic = defaultdict(lambda: 0)

for a in As:
    dic[a] += 1

tar = len(dic) - K

count = 0
if tar <= 0:
    print count
else:
    for i, (k, v) in enumerate(sorted(dic.items(), key=lambda x: x[1])):
        count += v
        if i+1 == tar:
            print count 
            break

