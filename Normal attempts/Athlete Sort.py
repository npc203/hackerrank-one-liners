n, m = map(int, input().split())
a = []
for i in range(n):
    a.append([int(i) for i in input().split()])
k = int(input())
for i in sorted(a, key=lambda x: x[k]):
    print(*i)