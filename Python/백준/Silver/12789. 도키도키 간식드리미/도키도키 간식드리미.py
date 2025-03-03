students = int(input())

wait = list(map(int,input().split()))

stack = []
next = 1
status = ''
while len(wait)>0:
    if wait[0]==next:
        wait.pop(0)
        next+=1
        continue
    else:
        if len(stack)>0:
            if stack[len(stack)-1]==next:
                stack.pop(len(stack)-1)
                next+=1
                continue
            if stack[len(stack)-1]>wait[0]:
                stack.append(wait.pop(0))
            else:
                status = 'Sad'
                break
        else:
            stack.append(wait.pop(0))

if status=='Sad':
    print(status)
else:
    print('Nice')