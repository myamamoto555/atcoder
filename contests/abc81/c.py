# coding:utf-8

from collections import defaultdict

N, K = map(int, raw_input().split())
As = map(int, raw_input().split())

dic = defaultdict(lambda: 0)

for a in As:
    dic[a] += 1

count = 0
while True:
    if len(dic) <= K:
        break
    dekey = min(dic, key=(lambda x: dic[x]))
    count += dic[dekey]
    del dic[dekey]

print count
