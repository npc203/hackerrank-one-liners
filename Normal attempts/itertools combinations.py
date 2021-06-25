from itertools import combinations
x = input().split()
x[0] = sorted(x[0])
for i in range(1,int(x[1])+1):
    print(*map(lambda x:"".join(x),combinations(x[0],i)),sep="\n")