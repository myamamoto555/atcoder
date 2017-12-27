# coding:utf-8

from collections import defaultdict

N = int(raw_input())
As = map(int, raw_input().split())

dic = defaultdict(lambda:0)
for a in As:
    dic[a] += 1

count = 0
for k, v in dic.items():
    if k > v:
        count += v
    else:
        count += v-k

print count

