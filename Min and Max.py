(lambda np:print(np.max(np.min(np.array([np.array(i.split(),int) for i in open(0).read().split("\n")[1:]],int),axis=1))))(__import__("numpy"))