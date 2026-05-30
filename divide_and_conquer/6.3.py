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
    if len(result_r)>len(a):
        result_r.pop(0)
        #print("".join(result_r))
        return result.pop(0)
    else:
        #print("".join(result_r))
        return result


def karatsuba_bin(a,b):
    len_a=len(a)
    len_b=len(b)
    m=max(len_a,len_b)
    if m%2==0:
        if len_a!=len_b:
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

            a=a[::-1]
            b=b[::-1]

    else:
        new_len=m+1
        l=min(len(a),len(b))
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

    if len(a)==1:
        return a[0]*b[0]
    
    else:
        q=(len(a))//2
        a_1=a[:q]
        b_1=a[q:len(a)]
        c=b[:q]
        d=b[q:len(b)]

        ac=karatsuba_bin(a_1,c)
        bd=karatsuba_bin(b_1,d)
        a_sum_b=sum_bin(a_1,b_1)
        c_sum_d=sum_bin(c,d)
        x_sum_y=sum_bin(a,b)

        z_p=karatsuba_bin(a_sum_b,c_sum_d)
        z_m=karatsuba_bin(z_p, x_sum_y)

        result=ac*(2**(2*q))+z_m*(2**q)+bd
        result_s=list(map(str, result))
        print("".join(result_s))


a=list(map(int, list(input())))
b=list(map(int, list(input())))

karatsuba_bin(a,b)



