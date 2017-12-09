#coding:utf-8

H, W = map(int, raw_input().split())
c = []
for i in range(10):
    c.append(map(int, raw_input().split()))
a = []
for h in range(H):
    a.append(map(int, raw_input().split()))

print c
print a
