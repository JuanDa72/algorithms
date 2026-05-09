def nthSuperUglyNumber(n: int, primes: list[int]) -> int:
    dp = [0] * n
    dp[0] = 1

    positions = [0] * len(primes)

    for i in range(1, n):
        minimum = float('inf')
        to_increase = 0
        results=[0]*len(positions)
        for j in range(len(positions)):
            current_value = dp[positions[j]] * primes[j]
            results[j]=current_value

            if current_value < minimum:
                minimum = current_value
                to_increase = j

        positions[to_increase] += 1
        dp[i]=minimum

        for k in range(len(results)):
            if results[k]==minimum and k!=to_increase:
                positions[k]+=1

    return dp[n - 1]


print(nthSuperUglyNumber(1, [2,3,5]))
