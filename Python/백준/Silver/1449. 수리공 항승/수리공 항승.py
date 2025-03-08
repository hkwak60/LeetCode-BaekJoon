N, L = map(int,input().split())
holes = sorted(list(map(int,input().split())))

t = 1
start_of_tape = holes.pop(0)

while len(holes)>0:
    next_hole = holes.pop(0)
    if next_hole<start_of_tape+L:
        continue
    start_of_tape=next_hole
    t+=1

print(t)