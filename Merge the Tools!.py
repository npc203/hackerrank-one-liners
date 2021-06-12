merge_the_tools = lambda string, k : print(*map(lambda x:"".join(dict.fromkeys(x)),[string[i:i+k] for i in range(0,len(string),k)]),sep="\n")

# Can't remove, boilerplate code
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)