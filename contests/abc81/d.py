#coding:utf-8

N = int(raw_input())
As = map(int, raw_input().split())
Astmp = As

mi = min(As)
ma = max(As)


while True:
    if Astmp[0] == mi:
        del list[0]


if abs(mi) < abs(ma):
