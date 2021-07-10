import re
a = open(0).read().split("\n")[1:]
x = "".join(a[i][j] for j in range(len(a[0])) for i in range(len(a)))
print(re.sub("(?<=([A-z0-9]))([^A-z0-9]+)(?=[A-z0-9])"," ",x))