(lambda g:[None for g["cube"],g["actual"],g["fibonacci"] in [(lambda x: x**3,lambda x: x if x<2 else actual(x-1)+actual(x-2),lambda n: map(actual, range(n)))]])(globals())
         
# Stub code can't be removed. 
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))