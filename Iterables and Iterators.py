(lambda _: (lambda a,k : (lambda x : print(sum(1 for i in x if "a" in i)/len(x)))([*__import__("itertools").combinations(a,k)]))(input().split(),int(input())) )(input())