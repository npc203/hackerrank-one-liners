print_rangoli = (lambda size: (lambda g: (lambda half : print("\n".join(half+half[-2::-1])))(["".join(i+i[-2::-1]) for i in [(lambda a : ''.join("-" if j%2 == 1 or j< size*2-1 - 2*(i) else (lambda x:(lambda _:x)([None for g['a'] in (g['a']-1,)][0]))(chr(g['a']+97))  for j in range(size*2-1)))([g['a'] for g['a'] in (size-1,)][0]) for i in range(1,size+1)]]))(globals()))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
