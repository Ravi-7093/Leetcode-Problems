class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        lst=[]
        for i in range(len(accounts)):
            ab=accounts[i]
            sum=0
            for i in range(len(ab)):
               sum=ab[i]+sum
            lst.append(sum)
        lst.sort()
        return lst[-1]
                
            
        
