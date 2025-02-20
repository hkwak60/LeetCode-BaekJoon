line = input().split()

N = int(line[0])
M = int(line[1])

pokedex = []
pokedex_dic = {}
for i in range(1,N+1):
    pokemon = input()
    pokedex.append(pokemon)
    pokedex_dic[pokemon]=i

answers = []
for i in range(M):
    quiz = input()
    if quiz.isnumeric():
        answers.append(pokedex[int(quiz)-1])
    else:
        answers.append(pokedex_dic[quiz])

for answer in answers:
    print(answer)