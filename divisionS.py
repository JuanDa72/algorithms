def syntactic(array, a):
    # array: Arreglo de los coeficientes del polinomio a dividir
    # a: termino independiente del divisor, por ejemplo, si tenemos como
    # dividendo "x-3" a=-3

    x=-a
    sub=0
    answer=[array[0]]
    for i in range(0, len(array)):
        if i==0:
            sub=x*array[i]
            continue

        result=array[i]+sub
        answer.append(result)
        sub=result*x

    return answer


print(syntactic([2,-3,4,-5],-2))

