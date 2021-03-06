class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = prices[0]
        for i in range(len(prices)): 
            if prices[i] < mini :
                mini = prices[i]
            elif prices[i] - mini > maxi:
                maxi = prices[i] - mini
        return maxi