cube = lambda x: x**3 

def fibonacci(n):
    a = -1
    b = 1
    for i in range(n):
        c = a+b
        a = b
        b = c
        yield c
         
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))