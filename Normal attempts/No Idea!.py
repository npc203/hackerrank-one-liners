from collections import Counter,defaultdict
func = lambda:map(int,input().split())
happy=0
n,m=func()
a = defaultdict(int,Counter(func()))
for i in func():
    happy+=a[i]
      
for i in func():
    happy-=a[i]
 
print(happy)