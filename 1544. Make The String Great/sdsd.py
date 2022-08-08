class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        for i in s:
            if res and res[-1].isupper() and res[-1].lower()==i:#check for small character
                res.pop()
            elif res and res[-1].islower() and res[-1].upper()==i:#check for capital letter 
                res.pop()
            else:
                res.append(i)
        return ''.join(res)
