#coding:utf-8

inp = list(raw_input())

a = int(inp[0])
b = int(inp[1])
c = int(inp[2])
d = int(inp[3])

if a + b + c + d == 7:
    print str(a) + "+" + str(b) + "+" + str(c) + "+" + str(d) + "=7"
elif a - b + c + d == 7:
    print str(a) + "-" + str(b) + "+" + str(c) + "+" + str(d) + "=7"
elif a + b - c + d == 7:
    print str(a) + "+" + str(b) + "-" + str(c) + "+" + str(d) + "=7"
elif a + b + c - d == 7:
    print str(a) + "+" + str(b) + "+" + str(c) + "-" + str(d) + "=7"
elif a - b - c + d == 7:
    print str(a) + "-" + str(b) + "-" + str(c) + "+" + str(d) + "=7"
elif a - b + c - d == 7:
    print str(a) + "-" + str(b) + "+" + str(c) + "-" + str(d) + "=7"
elif a + b - c - d == 7:
    print str(a) + "+" + str(b) + "-" + str(c) + "-" + str(d) + "=7"
elif a - b - c - d == 7:
    print str(a) + "-" + str(b) + "-" + str(c) + "-" + str(d) + "=7"
