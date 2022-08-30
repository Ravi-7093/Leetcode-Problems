class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n==1):#check if n==1 then return True 
            return True
        if(n==0):
            return False#check if n==1 return False
        else:
            if(n%4==0):#check if n is completely divisible by 4 
                n=n//4#divide the n by 4 
                return self.isPowerOfFour(n) # using recursion reduce the number and check if it returns 1 
            else:
                return False
