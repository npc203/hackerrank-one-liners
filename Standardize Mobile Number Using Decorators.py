wrapper= lambda f: lambda l: f([f"+91 {i[-10:-5]} {i[-5:]}" for i in l])

# HUGE Boilerplate code, can't remove.
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 