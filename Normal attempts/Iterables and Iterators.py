from itertools import combinations

n = int(input())
a = input().split()
k = int(input())
fin = 0
combos = [*combinations(a,k)]
for i in combos:
    if "a" in i:
        fin+=1

print(fin/len(combos))