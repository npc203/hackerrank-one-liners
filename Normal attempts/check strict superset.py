a = set(map(int,input().split()))
x = True
for i in range(int(input())):
    if(set(map(int,input().split()))-a):
        x = False
        break
print(x)