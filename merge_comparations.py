def comparations():

    result=0

    def merge(A: list, p: int, q: int, r: int):
        """
        :param A: Lista
        :param p: Inicio del primer arreglo
        :param q: Fin del primer arreglo
        :param r: Fin del segundo arreglo
        :return: arreglo ordenado
        """
        nonlocal result

        l: list = A[p:q + 1]
        # print(f"El arreglo l es {l}")
        r: list = A[q + 1:r + 1]
        # print(f"El arreglo r es {r}")
        array_r = []

        i: int = 0
        j: int = 0

        while len(l) > 0 and len(r) > 0:
            if l[0] <= r[0]:
                array_r.append(l[0])
                result += 1
                l.pop(0)

            else:
                array_r.append(r[0])
                result += 1
                r.pop(0)

        if len(l) == 0:
            array_r += r

        else:
            array_r += l

        return array_r

    # print(merge([1,5,8,4,2],0, 2, 4))

    def merge_sort(A: list, p: int, r: int):
        """
        :param A: Arreglo completo
        :param p: Inicio del arreglo
        :param r: Fin del arreglo
        :return: Arreglo ordenado
        """

        if p < r:
            q = (p + r) // 2
            merge_sort(A, p, q)
            merge_sort(A, q + 1, r)
            A[p:r + 1] = merge(A, p, q, r)

    array: list = input().split()
    A: list = list(map(int, array))
    p=0
    r=len(A)-1
    merge_sort(A, p, r)
    print(result)

comparations()



