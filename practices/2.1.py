n:int=int(input())
for i in range(n):
    array=list(map(int,input().split()))
    minimum=min(array)
    maximum=max(array)
    sum=0
    quadrate=0
    cube=0
    for j in range(minimum, maximum+1):
        sum+=j
        quadrate+=j**2
        cube+=j**3

    print(sum, quadrate, cube)

