average = (lambda arr: (lambda x: sum(x)/len(x))(set(arr)))

# Can't remove, boilerplate code
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)