for _ in range(int(input())):
    input()
    a=set(map(int,input().split()))
    input()
    print(not bool(a-set(map(int,input().split()))))