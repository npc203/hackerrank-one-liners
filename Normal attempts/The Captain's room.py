a = int(input())
x = sorted(map(int,input().split()))
print(set(x[::2]).symmetric_difference(set(x[1::2])).pop())