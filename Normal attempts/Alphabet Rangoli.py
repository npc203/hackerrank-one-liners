def print_rangoli(size):
    w = size*2-1
    arr= []
    for i in range(1,size+1):
        a = size-1
        tmp = ""
        for j in range(w):
            if j%2 == 1 or j< w - 2*(i) :
                tmp+="-"                
            else:
                tmp+=chr(a+97)
                a-=1
        arr.append(tmp)
    half = ["".join(i+i[-2::-1]) for i in arr]
    print("\n".join(half+half[-2::-1]))
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
