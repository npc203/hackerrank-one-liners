from itertools import combinations_with_replacement
x = input().split()
x[0] = sorted(x[0])
print(*map(lambda x:"".join(x),combinations_with_replacement(x[0],int(x[1]))),sep="\n")