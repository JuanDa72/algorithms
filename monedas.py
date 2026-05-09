n:int=int(input())

def coins(n):
    counter=1
    number=0
    while number<=n:
        counter += 1
        number=3**counter

    print(counter)

coins(n)


