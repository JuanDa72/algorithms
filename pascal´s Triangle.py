
def generate(numRows:int)->list[list[int]]:
    solution=[]
    numRows+=1
    for i in range(numRows):
        new_array = []
        if(i<2):
            for j in range(i+1):
               # new_array.clear()
                new_array.append(1)
                #print(new_array)
            solution.append(new_array)
            #print(solution)

        else:
            new_array=[1]
            for k in range(1,i):
                new_array.append(solution[i-1][k-1]+solution[i-1][k])

            new_array.append(1)
            solution.append(new_array)

    return solution[numRows-1]

print(generate(1))