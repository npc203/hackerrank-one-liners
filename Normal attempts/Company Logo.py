from collections import Counter
a =  Counter(input())
b = sorted(sorted(a.items()),key=lambda x:x[1],reverse=True)
for i,j in b[:3]:
    print(i,j)