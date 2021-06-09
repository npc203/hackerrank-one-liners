def merge_the_tools(string, k):
    s = [string[i:i+k] for i in range(0,len(string),k)]
    print(*map(lambda x:"".join(dict.fromkeys(x)),s),sep="\n")
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
