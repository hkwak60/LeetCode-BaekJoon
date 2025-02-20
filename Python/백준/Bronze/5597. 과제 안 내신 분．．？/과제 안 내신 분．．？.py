students = []
for i in range(30):
    students.append(i+1)
for i in range(28):
    students.remove(int(input()))
for i in students:
    print(i)