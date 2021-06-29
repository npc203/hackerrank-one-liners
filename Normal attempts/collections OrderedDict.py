from collections import OrderedDict
n = int(input())
s = OrderedDict()
for i in range(n):
    a,x = input().rsplit(" ",1)
    s[a] = s.get(a,0) + int(x)
print(*map(lambda x:f"{x[0]} {x[1]}",s.items()),sep="\n")