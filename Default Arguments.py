# Too many stub templates here so removed.
print_from_stream = lambda n, stream=None: (lambda stream: [print(stream.get_next()) for _ in range(n)])(EvenStream()if not stream else stream)