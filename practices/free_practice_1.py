import math

coefficients=list(map(float, input().split()))
c1=0
c2=0
abs_1=0
for i in range(len(coefficients)):
    if i!=0:
       value=abs(coefficients[i])
       c2+=value
       abs_1+=value

    else:
        c2+=abs(coefficients[i])

n_0=math.floor((abs_1/coefficients[0])+1)
c1=coefficients[0]-(abs_1/n_0)


print(f"{n_0}\t{c1:.2f}\t{c2:.2f}")