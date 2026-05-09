def mistery(n):
    x=0
    y=1
    for i in range(1,n+1):
        y=y*i
        while x<y:
            x=x+1


print(mistery(5))