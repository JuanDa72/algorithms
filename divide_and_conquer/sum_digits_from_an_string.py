def sum_dac(string):
    if len(string)==1:
        return int(string)

    else:
        n=len(string)//2
        fv=sum_dac(string[:n])
        sc=sum_dac(string[n:])
        return fv+sc

print(sum_dac("5"))