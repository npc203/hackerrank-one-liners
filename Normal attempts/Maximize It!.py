from itertools import product
k,m=map(int,input().split())
d = [[*map(int,input().split())][1:] for i in range(k)]
print(max(sum(map(lambda x : x**2,i))%m for i in product(*d)))