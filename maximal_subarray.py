import math


def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -math.inf
    total = 0
    max_left = mid

    # Buscar mejor subarreglo en mitad izquierda (hacia atrás desde mid)
    for i in range(mid, low - 1, -1):
        total += A[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = -math.inf
    total = 0
    max_right = mid + 1

    # Buscar mejor subarreglo en mitad derecha (hacia adelante desde mid+1)
    for j in range(mid + 1, high + 1):
        total += A[j]
        if total > right_sum:
            right_sum = total
            max_right = j

    return (max_left, max_right, left_sum + right_sum)


def find_maximum_subarray(A, low, high):
    # Caso base: un solo elemento
    if high == low:
        return (low, high, A[low])

    else:
        mid = (low + high) // 2  # División entera

        # Llamadas recursivas
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

        # Comparar y devolver el mejor
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)



# Función auxiliar para probar
def test_max_subarray(A):
    print(f"Arreglo: {A}")
    low, high, total = find_maximum_subarray(A, 0, len(A) - 1)
    subarray = A[low:high + 1]
    print(f"Subarreglo máximo: {subarray}")
    print(f"Índices: {low} a {high}")
    print(f"Suma: {total}\n")
    return low, high, total

test_max_subarray([1,5,-3,45,3,-35])