class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        new_count=0
        res=0
        for i in s:
            if(i=="1"):
                count+=1
        new_count=count
        for i in range(len(s)-1):
            if s[i]=="0":
                new_count+=1
            else:
                new_count-=1
            if (new_count>res):
                res=new_count
        return res
