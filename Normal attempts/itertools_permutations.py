from itertools import permutations
x = input().split()
x[0] = sorted(x[0])
x[1] = int(x[1])
print(*map(lambda x:"".join(x),permutations(*x)),sep="\n")