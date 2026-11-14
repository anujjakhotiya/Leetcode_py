class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp0, dp1, dp2 = float('inf'), float('inf'), 0
        
        for cost in costs:
            curr = cost + min(dp2 + 1,dp1 + 4,dp0 + 9 )
            dp0, dp1, dp2 = dp1, dp2, curr
            
        return dp2