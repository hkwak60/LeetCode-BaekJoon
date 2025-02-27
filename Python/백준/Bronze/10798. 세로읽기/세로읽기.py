voca = []
maxlen = 0
for i in range(5):
    voca.append(list(input()))
    maxlen = max(maxlen, len(voca[i]))

res = ""

for j in range(maxlen):
    for i in range(5):
        if len(voca[i])>0:
            res+=voca[i][0]
            voca[i].pop(0)

print(res)