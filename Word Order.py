(lambda a : print(f"{len(a)}\n{' '.join(map(str,a.values()))}"))(__import__("collections").Counter(open(0).read().split("\n")[1:]))