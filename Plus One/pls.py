class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strg=""
        for i in digits:
            strg =strg+str(i)
        strg=int(strg)
        res=strg+1
        x=[int(a) for a in str(res)]
        return x
