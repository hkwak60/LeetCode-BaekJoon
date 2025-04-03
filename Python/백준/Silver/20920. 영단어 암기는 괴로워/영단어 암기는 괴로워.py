import sys

N,M= map(int,sys.stdin.readline().strip().split())

words = {}
for i in range(N):
    word = sys.stdin.readline().strip()
    if len(word)>=M:
        if word in words:
            words[word]+=1
        else:
            words[word] = 1

s_words = dict(sorted(words.items(), key=lambda x: (-x[1],-len(x[0]),x[0])))
# print(s_words)
for i in s_words:
    print(i)