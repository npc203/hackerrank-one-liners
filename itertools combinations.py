(lambda x: (lambda func : [print(*map(lambda x:"".join(x),func(sorted(x[0]),i)),sep="\n") for i in range(1,int(x[1])+1)])(__import__("itertools").combinations))(input().split())