class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        bal_var =0
        count=0
        for i in s:
            if(i=="L"):
                bal_var+=1
                if(bal_var==0):
                    count+=1
            else:
                bal_var-=1
                if(bal_var==0):
                    count+=1
        return count
