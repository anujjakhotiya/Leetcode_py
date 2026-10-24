class Solution:
    def finalPrices(self, prices):
        ans = prices[:]
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                ans[j] -= prices[i]
            stack.append(i)

        return ans