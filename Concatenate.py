(lambda np,n,m,p:(lambda o:print(np.concatenate((o(n), o(m)), axis = 0)))(lambda x: np.array([input().split() for _ in range(x)],int)))(__import__("numpy"),*map(int,input().split()))