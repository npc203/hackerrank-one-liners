(lambda x: print(*x if x else [-1],sep="\n"))(list(map(lambda x: x.group()[:-1],__import__("re").finditer(r"(?i)(?<=[^aeiou])[aeiou]{2,}[^aeiou]",input()))))