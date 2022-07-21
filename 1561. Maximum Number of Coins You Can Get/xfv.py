class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n=len(piles)//3
        sum=piles[n]
        for i in range(n+2,len(piles),2):
            sum =sum+piles[i]
        return sum
