from collections import defaultdict
x=defaultdict(list)
n,m=map(int,input().split())
for i in range(n):
    x[input()].append(i+1)

for i in range(m):
    tmp = input()
    if tmp in x:
        print(*x[tmp])
    else:
        print(-1)