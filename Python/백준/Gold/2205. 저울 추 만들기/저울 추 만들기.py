import sys


N = int(sys.stdin.readline().strip())
if N==1:
    print(1)
    exit()
elif N==2:
    print(1)
    print(2)
    exit()
else:
    dic2 = {1:3,2:2,3:1}


    powers_of_2 = {2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192,16384}
    sorted_pow2_list = sorted(list(powers_of_2))

    pow = 2

    for x in range(4,N+1):
        changing = {0}
        modified = {0}
        if x==2**pow:
            dic2[x]=x
            pow+=1
        else:
            matching_y = 2**pow-x
            dic2[x] = matching_y
            changing.add(dic2[matching_y])
            modified.add(matching_y)
            dic2[matching_y] = x
            while len(changing)>1:
                y = list(changing)[-1]
                changing.remove(y)
                if dic2[y] in modified:
                    dic2[y] = y
                if dic2[y]+y not in powers_of_2:
                    # print("nope",dic2[y],y)
                    for i in range(1,13):
                        if y<sorted_pow2_list[i]:
                            matching_y = sorted_pow2_list[i]-y
                            # print(matching_y,y)
                            break
                    dic2[y] = matching_y
                    changing.add(dic2[matching_y])
                    modified.add(matching_y)
                    dic2[matching_y] = y
                    

    for d in dic2:
        print(dic2[d])
