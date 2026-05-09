def diffWaysToCompute(expression: str) -> list[int]:
    memo = {}

    def solve(expression: str):
        if expression in memo:
            return memo[expression]

        res = []

        for i in range(len(expression)):
            if expression[i] in "+-*":
                left = solve(expression[:i])
                right = solve(expression[i + 1:])

                for l in left:
                    for r in right:
                        if expression[i] == "+":
                            res.append(l + r)

                        elif expression[i] == "-":
                            res.append(l - r)

                        else:
                            res.append(l * r)

        if not res:
            res.append(int(expression))

        memo[expression] = res
        return res

    return solve(expression)


print(diffWaysToCompute("2-1-1"))