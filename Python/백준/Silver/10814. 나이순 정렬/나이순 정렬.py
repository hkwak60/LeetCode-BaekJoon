users = int(input())

data = [input().split() for _ in range(users)]
data = [(int(age), name) for age, name in data]

data.sort(key=lambda x: (x[0]))

for age, name in data:
    print(age, name)