from collections import Counter
n=int(input())
shoes = Counter(map(int,input().split()))
profit = 0
for i in range(int(input())):
    s,cost = map(int,input().split())
    if shoes[s]>0:
        profit+=cost
        shoes[s]-=1
print(profit)