(lambda np:(lambda a: (lambda _:print(a.flatten()))(print(a.transpose())))(np.array([np.array([*map(int,i.split())]) for i in open(0).read().split("\n")[1:]])))(__import__("numpy"))