(lambda _: (lambda s: (lambda _ : print(sum(s)))([(lambda a: getattr(s,a[0])(*map(int,a[1:])))(input().split()) for i in range(int(input()))])
)(set(map(int, input().split()))) )(input())