score_words = lambda words: sum(1 if sum(1 for letter in word if letter in  ('a', 'e', 'i', 'o', 'u', 'y'))%2 else 2 for word in words)

# Stub code can't remove
n = int(input())
words = input().split()
print(score_words(words))