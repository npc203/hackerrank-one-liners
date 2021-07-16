import re

for i in range(int(input())):
    a,b = input().split()
    if re.search(r"<[a-zA-Z][\w\-\.]*@[a-zA-Z]*\.[a-zA-Z]{1,3}>",b):
        print(a,b)