def maxProfit(prices: list[int]) -> int:
    gan:int=0
    minimum:int=prices[0]

    for i in range(1, len(prices)):
        if(prices[i]<minimum):
            minimum=prices[i]

        today_value:int=prices[i]-minimum
        gan=max(gan, today_value)

    return gan



print(maxProfit([7,6,4,3,1]))
