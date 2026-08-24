class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maximum = 0
        lowest = prices[0]

        while right < len(prices):
            maximum = max(maximum, prices[right] - prices[left])
            
            if prices[right] < lowest:
                lowest = prices[right]
                left = right
            right += 1  

        return maximum