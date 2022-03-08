class Solution: # 贪心思路
    def maxProfit(self, prices, fee: int) -> int:
        result = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] >= minPrice and prices[i] <= minPrice + fee:
                continue
            else:
                result += prices[i] - minPrice - fee
                minPrice = prices[i] - fee
        return result

s = Solution()
print(s.maxProfit(prices = [1, 3, 2, 8, 4, 9, 10, 15], fee = 2))