def sum_bin(a,b):
    len_a=len(a)
    len_b=len(b)
    l=min(len(a),len(b))
    m=max(len(a),len(b))
    a=a[::-1]
    b=b[::-1]
    i=0
    j=0
    while i<len_a or j<len_b:
        if i>=len_a:
            a.append(0)
        if j>=len_b:
            b.append(0)

        i+=1
        j+=1

    current_c=0
    aca=[]
    result=[]
    for i in range(m):
        value=a[i]+b[i]+current_c
        if value<=1:
            aca.append(0)
            current_c=0
            result.append(value)

        
        else:
            aca.append(1)
            current_c=1
            if value==2:
                result.append(0)

            else:
                result.append(1)

    if current_c==1:
        result.append(1)


    return result[::-1]

def l_bin(a,b):
    len_a=len(a)
    len_b=len(b)
    l=min(len(a),len(b))
    m=max(len(a),len(b))
    b=b[::-1]
    i=0
    j=0
    while i<len_a or j<len_b:
        if i>=len_a:
            a.append(0)
        if j>=len_b:
            b.append(0)

        i+=1
        j+=1

    b=b[::-1]

    for i in range(len(b)):
        if b[i]==0:
            b[i]=1

        else:
            b[i]=0

    new_b=sum_bin(b, [1])
    result=sum_bin(a, new_b)
    result_r=list(map(str, result))
    if len(result_r) > len(a):
        return result[1:]  # descarta el primer bit y retorna el resto como lista
    else:
        return result


def karatsuba_bin(a, b):
    if len(a)==1 and len(b)==1:
        return [a[0]*b[0]]

    len_a=len(a)
    len_b=len(b)
    m=max(len_a,len_b)

    if m%2==0:
        if len_a!=len_b:
            a=a[::-1]
            b=b[::-1]
            i=0
            j=0
            while i<len_a or j<len_b:
                if i>=len_a:
                    a.append(0)
                if j>=len_b:
                    b.append(0)
                i+=1
                j+=1
            a=a[::-1]
            b=b[::-1]
    else:
        new_len=m+1
        a=a[::-1]
        b=b[::-1]
        i=0
        j=0
        while i<new_len or j<new_len:
            if i>=len_a:
                a.append(0)
            if j>=len_b:
                b.append(0)
            i+=1
            j+=1
        a=a[::-1]
        b=b[::-1]

    q=(len(a))//2
    a_high=a[:q]
    a_low=a[q:len(a)]
    b_high=b[:q]
    b_low=b[q:len(b)]

    ac=karatsuba_bin(a_high, b_high)
    bd=karatsuba_bin(a_low, b_low)
    a_sum=sum_bin(a_high, a_low)
    b_sum=sum_bin(b_high, b_low)
    z_p=karatsuba_bin(a_sum, b_sum)

    pr=l_bin(z_p, ac)
    z_m=l_bin(pr, bd)

    ac_c=ac+[0]*(2*q)
    zm_c=z_m+[0]*q

    result=sum_bin(sum_bin(ac_c, zm_c), bd)
    #result_s=list(map(str, result))
    #print("".join(result_s))
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    return result



a=list(map(int, list(input())))
b=list(map(int, list(input())))

f_result=karatsuba_bin(a,b)
result_s=list(map(str, f_result))
print("".join(result_s))


