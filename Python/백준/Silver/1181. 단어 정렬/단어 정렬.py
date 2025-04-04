import sys

N = int(sys.stdin.readline().strip())

words = []
for _ in range(N):
    word = sys.stdin.readline().strip()
    if word not in words:
        words.append(word)

s_words = sorted(words, key = lambda x: (len(x),x))
for w in s_words:
    print(w)