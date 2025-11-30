class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = prices[0]
        max_profit = 0

        for _, p in enumerate(prices, start=1):
            if p > lowest:
                max_profit = max(max_profit, p - lowest)
            elif p < lowest:
                lowest = p

        return max_profit
    

if __name__ == "__main__":
    solution = Solution()

    prices = [7,1,5,3,6,4]
    assert solution.maxProfit(prices) == 5

    prices = [7,6,4,3,1]
    assert solution.maxProfit(prices) == 0
