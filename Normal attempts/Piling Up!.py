for t in range(int(input())):
    input()
    a = [*map(int,input().split())]
    mid = a.index(min(a))
    l = a[:mid]
    r = a[mid+1:]
    print("YNeos"[not (sorted(l, reverse=True) == l and sorted(r) == r)::2])