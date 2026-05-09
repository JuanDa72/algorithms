n=int(input())
for i in range(n):
    coefficients=list(map(int,input().split()))[::-1]
    current=1
    while True:
        flag = False
        result=coefficients[0]
        for j in range(1,len(coefficients)):
            second=current*result
            result=coefficients[j]+second
            if result<0:
                flag=True
                break

        if flag:
            current+=1

        else:
            print(f"{current}")
            break

