import itertools
a=map(int,input().split())
b=map(int,input().split())
print(*itertools.product(a,b))