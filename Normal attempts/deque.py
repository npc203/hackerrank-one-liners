from collections import deque
d = deque()
for _ in range(int(input())):
    a = input().split()
    getattr(d,a[0])(*map(int,a[1:]))
print(*d)