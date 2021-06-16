n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    a = input().split()
    getattr(s,a[0])(*map(int,a[1:]))
print(sum(s))