t:int=int(input())

for i in range(t):
    potency,objetive=map(int, input().split())

    answer=[]
    steps=0
    chocolate=2**potency
    vanilla= 2**potency

    if(chocolate==objetive):
        print(0)
        print()
        continue


    elif(chocolate+vanilla-1)>2*objetive:
        while(chocolate!=2*objetive):
            if vanilla%2==0:
                chocolate+=vanilla/2
                vanilla=vanilla/2
                answer.append(2)
                steps+=1

            else:
                print("No es par y fallo xd")

        if chocolate%2==0:
            vanilla+=chocolate/2
            chocolate=chocolate/2
            answer.append(1)
            steps+=1

    else:
        #print("Entramooos")
        while(chocolate!=objetive):
            vanilla+=chocolate/2
            chocolate = chocolate / 2
            answer.append(1)
            steps+=1

            if(chocolate+vanilla/2)==objetive:
                result=vanilla/2
                vanilla=vanilla/2
                answer.append(2)
                steps+=1
                chocolate+=result


    print(steps)
    print(*answer)



