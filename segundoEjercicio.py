def n0(coefficients):
    coefficients.reverse()
    n=1
    while True:
        #print("El n es igual a "+str(n))
        c_division = [n]
        for i in range(0, len(coefficients)):
            if i == 0:
                sub = n * coefficients[i]
                #print(sub)
                continue

            result = coefficients[i] + sub
            #print("result es "+str(result))
            #print(result)
            if(result<0):
                c_division.append(result)
                n+=1
                c_division.clear()
                break

            c_division.append(result)
            sub=result*n

        else:
            #print("entre aquí")
            #print(c_division)
            return n



t=int(input())
for i in range(0,t):
    array=list(map(int,input().split()))
    print(n0(array))







