# coding:utf-8

X, Y = map(int, raw_input().split())

count = 1
while(True):
    if X * 2 <= Y:
        count += 1
        X *= 2
    else:
        break

print count
