(lambda x,y : print(*map(lambda x:"".join(x),__import__("itertools").combinations_with_replacement(x,y)),sep="\n"))(*(lambda x:(sorted(x[0]),int(x[1])))(input().split()))