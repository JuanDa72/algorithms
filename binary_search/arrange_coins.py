def arrangeCoins(n: int) -> int:
    rows = 1
    while n >=rows:
        n -= rows
        rows += 1

    return rows-1


print(arrangeCoins(8))