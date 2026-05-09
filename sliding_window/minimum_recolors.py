def minimumRecolors(blocks: str, k: int) -> int:
    minimum: int = float('inf')
    current: int = 0
    left: int = 0
    for right in range(len(blocks)):
        if blocks[right] == "W":
            current += 1

        if right - left == k-1:

            if current < minimum:
                minimum = current

            if blocks[left] == "W":
                current -= 1

            left += 1

    return minimum


print(minimumRecolors("WBBWWBBWBW",7))