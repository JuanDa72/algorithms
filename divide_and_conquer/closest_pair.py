import math

def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def fuerza_bruta(puntos):
    min_dist = float('inf')
    par = (None, None)
    n = len(puntos)
    for i in range(n):
        for j in range(i + 1, n):
            d = distancia(puntos[i], puntos[j])
            if d < min_dist:
                min_dist = d
                par = (puntos[i], puntos[j])
    return min_dist, par

def minima_franja(franja, d):
    # franja: puntos dentro de [mid_x - d, mid_x + d], ordenados por Y
    # d: mejor distancia encontrada hasta ahora
    min_dist = d
    par = (None, None)

    # Ordenamos por coordenada Y
    franja.sort(key=lambda p: p[1])

    for i in range(len(franja)):
        j = i + 1
        # Solo comparamos mientras la diferencia en Y sea menor que d
        while j < len(franja) and (franja[j][1] - franja[i][1]) < min_dist:
            dist = distancia(franja[i], franja[j])
            if dist < min_dist:
                min_dist = dist
                par = (franja[i], franja[j])
            j += 1

    return min_dist, par

def _closest_rec(puntos_x):
    # puntos_x: puntos ya ordenados por X
    n = len(puntos_x)

    # Caso base: 3 o menos puntos → fuerza bruta
    if n <= 3:
        return fuerza_bruta(puntos_x)

    # Dividir por el punto medio
    mid = n // 2
    mid_x = puntos_x[mid][0]

    # Llamadas recursivas a cada mitad
    d_izq, par_izq = _closest_rec(puntos_x[:mid])
    d_der, par_der = _closest_rec(puntos_x[mid:])

    # Nos quedamos con la menor distancia de ambos lados
    if d_izq < d_der:
        d, mejor_par = d_izq, par_izq
    else:
        d, mejor_par = d_der, par_der

    # Filtrar puntos dentro de la franja [mid_x - d, mid_x + d]
    franja = [p for p in puntos_x if abs(p[0] - mid_x) < d]
    # Revisar si hay un par cruzado más cercano en la franja
    d_franja, par_franja = minima_franja(franja, d)

    if d_franja < d:
        return d_franja, par_franja
    else:
        return d, mejor_par

def closest_pair(puntos):
    # Pre-ordenamos por X una sola vez → O(n log n)
    puntos_x = sorted(puntos, key=lambda p: p[0])
    return _closest_rec(puntos_x)

puntos = [
    (2, 3), (12, 30), (40, 50), (5, 1),
    (12, 10), (3, 4)
]

distancia_min, par = closest_pair(puntos)

print(f"Par más cercano: {par}")
print(f"Distancia: {distancia_min:.4f}")

# Verificación con fuerza bruta
d_bf, par_bf = fuerza_bruta(puntos)
print(f"\nVerificación fuerza bruta: {par_bf}, dist={d_bf:.4f}")